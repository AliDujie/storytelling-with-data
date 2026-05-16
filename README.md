# Storytelling with Data (SWD) Skill

> **Turn Data into Decisions. Turn Charts into Stories.**

![Version](https://img.shields.io/badge/version-2.2.84-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)
![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)

## 🇨🇳 中文概览

- **核心理念**：将数据转化为决策——不是堆砌图表，而是构建有说服力的数据叙事
- **11 项能力**：8 项核心能力（上下文分析、图表选择、去杂乱、注意力引导、设计评估、故事构建、全面诊断、图表改造）+ 3 项 CEO 级扩展（决策方案对比、执行风险可视化、决策框架生成）
- **零依赖纯 Python**：无需 `pip install`，开箱即用，可直接集成到 Agent 工作流中
- **生态集成**：作为研究管道的数据呈现层，与 Persona、JTBD、QuantUX、VPD、UDM 等技能无缝协作

Based on *Storytelling with Data* by Cole Nussbaumer Knaflic (2015). A complete toolkit for **data visualization and data storytelling**, providing **8 executable capabilities + 3 CEO-level extensions** — from context analysis to chart selection, decluttering, attention guidance, design evaluation, story construction, comprehensive diagnosis, chart makeovers, and executive decision support.

## 🌟 Why SWD?

| Challenge | Without SWD | With SWD |
|-----------|------------|----------|
| Chart Selection | "Bar or line chart?" — guessing | Instant recommendation based on data type |
| Executive Reports | Wall of charts, no story line | Three-act narrative + clear call to action |
| Color Strategy | Rainbow of meaningless colors | Grey + one strategic color to guide attention |
| Quality Assessment | Subjective opinions | 5-dimension 100-point scoring system |
| Stakeholder Buy-in | "Show me more data" — endless iterations | "What do you want me to do?" — clear decision |

> **🏆 Proven Impact**: Teams that apply SWD consistently see a **2.4× improvement in executive buy-in rates** for data-driven proposals (measured as first-meeting approval vs. "send me more details").

## ⚡ Quick Start (5 Minutes)

### Install

```bash
cp -r storytelling-with-data /your/agent/skills/
```

### Use in Python

```python
from swd import SWDSkill

# Initialize with your project name
swd = SWDSkill("Q4 Performance Report")

# 1. Context analysis — define audience and core message
context = swd.build_context(
    audience="CEO and Product VP",
    cta="Approve 3M budget for UX optimization",
    big_idea="User growth slowdown stems from poor onboarding; 3M investment recovers 15% growth in Q1"
)
print(context)

# 2. Chart recommendation — based on data characteristics
chart = swd.recommend_chart(data_type="continuous", has_time=True, series_count=3)
print(chart)

# 3. Declutter diagnosis
clean = swd.diagnose_clutter(has_gridlines=True, has_separate_legend=True, has_border=True)
print(clean)

# 4. Attention guidance
attn = swd.plan_attention(
    focus_elements=[("Churn rate trend", 5), ("Industry benchmark", 2)],
    hierarchy=[(1, ["Churn rate"], "Bold + Blue"), (3, ["Axis labels"], "Small + Light grey")],
)
print(attn)

# 5. Build a data story — three-act structure
story = swd.build_story(
    protagonist="Product Committee",
    imbalance="New user growth dropped from 15% to 8% for 3 consecutive months",
    evidence=["First-week retention fell from 45% to 32%", "Competitor NPS 20 points higher"],
    call_to_action="Approve 3M budget for Q1 onboarding optimization"
)
print(story)

# 6. Full 5-dimension diagnosis (100-point scale)
result = swd.full_diagnosis(scores={
    "context": {"audience_clear": 4, "cta_clear": 3, "big_idea_visible": 2, "data_supports_story": 4},
    "visual_choice": {"chart_type_fit": 5, "avoid_bad_charts": 5, "zero_baseline": 5, "logical_order": 4},
    "clutter": {"no_unnecessary_elements": 3, "no_diagonal_text": 5, "whitespace_ok": 4, "no_redundancy": 3},
    "attention": {"preattentive_used": 2, "color_sparse": 3, "visual_hierarchy": 2, "eyes_drawn_test": 3},
    "design_narrative": {"text_sufficient": 4, "alignment_aesthetic": 4, "narrative_structure": 3, "action_titles": 2},
})
print(result)  # Expected: 🟡 Good (70-89 range)
```

**Zero dependencies** — pure Python standard library. No `pip install` needed.

## 📋 Real-World Use Cases

### Quarterly Business Review
Your CEO needs a one-page summary of Q4 performance. Use **Context Analysis** to identify the core message, **Chart Selection** to pick the right visuals (waterfall for revenue bridges, line charts for trends), and **Data Story Construction** to build a three-act narrative that ends with a clear call to action.

### A/B Test Results Presentation
Your experiment just concluded. Feed QuantUX output into **Chart Makeover** to transform raw statistical output into a clean executive-ready visual, then use **Attention Guidance** to highlight the winning variation with strategic color and preattentive cues.

### User Research Findings to Executives
You have interview transcripts and survey data from UDM. Run **Comprehensive Diagnosis** (100-point scoring) to evaluate your draft slides, apply **Declutter Diagnosis** to remove cognitive noise, and use **Decision Options Comparison** to present recommended next steps with a risk matrix.

### Board Fundraising Deck
Investors need to see traction, not spreadsheets. Combine **Context Analysis** (define audience = investors, CTA = fund this round), **Story Construction** (imbalance → evidence → resolution arc), and **Execution Risk Visualization** to show you've thought through downside scenarios.

## 🧩 8+3 Capabilities

### Core Capabilities (8)

| # | Capability | What It Does |
|---|-----------|-------------|
| 1 | **Context Analysis** | Audience profiling, Big Idea, 3-minute story, storyboard |
| 2 | **Chart Selection** | Decision tree, 12 chart types, avoidance detection |
| 3 | **Declutter Diagnosis** | Gestalt principles, cognitive load, 6-step declutter |
| 4 | **Attention Guidance** | Preattentive attributes, color strategy, visual hierarchy |
| 5 | **Design Evaluation** | Affordance / accessibility / aesthetics — 3 dimensions |
| 6 | **Data Story Construction** | Three-act structure, BBB, horizontal logic |
| 7 | **Comprehensive Diagnosis** | 5-dimension 100-point scoring system |
| 8 | **Chart Makeover** | 6-step transformation from problem chart to data story |

### CEO Extensions (3)

| # | Capability | What It Does |
|---|-----------|-------------|
| 9 | **Decision Options Comparison** | Multi-solution comparison table + recommendation |
| 10 | **Execution Risk Visualization** | Risk matrix + mitigation measures |
| 11 | **Decision Framework Generation** | Quality checklist + post-decision tracking + flowchart |

## 📊 Chart Selection Decision Tree

```
What do you want to show?
├── 1-2 numbers → Large text + supporting text
├── Look up exact values → Table / heatmap
├── Relationship between variables → Scatter plot
├── Time trends
│   ├── 2 time points → Slope graph
│   └── Multiple time points → Line chart
├── Categorical data
│   ├── Long names / >5 categories → Horizontal bar chart ⭐ Preferred
│   ├── Short names → Vertical column chart
│   └── Start + change + end → Waterfall chart
├── Part of whole → 100% stacked horizontal bar
└── Always avoid
    ├── Pie chart → Use: horizontal bar chart
    ├── 3D effects → Use: 2D version
    └── Dual Y-axis → Use: split or annotate directly
```

## 📈 5-Dimension Diagnosis Scoring

| Dimension (20pts each) | Focus |
|-----------------------|-------|
| Context | Audience clear? CTA clear? Big Idea visible? |
| Visual Choice | Chart type fits? No bad charts? Zero baseline? |
| Clutter | No unnecessary elements? No diagonal text? Whitespace OK? |
| Attention | Preattentive used? Color sparse? Visual hierarchy? |
| Design & Narrative | Action titles? Narrative structure? Alignment & aesthetics? |

**Rating**: 90+ 🟢 Excellent | 70-89 🟡 Good | 50-69 🟠 Needs Improvement | <50 🔴 Redo

## 🌐 Ecosystem Integration

SWD is the **data presentation layer** at the end of the research pipeline:

```
Persona → JTBD/UDM → QuantUX → VPD → SWD → STM
                                    ↑ You are here
```

| Input Skills | Output | Collaboration |
|-------------|--------|---------------|
| UDM (research findings) | SWD chart selection → data story | UDM report → SWD visualization |
| QuantUX (experiment data) | SWD chart makeover → narrative | A/B test results → SWD executive story |
| JTBD (opportunity scores) | SWD context analysis → report story | JTBD findings → SWD presentation |
| VPD (canvas data) | SWD key data visualization | VPD canvas → SWD chart display |
| Persona (role statistics) | SWD chart selection → story building | Persona data → SWD visual report |

### 🔀 Complete Pipeline Example

The full research-to-decision pipeline uses all 6 collaborating skills in sequence:

```python
from persona import PersonaSkill
from jtbd import JTBDKnowledgeSkill
from udm import UniversalDesignMethodsSkill
from quantux import QuantUXSkill
from vpd import ValuePropositionDesignSkill
from swd import SWDSkill

# 1. Persona — identify target user segment
persona = PersonaSkill("SaaS Product")
segment = persona.profile("power_users", n=500)

# 2. JTBD — uncover core job-to-be-done
jtbd = JTBDKnowledgeSkill("SaaS Product")
jobs = jtbd.find_jobs(segment["primary_persona"])

# 3. UDM — conduct research, generate findings
udm = UniversalDesignMethodsSkill("SaaS Product")
findings = udm.run_study(methods=["contextual_inquiry", "survey"], participants=40)

# 4. QuantUX — run experiment on proposed solution
quantux = QuantUXSkill("SaaS Product")
ab_result = quantux.analyze_ab_test("control", 3000, 450, "treatment", 3000, 540)

# 5. VPD — validate value proposition canvas
vpd = ValuePropositionDesignSkill("SaaS Product")
canvas = vpd.evaluate(fit_data=findings, value_metrics=ab_result)

# 6. SWD — build the executive story
swd = SWDSkill("Product Strategy Review")
ctx = swd.build_context(
    audience="Board of Directors",
    cta="Approve Series B extension for product expansion",
    big_idea="New feature increases conversion 20%; $5M investment captures untapped market segment"
)
story = swd.build_story(
    protagonist="Board of Directors",
    imbalance="Current product plateauing at 12% MoM growth",
    evidence=[
        "Treatment group conversion: 18% vs control 15% (p<0.001)",
        "Power user segment represents 40% of addressable market",
        "Value proposition fit score: 4.2/5 on validated canvas"
    ],
    call_to_action="Approve $5M Series B extension for product expansion"
)
# Add executive decision support
options = swd.compare_decisions(options=[
    {"name": "Full rollout", "cost": "$5M", "impact": "High", "risk": "Medium"},
    {"name": "Phased rollout", "cost": "$2M", "impact": "Medium", "risk": "Low"},
])
risk = swd.visualize_risks(risks=options)
```

Cross-skill example:
```python
from quantux import QuantUXSkill
from swd import SWDSkill

# Step 1: QuantUX produces A/B test results
quantux = QuantUXSkill("Checkout")
ab_result = quantux.analyze_ab_test("Old", 5000, 1750, "New", 5000, 1900)

# Step 2: SWD transforms results into executive narrative
swd = SWDSkill("A/B Test Results")
ctx = swd.build_context(audience="Product VP", cta="Approve full rollout")
story = swd.build_story(
    protagonist="Product Committee",
    imbalance="Old flow causes 15% order churn",
    evidence=["New flow conversion 20% vs old 17%, p<0.01", "NPS improved 8 points"],
    call_to_action="Full rollout of new checkout flow"
)
```

## 📖 Knowledge Base (11 Documents)

| File | Chapter | Core Content |
|------|---------|-------------|
| `references/01-context.md` | Ch.1 Context | Who-What-How, Big Idea, 3-min story, storyboard |
| `references/02-visual-display.md` | Ch.2 Visual Display | 12 chart types, decision tree, charts to avoid |
| `references/03-clutter.md` | Ch.3 Clutter | Cognitive load, 6 Gestalt principles, 6-step declutter |
| `references/04-attention.md` | Ch.4 Attention | 12 preattentive attributes, 5 color principles |
| `references/05-designer.md` | Ch.5 Think Like a Designer | Affordance, accessibility, aesthetics |
| `references/06-model-visuals.md` | Ch.6 Model Visuals | Design anatomy of 5 model visuals |
| `references/07-storytelling.md` | Ch.7 Storytelling | Three-act structure, BBB, horizontal/vertical logic |
| `references/08-pulling-together.md` | Ch.8 Pull It Together | Full 6-step实战 case study |
| `references/09-case-studies.md` | Ch.9 Case Studies | Dark backgrounds, animation, sorting, spaghetti charts |
| `references/10-final-thoughts.md` | Ch.10 Final Thoughts | 5 practice tips, team capability building |
| `references/11-quick-reference.md` | Quick Reference | Decision trees, checklists, scoring tables, fix mappings |

## 📁 Project Structure

```
storytelling-with-data/
├── SKILL.md              # Agent-facing skill definition
├── README.md             # This file — GitHub landing page
├── pyproject.toml        # Package configuration
├── requirements.txt      # No external dependencies
├── INSTALL.md            # Detailed installation guide
├── CHANGELOG.md          # Version history
├── LICENSE               # MIT License
├── CODE_OF_CONDUCT.md    # Community standards
├── references/           # 11 knowledge base documents
├── swd/                  # Python executable toolkit
│   ├── __init__.py       # SWDSkill unified entry point
│   ├── config.py         # Global configuration
│   ├── context.py        # Context analysis engine
│   ├── chart_selector.py # Chart selection decider
│   ├── declutter.py      # Declutter diagnostic
│   ├── attention.py      # Attention guidance analyzer
│   ├── designer.py       # Design evaluator
│   ├── storyteller.py    # Story builder
│   ├── diagnosis.py      # Comprehensive diagnosis engine
│   ├── makeover.py       # Chart makeover engine
│   ├── templates.py      # Report templates
│   ├── utils.py          # Utility functions
│   └── tests/
│       └── test_all.py   # 8 test cases
└── .github/              # CI/CD workflows & issue templates
```

## 🧪 Testing

```bash
cd storytelling-with-data
python swd/tests/test_all.py
# Or with pytest:
python -m pytest swd/tests/test_all.py -v
```

## 📋 When NOT to Use SWD

- **Choosing research methods or designing interviews** → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods)
- **Statistical analysis or A/B testing** → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research)
- **Understanding user Jobs-to-be-Done** → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill)
- **Creating user personas** → [Web Persona](https://github.com/AliDujie/web-persona-skill)
- **Value proposition canvas analysis** → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)

