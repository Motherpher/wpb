# CareerHub visual system

CareerHub's interface is built around the same mental model as the workflow:

**Find jobs → Choose job → Apply**

The graphic language intentionally uses an organic journey rather than a conventional corporate dashboard grid.

## Palette

| Role | Colour |
|---|---|
| Working surface | `#F7F8F3` |
| Journey / primary action | `#2E50E8` |
| Information blue | `#2A72A3` |
| Soft information field | `#C6D8E6` |
| Deadline / urgency | `#F97279` |
| Apply / forward motion | `#F6AB16` |
| Text | `#111111` |

The pale blue, coral and blue values follow the supplied palette reference. The cobalt journey line and warm yellow extend that language using the supplied journey/poster references.

## Design principles

- one continuous journey rather than several competing dashboards
- large simple stage labels
- strong whitespace
- organic curves instead of technical flowchart arrows
- urgency expressed with coral, not with clutter
- numbers used only where they help orientation
- technical controls placed below the normal user journey
- live data visual rather than a static illustration

## Generated visual

`careerhub-journey.svg` is regenerated from CareerHub state.

It currently visualises:

- live sourced leads
- active chosen cases
- applications in process
- deadlines within seven days
- total jobs retained in the historic vault

The SVG is the single hero visual for CareerHub and should remain the visual anchor if CareerHub later becomes a standalone web interface.
