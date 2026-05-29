# Storytelling with Data — Runnable Examples

Zero-dependency Python examples demonstrating SWD capabilities. Each script is standalone.

## Quick Start

```bash
PYTHONPATH=. python examples/01_chart_selection.py
PYTHONPATH=. python examples/02_data_story.py
PYTHONPATH=. python examples/02_story_building.py
PYTHONPATH=. python examples/03_declutter_diagnosis.py
```

## Examples

| Script | What It Shows |
|--------|--------------|
| `01_chart_selection.py` | Intelligent chart type recommendation based on data characteristics |
| `02_data_story.py` | Building a 3-act data narrative with evidence |
| `02_story_building.py` | Story building for a data narrative with protagonist, imbalance, and call-to-action |
| `03_declutter_diagnosis.py` | Automated clutter detection and cleanup recommendations |

## Try Before You Decide

```bash
PYTHONPATH=. python -c "
from swd import SWDSkill
skill = SWDSkill('My Project')
chart = skill.recommend_chart('compare', ['Category A', 'Category B', 'Category C'], [35, 52, 28])
print(chart)
"
```
