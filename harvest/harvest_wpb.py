#!/usr/bin/env python3
"""WPB public-web metadata harvester.

Discovers and records public metadata about Weronika Pérez Borjas.
No paywall bypass; no full article bodies are persisted.
"""

from __future__ import annotations

import argparse, csv, hashlib, json, os, re, sys, time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
HARVEST = ROOT / "harvest"
OUT = HARVEST / "output"
USER_AGENT = "WPB-Archive-Metadata-Harvester/1.0 (+https://github.com/Hybrismannen/wpb)"
TIMEOUT = 20

def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def write_jsonl(path: Path, rows):
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

def norm_url(url: str) -> str:
    url, _ = urldefrag(url.strip())
    return url

def hostname(url: str) -> str:
    return (urlparse(url).hostname or "").lower()

def allowed(url: str, domains: set[str]) -> bool:
    h = hostname(url)
    return any(h == d or h.endswith("." + d) for d in domains)

def meta(soup: BeautifulSoup, *, name=None, prop=None):
    attrs = {"name": name} if name else {"property": prop}
    tag = soup.find("meta", attrs=attrs)
    return (tag.get("content") or "").strip() if tag else None

def all_meta(soup: BeautifulSoup, key: str):
    vals=[]
    for tag in soup.find_all("meta"):
        if (tag.get("name") or tag.get("property") or "").lower() == key.lower():
            v=(tag.get("content") or "").strip()
            if v and v not in vals: vals.append(v)
    return vals

def jsonld_nodes(soup: BeautifulSoup):
    out=[]
    for tag in soup.find_all("script", type="application/ld+json"):
        raw=tag.string or tag.get_text()
        if not raw: continue
        try:
            obj=json.loads(raw)
            if isinstance(obj,list): out.extend(obj)
            elif isinstance(obj,dict) and isinstance(obj.get("@graph"),list): out.extend(obj["@graph"])
            else: out.append(obj)
        except Exception:
            continue
    return [x for x in out if isinstance(x,dict)]

def flatten_authors(v):
    if v is None: return []
    if isinstance(v,str): return [v.strip()]
    if isinstance(v,dict): return flatten_authors(v.get("name"))
    if isinstance(v,list):
        out=[]
        for x in v: out.extend(flatten_authors(x))
        return [x for x in out if x]
    return []

def visible_credit_lines(text: str, names: list[str]):
    lines=[re.sub(r"\s+"," ",x).strip() for x in text.splitlines()]
    pats=("words by","written by","by ","author","text ","tekst","credits","styling","translation","tłumac")
    out=[]
    for line in lines:
        ll=line.lower()
        if any(n.lower() in ll for n in names) and any(p in ll for p in pats):
            if 0 < len(line) <= 500 and line not in out: out.append(line)
    return out[:30]

def content_fingerprint(soup: BeautifulSoup):
    clone=BeautifulSoup(str(soup), "html.parser")
    for t in clone(["script","style","nav","footer","header","form","noscript"]): t.decompose()
    text=re.sub(r"\s+"," ",clone.get_text(" ", strip=True)).strip()
    return {
        "visible_word_count": len(text.split()),
        "visible_text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest() if text else None
    }

class Robots:
    def __init__(self, session):
        self.session=session; self.cache={}
    def can_fetch(self, url):
        h=hostname(url)
        if not h: return False
        if h not in self.cache:
            rp=RobotFileParser()
            robots=f"{urlparse(url).scheme or 'https'}://{h}/robots.txt"
            try:
                r=self.session.get(robots, timeout=TIMEOUT)
                rp.parse(r.text.splitlines() if r.ok else [])
            except Exception:
                rp.parse([])
            self.cache[h]=rp
        return self.cache[h].can_fetch(USER_AGENT,url)