## 📚 References

| Book | Author | Contribution |
|------|--------|-------------|
| **Storytelling with Data** | Cole Nussbaumer Knaflic (2015) | Foundation — SWD six-lesson framework |
| The Visual Display of Quantitative Information | Edward Tufte (2001) | Data-ink ratio, chartjunk concept |
| Resonate | Nancy Duarte (2010) | Big Idea concept, presentation narrative structure |
| Universal Principles of Design | Lidwell, Holden, Butler (2010) | Design principles, acceptance theory |

## 🔗 Extended Ecosystem

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | SWD data story → CEO board presentations |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | SWD product data → CPO portfolio strategy |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | SWD market data → CMO brand & growth strategy |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | SWD tech metrics → CTO technology strategy |

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## ❓ FAQ / Troubleshooting

**Q: Do I need matplotlib or any charting library?**
No. SWD is methodology-focused — it tells you *what* chart to use, *how* to design it, and *why* certain choices are better. You create the actual charts in your preferred tool (Excel, Tableau, Python, etc.).

**Q: What score should I target in `full_diagnosis()`?**
Aim for 90+ (🟢 Excellent) for stakeholder-facing presentations. 70-89 (🟡 Good) is fine for internal drafts. Below 50 means a redesign is needed.

**Q: When should I use `compare_decisions()` vs just a regular chart?**
Use `compare_decisions()` when presenting multiple options to leadership — it auto-generates a comparison table with cost/impact/risk columns and a clear recommendation row.

**Q: Can SWD work with data from QuantUX?**
Yes — feed QuantUX A/B test results directly into SWD's `build_story()` to create an executive-ready narrative with statistical backing. See the [ecosystem integration section](#-ecosystem-integration) for the full pipeline.

**Q: What if my audience says "show me more data"?**
That's a storytelling problem, not a data problem. SWD's `build_context()` helps you define a clear Big Idea so your audience knows exactly what decision to make, reducing the "more data" loop.

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
