# Storytelling with Data — Runnable Examples

Zero-dependency Python examples demonstrating SWD capabilities. Each script is standalone.

## Quick Start

```bash
PYTHONPATH=. python examples/01_chart_selection.py
PYTHONPATH=. python examples/02_data_story.py
PYTHONPATH=. python examples/03_story_building.py
PYTHONPATH=. python examples/04_declutter_diagnosis.py
```

## Examples

| Script | What It Shows |
|--------|--------------|
| `01_chart_selection.py` | Intelligent chart type recommendation based on data characteristics |
| `02_data_story.py` | Building a 3-act data narrative with evidence |
| `03_story_building.py` | Story building for a data narrative with protagonist, imbalance, and call-to-action |
| `04_declutter_diagnosis.py` | Automated clutter detection and cleanup recommendations |

### Expected Output

```
>>> Chart Recommendation: Compare categories
>>> Data: [Category A: 35, Category B: 52, Category C: 28]
>>>
>>>  Recommended: Bar Chart (horizontal)
>>>  Rationale: Clear comparison of discrete categories; horizontal bars
>>>             allow easy label reading and value comparison.
>>>  Design tip: Sort descending, use gray bars with one highlight color.
```

*Actual output varies based on input — run to see the full analysis.*

## Try Before You Decide

```bash
PYTHONPATH=. python -c "
from swd import SWDSkill
skill = SWDSkill('My Project')
chart = skill.recommend_chart('compare', ['Category A', 'Category B', 'Category C'], [35, 52, 28])
print(chart)
"
```

## Tips / 提示

- Set `PYTHONPATH=.` to run examples without installing
- No `pip install` required — SWD uses only Python standard library
- Combine with QuantUX examples: QuantUX generates data → SWD visualizes it
- See [USAGE.md](../USAGE.md) for detailed API documentation

## 🔗 Ecosystem Integration / 生态集成

SWD is the presentation layer of the AliDujie UX Research Ecosystem. Chain it with other skills:

- **QuantUX → SWD**: [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) experiment data → SWD data stories
- **UDM → SWD**: [UDM](https://github.com/AliDujie/universal-design-methods) research reports → SWD executive narratives
- **VPD → SWD**: [VPD](https://github.com/AliDujie/value-proposition-design) canvas scores → SWD value stories
- **JTBD → SWD**: [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) opportunity scores → SWD need stories
- **Persona → SWD**: [Persona](https://github.com/AliDujie/web-persona-skill) economics → SWD user stories
- **SWD → STM**: SWD data stories → [STM](https://github.com/AliDujie/Structured-Thinking-Model) strategic frameworks

See the [full pipeline example](../README.md#complete-pipeline-example) in README.md for a 7-skill end-to-end workflow.