def extract(session, robots, url, names, domains, delay):
    record={"url":url,"retrieved_at":datetime.now(timezone.utc).isoformat()}
    if not robots.can_fetch(url):
        record.update({"status":"robots-denied"})
        return record, []
    time.sleep(delay)
    try:
        r=session.get(url, timeout=TIMEOUT, allow_redirects=True)
        record.update({
            "http_status":r.status_code,
            "final_url":r.url,
            "content_type":r.headers.get("content-type"),
            "etag":r.headers.get("etag"),
            "last_modified":r.headers.get("last-modified"),
        })
        if not r.ok or "html" not in (r.headers.get("content-type") or "").lower():
            return record, []
        soup=BeautifulSoup(r.text,"html.parser")
        title=(soup.title.get_text(" ",strip=True) if soup.title else None)
        canon=soup.find("link", rel=lambda v: v and "canonical" in v)
        nodes=jsonld_nodes(soup)
        authors=[]
        dates_pub=[]; dates_mod=[]; keywords=[]
        for n in nodes:
            authors += flatten_authors(n.get("author"))
            for k in ("datePublished","uploadDate"):
                if n.get(k): dates_pub.append(str(n[k]))
            if n.get("dateModified"): dates_mod.append(str(n["dateModified"]))
            kw=n.get("keywords")
            if isinstance(kw,str): keywords += [x.strip() for x in kw.split(",") if x.strip()]
            elif isinstance(kw,list): keywords += [str(x).strip() for x in kw if str(x).strip()]
        authors += all_meta(soup,"author")
        authors=list(dict.fromkeys(a for a in authors if a))
        full_text=soup.get_text("\n",strip=True)
        identity_hits=[n for n in names if n.lower() in full_text.lower() or any(n.lower() in a.lower() for a in authors)]
        record.update({
            "title":title,
            "canonical_url":(canon.get("href") if canon else None),
            "description":meta(soup,name="description") or meta(soup,prop="og:description"),
            "og_title":meta(soup,prop="og:title"),
            "og_type":meta(soup,prop="og:type"),
            "og_image":meta(soup,prop="og:image"),
            "twitter_image":meta(soup,name="twitter:image"),
            "language":(soup.html.get("lang") if soup.html else None),
            "authors":authors,
            "published_dates":list(dict.fromkeys(dates_pub + all_meta(soup,"article:published_time"))),
            "modified_dates":list(dict.fromkeys(dates_mod + all_meta(soup,"article:modified_time"))),
            "section":meta(soup,prop="article:section"),
            "keywords":list(dict.fromkeys(keywords + all_meta(soup,"keywords"))),
            "jsonld_types":list(dict.fromkeys(str(n.get("@type")) for n in nodes if n.get("@type"))),
            "identity_hits":identity_hits,
            "credit_lines":visible_credit_lines(full_text,names),
            **content_fingerprint(soup)
        })
        links=[]
        for a in soup.find_all("a", href=True):
            href=norm_url(urljoin(r.url,a["href"]))
            if href.startswith(("http://","https://")) and allowed(href,domains):
                links.append(href)
        return record, list(dict.fromkeys(links))
    except Exception as e:
        record.update({"status":"error","error":repr(e)})
        return record, []

def brave_search(session, queries):
    key=os.getenv("BRAVE_SEARCH_API_KEY")
    if not key: return []
    rows=[]
    for q in queries:
        try:
            r=session.get("https://api.search.brave.com/res/v1/web/search",
                params={"q":q,"count":20},headers={"X-Subscription-Token":key},timeout=TIMEOUT)
            data=r.json() if r.ok else {}
            for item in data.get("web",{}).get("results",[]):
                rows.append({"query":q,"title":item.get("title"),"url":item.get("url"),"description":item.get("description")})
        except Exception as e:
            rows.append({"query":q,"error":repr(e)})
        time.sleep(.5)
    return rows

def wayback(session, urls):
    rows=[]
    for url in urls:
        try:
            api="https://web.archive.org/cdx/search/cdx"
            r=session.get(api,params={"url":url,"output":"json","fl":"timestamp,original,statuscode,mimetype,digest","filter":"statuscode:200","collapse":"digest","limit":"100"},timeout=TIMEOUT)
            data=r.json() if r.ok else []
            for row in data[1:] if isinstance(data,list) and data else []:
                rows.append(dict(zip(["timestamp","original","statuscode","mimetype","digest"],row)))
        except Exception as e:
            rows.append({"original":url,"error":repr(e)})
        time.sleep(.25)
    return rows

def scholarly(session, names, do_crossref, do_openalex):
    rows=[]
    query=names[0]
    if do_crossref:
        try:
            r=session.get("https://api.crossref.org/works",params={"query.author":query,"rows":100},timeout=TIMEOUT)
            for x in (r.json().get("message",{}).get("items",[]) if r.ok else []):
                rows.append({"source":"crossref","doi":x.get("DOI"),"title":(x.get("title") or [None])[0],"url":x.get("URL"),"published":x.get("published-print") or x.get("published-online"),"authors":x.get("author")})
        except Exception as e: rows.append({"source":"crossref","error":repr(e)})
    if do_openalex:
        try:
            r=session.get("https://api.openalex.org/works",params={"search":query,"per-page":100},timeout=TIMEOUT)
            for x in (r.json().get("results",[]) if r.ok else []):
                rows.append({"source":"openalex","id":x.get("id"),"doi":x.get("doi"),"title":x.get("title"),"publication_date":x.get("publication_date"),"primary_location":x.get("primary_location")})
        except Exception as e: rows.append({"source":"openalex","error":repr(e)})
    return rows

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--deep",action="store_true")
    p.add_argument("--max-pages",type=int,default=300)
    p.add_argument("--delay",type=float,default=1.25)
    p.add_argument("--wayback",action="store_true")
    p.add_argument("--crossref",action="store_true")
    p.add_argument("--openalex",action="store_true")
    p.add_argument("--brave-search",action="store_true")
    args=p.parse_args()

    OUT.mkdir(parents=True,exist_ok=True)
    seeds=load_json(HARVEST/"seeds.json")
    corpus=load_json(ROOT/"data"/"corpus.json")
    names=seeds["identity_variants"]
    domains=set(seeds["allow_domains"])

    session=requests.Session()
    session.headers.update({"User-Agent":USER_AGENT,"Accept-Language":"en,sv,pl;q=0.8,*;q=0.5"})
    robots=Robots(session)

    start=[w["url"] for w in corpus["works"] if w.get("url")] + seeds["author_pages"]
    search_rows=[]
    if args.brave_search:
        search_rows=brave_search(session,seeds["search_queries"])
        start += [x["url"] for x in search_rows if x.get("url") and allowed(x["url"],domains)]

    q=deque(dict.fromkeys(norm_url(x) for x in start))
    seen=set(); fetched=[]; positives=[]; errors=[]; candidates=set()
    seed_hosts={hostname(x) for x in seeds["author_pages"]}

    while q and len(seen)<args.max_pages:
        url=q.popleft()
        if url in seen or not allowed(url,domains): continue
        seen.add(url)
        rec,links=extract(session,robots,url,names,domains,args.delay)
        fetched.append(rec)
        if rec.get("status")=="error": errors.append(rec)
        positive=bool(rec.get("identity_hits") or any(any(n.lower() in a.lower() for n in names) for a in rec.get("authors",[])))
        if positive:
            positives.append(rec)
            candidates.add(rec.get("canonical_url") or rec.get("final_url") or url)
        # Follow one hop from author/tag pages even without deep mode; deep mode follows all allowlisted pages.
        if args.deep or hostname(url) in seed_hosts or url in seeds["author_pages"]:
            for link in links:
                if link not in seen: q.append(link)

    urls=list(dict.fromkeys([x for x in candidates if x]))
    wb=wayback(session,urls) if args.wayback else []
    sch=scholarly(session,names,args.crossref,args.openalex)

    write_jsonl(OUT/"all_fetched_metadata.jsonl",fetched)
    write_jsonl(OUT/"positive_matches.jsonl",positives)
    write_jsonl(OUT/"errors.jsonl",errors)
    write_jsonl(OUT/"wayback_captures.jsonl",wb)
    write_jsonl(OUT/"scholarly_records.jsonl",sch)
    write_jsonl(OUT/"search_results.jsonl",search_rows)

    with (OUT/"candidate_urls.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["url"]); w.writeheader()
        for url in sorted(urls): w.writerow({"url":url})

    report={
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "pages_seen":len(seen),"pages_fetched":len(fetched),
        "positive_matches":len(positives),"candidate_urls":len(urls),
        "errors":len(errors),"wayback_records":len(wb),"scholarly_records":len(sch),
        "full_text_persisted":False
    }
    (OUT/"discovery_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
