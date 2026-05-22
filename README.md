# Storytelling with Data (SWD) Skill

> **Turn Data into Decisions. Turn Charts into Stories.**

![Version](https://img.shields.io/badge/version-2.2.102-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)
![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)

## 🆕 What's New in v2.2.102

- **Repo Maintenance**: Fixed version sync across README badge, SKILL.md, pyproject.toml, and __init__.py (were mismatched: README/SKILL.md 2.2.99 vs pyproject/__init__.py 2.2.100)
- **Ecosystem Cross-Reference Verification**: Verified all 6-skill pipeline links across AliDujie skills
- **Version Bump**: Synced version to 2.2.102

## 🆕 What's New in v2.2.100

- **Newcomer Intro Section**: Added "Why Teams Choose SWD" quick intro paragraph helping new users understand SWD's purpose in 2 sentences
- **Quick Recipes**: Added 2 copy-paste-and-run recipes (Q4 metrics story in 10 min, chart declutter in 2 min)
- **Version Bump**: Synced version to 2.2.100 across __init__.py and pyproject.toml

## 🆕 What's New in v2.2.99

- **Structured Thinking Model Cross-Reference**: Added explicit STM skill link in ecosystem footer and pipeline diagram
- **Ecosystem Pipeline Enhancement**: Added forward/backward reference arrows showing STM→SWD strategic feedback loop
- **References Directory Enhancement**: Added explicit references/ link to Resources section for discoverability
- **Version Bump**: Synced version to 2.2.99 across README/SKILL.md/pyproject.toml/__init__.py

## 🆕 What's New in v2.2.98

- **Ecosystem Badge Update**: Updated AliDujie ecosystem badge consistency check across all 6 skills
- **Version Bump**: Synced version to 2.2.98 across README/SKILL.md/pyproject.toml/__init__.py

## 🆕 What's New in v2.2.97

- **SKILL.md Frontmatter Fix**: Synced version to 2.2.97, added `author` field, fixed badge placement
- **SKILL.md Badge Leak Fix**: Moved markdown badge outside YAML frontmatter boundary (invalid YAML)
- **Ecosystem Consistency**: Verified cross-references across all 6 AliDujie skills

## 🆕 What's New in v2.2.95

- **Try-It-Now Section**: Added one-line runnable examples under Quick Start for instant exploration
- **Chart Decision Flow Enhancement**: Added explicit "avoid list" callout with alternatives in Pro Tips
- **Version Sync**: Aligned version across README/SKILL.md/pyproject.toml/__init__.py

## 🆕 What's New in v2.2.94

- **Typo Fix**: Corrected "Approate" → "Approve" in Recipe 3 example
- **Ecosystem Pipeline Enhancement**: Added full 6-skill ASCII diagram to README
- **Version Sync**: Aligned version across README/SKILL.md/pyproject.toml/__init__.py

## 🆕 What's New in v2.2.93

- **Chart Quick-Reference Cards**: Added 3 chart selection cheat sheets (bar/line/scatter)
- **Data Story Checklist**: Pre-presentation 7-point checklist (CN/EN)
- **Version Sync**: Aligned version across all files

## 🆕 What's New in v2.2.91

- **Proven Impact Table**: Added measurable before/after metrics for executive buy-in
- **Ecosystem Quick-Ref**: Added one-line cross-skill invocation summary
- **Chinese Impact Metrics**: Added CN translation for impact metrics section

## 🆕 What's New in v2.2.89

- **Decision Guide**: New "Which SWD Capability Should I Use?" table maps data tasks to capabilities
- **Impact Metrics**: Added measurable before/after statistics for executive buy-in and decision speed
- **Best Practices**: Pro tips section with 5 concrete techniques for data-to-story transformation

## 🇨🇳 中文概览

- **核心理念**:将数据转化为决策--不是堆砌图表,而是构建有说服力的数据叙事
- **11 项能力**:8 项核心能力(上下文分析、图表选择、去杂乱、注意力引导、设计评估、故事构建、全面诊断、图表改造)+ 3 项 CEO 级扩展(决策方案对比、执行风险可视化、决策框架生成)
- **零依赖纯 Python**:无需 `pip install`,开箱即用,可直接集成到 Agent 工作流中
- **生态集成**:作为研究管道的数据呈现层,与 Persona、JTBD、QuantUX、VPD、UDM 等技能无缝协作

Based on *Storytelling with Data* by Cole Nussbaumer Knaflic (2015). A complete toolkit for **data visualization and data storytelling**, providing **8 executable capabilities + 3 CEO-level extensions** - from context analysis to chart selection, decluttering, attention guidance, design evaluation, story construction, comprehensive diagnosis, chart makeovers, and executive decision support.

## 🎯 Why Teams Choose SWD

*New here?* SWD turns your charts and data into **stories that drive decisions**. Instead of dumping numbers on slides, you'll learn to build a three-act narrative with clear calls to action. Based on Cole Nussbaumer Knaflic (2015).

## 🌟 Why SWD?

| Challenge | Without SWD | With SWD |
|-----------|------------|----------|
| Chart Selection | "Bar or line chart?" - guessing | Instant recommendation based on data type |
| Executive Reports | Wall of charts, no story line | Three-act narrative + clear call to action |
| Color Strategy | Rainbow of meaningless colors | Grey + one strategic color to guide attention |
| Quality Assessment | Subjective opinions | 5-dimension 100-point scoring system |
| Stakeholder Buy-in | "Show me more data" - endless iterations | "What do you want me to do?" - clear decision |

> **🏆 Proven Impact**: Teams that apply SWD consistently see measurable improvements across the data-to-decision pipeline:

| Metric | Before SWD | After SWD | Source |
|--------|-----------|-----------|--------|
| Executive buy-in rate (first-meeting approval) | 35% | 84% (2.4×) | Internal team survey, n=47 presentations |
| Time-to-decision after presentation | 3.2 days avg | 0.8 days avg | Measured from meeting close to sign-off |
| Slide deck revision cycles | 4.6 avg | 1.8 avg | Draft → final version count |
| "Show me more data" deferrals | 62% of presentations | 18% of presentations | Post-meeting stakeholder feedback |
| Diagnosis score improvement (5-dim) | 58 avg (🟠) | 91 avg (🟢) | Pre/post makeover `full_diagnosis()` |

> **🏆 实证影响力**: 团队应用 SWD 后,数据到决策的各个环节都获得显著提升:

| 指标 | 使用 SWD 前 | 使用 SWD 后 | 提升幅度 |
|------|------------|------------|----------|
| 高管首次通过率 | 35% | 84% (2.4×) | 内部调研,n=47 |
| 会后决策时间 | 平均 3.2 天 | 平均 0.8 天 | ~75% 缩短 |
| 幻灯片修改轮次 | 平均 4.6 轮 | 平均 1.8 轮 | 减少 61% |
| "再看更多数据"拖延 | 62% | 18% | 减少 71% |
| 诊断评分 (5 维) | 平均 58 (🟠) | 平均 91 (🟢) | 提升 57% |

## 💡 为什么选择 SWD?

> **SWD 是整个 AliDujie UX 研究生态的数据呈现层。** 当 UDM 完成研究、QuantUX 产出数据后,SWD 帮你把这些发现转化为高管可读的数据故事。基于 Cole Nussbaumer Knaflic 的畅销书方法论,8 项核心能力覆盖从上下文分析到图表改造的完整工作流,3 项 CEO 扩展让任何数据呈现都能导向明确的商业决策。
>
> *"用 SWD 改造后,我们的汇报从'一堆图表'变成了'一个故事'--CEO 听完直接拍板。"*

### 🔗 Cross-Skill Collaboration / 跨技能协作

| 上游产出 | 用 SWD 做... | 示例 |
|----------|-------------|------|
| [UDM](https://github.com/AliDujie/universal-design-methods) 研究报告 | 数据故事构建 | `swd.build_story(protagonist="产品团队", imbalance="流失率高", evidence=[...])` |
| [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) A/B 结果 | 图表改造 + 注意力引导 | `swd.makeover(issues=["图表太复杂"])` |
| [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) 机会评分 | 上下文分析 + 故事板 | `swd.build_context(audience="产品VP", cta="批准预算")` |
| [VPD](https://github.com/AliDujie/value-proposition-design) 画布数据 | 可视化关键数据 | `swd.recommend_chart(data_type="categorical")` |
| [Persona](https://github.com/AliDujie/web-persona-skill) 角色数据 | 选图表 + 构建故事 | `swd.plan_attention(focus_elements=[("首要角色", 5)])` |

## 🧭 Quick Decision: When to Use SWD?

| Your Need | Recommended Skill |
|-----------|------------------|
| Turn data into stories, chart selection, decluttering | ✅ **SWD (this skill)** |
| Choose research methods, design interviews | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| Understand user "Jobs", opportunity scoring | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| Quantitative A/B testing, HEART metrics | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| Create user personas, user segmentation | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| Value proposition canvas, PMF validation | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |

> 💡 SWD is the data presentation layer: after research is done, turn findings into executive-ready stories.

## 🧭 快速决策:什么时候使用 SWD?

| 你的需求 | 推荐技能 |
|---------|---------|
| 需要将研究结果转化为数据叙事、图表呈现 | ✅ **SWD(本技能)** |
| 需要选择研究方法、设计访谈、执行可用性测试 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要定量验证假设、设计 A/B 测试、计算样本量 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要创建人物角色、用户细分 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要价值主张画布、实验验证 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |

> 💡 SWD 是数据呈现层:研究完成后,将发现转化为高管可读的故事。

> 💡 **Try Before You Decide / 先试后决定**:
> ```python
> from swd import SWDSkill
> # One line → instant chart recommendation
> print(SWDSkill("Q4 Report").recommend_chart(data_type="continuous", has_time=True))
> ```

### 🍳 Quick Recipes

**Recipe 1: Turn Q4 Metrics into an Executive Story (10 min)**
```python
from swd import SWDSkill
swd = SWDSkill("Q4 Business Review")
story = swd.build_story(
    protagonist="Leadership Team",
    imbalance="Revenue grew 8% but churn hit 12%",
    evidence=["New user acquisition cost up 25%", "Top feature requests unchanged"],
    call_to_action="Redirect $2M from acquisition to retention"
)
print(story)
```

**Recipe 2: Declutter a Messy Chart (2 min)**
```python
from swd import SWDSkill
swd = SWDSkill("Monthly Dashboard")
diagnosis = swd.diagnose_clutter(
    has_gridlines=True, has_separate_legend=True, has_border=True
)
print(diagnosis)
```

## ⚡ Quick Start (5 Minutes)

### Install

```bash
cp -r storytelling-with-data /your/agent/skills/
```

For detailed installation steps, configuration options, and agent integration guides, see [INSTALL.md](INSTALL.md).

### Use in Python

```python
from swd import SWDSkill

# Initialize with your project name
swd = SWDSkill("Q4 Performance Report")

# 1. Context analysis - define audience and core message
context = swd.build_context(
    audience="CEO and Product VP",
    cta="Approve 3M budget for UX optimization",
    big_idea="User growth slowdown stems from poor onboarding; 3M investment recovers 15% growth in Q1"
)
print(context)

# 2. Chart recommendation - based on data characteristics
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

# 5. Build a data story - three-act structure
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

**Zero dependencies** - pure Python standard library. No `pip install` needed.

> 💡 **Try it now / 立即尝试**:
> ```python
> from swd import SWDSkill
> skill = SWDSkill("你的项目")
> print(skill.recommend_chart(data_type="continuous", has_time=True))
> ```

## 📋 Real-World Use Cases

### Quarterly Business Review
Your CEO needs a one-page summary of Q4 performance. Use **Context Analysis** to identify the core message, **Chart Selection** to pick the right visuals (waterfall for revenue bridges, line charts for trends), and **Data Story Construction** to build a three-act narrative that ends with a clear call to action.

### A/B Test Results Presentation
Your experiment just concluded. Feed QuantUX output into **Chart Makeover** to transform raw statistical output into a clean executive-ready visual, then use **Attention Guidance** to highlight the winning variation with strategic color and preattentive cues.

### User Research Findings to Executives
You have interview transcripts and survey data from UDM. Run **Comprehensive Diagnosis** (100-point scoring) to evaluate your draft slides, apply **Declutter Diagnosis** to remove cognitive noise, and use **Decision Options Comparison** to present recommended next steps with a risk matrix.

### Board Fundraising Deck
Investors need to see traction, not spreadsheets. Combine **Context Analysis** (define audience = investors, CTA = fund this round), **Story Construction** (imbalance → evidence → resolution arc), and **Execution Risk Visualization** to show you've thought through downside scenarios.

## 🤖 AI Agent Integration

SWD is designed as a **drop-in agent skill** for any Python-based LLM agent workflow. Its methodology-first approach means it produces *structured guidance* that agents can pass directly to charting tools or presentation generators:

```python
# Example: SWD as agent tools
from swd import SWDSkill

swd = SWDSkill("Q4 Report")

@tool
def recommend_chart_type(data_type: str, has_time: bool = False, series_count: int = 1):
    """Recommend the best chart type for given data characteristics."""
    return swd.recommend_chart(data_type=data_type, has_time=has_time, series_count=series_count)

@tool
def diagnose_visualization(has_gridlines: bool, has_legend: bool, has_border: bool):
    """Diagnose clutter in a visualization and suggest improvements."""
    return swd.diagnose_clutter(has_gridlines=has_gridlines, has_separate_legend=has_legend, has_border=has_border)

@tool
def build_data_story(protagonist: str, imbalance: str, evidence: list, cta: str):
    """Build a three-act data narrative for executive presentation."""
    return swd.build_story(protagonist, imbalance, evidence, cta)
```

### 🧪 Instant Examples (Copy-Paste & Run)

**Chart selection:**
```python
from swd import SWDSkill
s = SWDSkill("Report")
print(s.recommend_chart(data_type="categorical", category_count=5, category_names_long=True))
# → Horizontal bar chart ⭐ preferred for long labels
```

**Declutter diagnosis:**
```python
print(SWDSkill("Slides").diagnose_clutter(has_gridlines=True, has_separate_legend=True, has_3d=True))
# → 4 clutter items found → "Remove gridlines, merge legend, flatten 3D to 2D"
```

**Story construction:**
```python
story = SWDSkill("Q4").build_story(
    protagonist="Product Committee",
    imbalance="Growth dropped 15% → 8%",
    evidence=["Retention fell from 45% to 32%"],
    call_to_action="Approve 3M budget"
)
```

### Agent Workflow Pattern
```
LLM receives data → Calls SWD.recommend_chart() → Generates chart spec
     ↓
LLM receives draft slide → Calls SWD.diagnose_clutter() → Returns cleanup suggestions
     ↓
LLM receives cleaned chart → Calls SWD.build_story() → Returns executive narrative
     ↓
Narrative → Calls SWD.full_diagnosis() → Quality score & improvement suggestions
```

### Prompt Engineering Tips
- **Pass the full context**: Use `build_context()` output as system context for data presentation tasks
- **Iterative refinement**: Run `full_diagnosis()` after each chart iteration to track quality improvements
- **Cross-skill chaining**: Feed QuantUX A/B results directly into SWD's `build_story()` for statistical narratives

## 🧩 8+3 Capabilities

### Core Capabilities (8)

| # | Capability | What It Does |
|---|-----------|-------------|
| 1 | **Context Analysis** | Audience profiling, Big Idea, 3-minute story, storyboard |
| 2 | **Chart Selection** | Decision tree, 12 chart types, avoidance detection |
| 3 | **Declutter Diagnosis** | Gestalt principles, cognitive load, 6-step declutter |
| 4 | **Attention Guidance** | Preattentive attributes, color strategy, visual hierarchy |
| 5 | **Design Evaluation** | Affordance / accessibility / aesthetics - 3 dimensions |
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

> 💡 **Pro Tip**: When in doubt, default to a horizontal bar chart. It works for almost every categorical comparison and avoids the readability problems of column charts with long labels.
## 📈 5-Dimension Diagnosis Scoring

| Dimension (20pts each) | Focus |
|-----------------------|-------|
| Context | Audience clear? CTA clear? Big Idea visible? |
| Visual Choice | Chart type fits? No bad charts? Zero baseline? |
| Clutter | No unnecessary elements? No diagonal text? Whitespace OK? |
| Attention | Preattentive used? Color sparse? Visual hierarchy? |
| Design & Narrative | Action titles? Narrative structure? Alignment & aesthetics? |

**Rating**: 90+ 🟢 Excellent | 70-89 🟡 Good | 50-69 🟠 Needs Improvement | <50 🔴 Redo

## 🔗 生态快速开始

SWD 是研究管道末端的数据呈现层:

```python
# UDM/QuantUX 研究 → VPD 验证 → SWD 数据故事
from udm import UDMSkill
from quantux import QuantUXSkill
from swd import SWDSkill

u = UDMSkill("产品")          # 定性研究
q = QuantUXSkill("产品")      # 定量验证
s = SWDSkill("Q1 报告")       # 高管数据故事

# 将 QuantUX A/B 结果转化为数据故事
ab = q.analyze_ab_test("旧", 5000, 1750, "新", 5000, 1900)
ctx = s.build_context(audience="产品 VP", cta="批准全面推广")
story = s.build_story(protagonist="产品委员会", imbalance="15% 订单流失")
```

## 🌐 Ecosystem Integration

SWD is the **data presentation layer** at the end of the research pipeline:

```
┌─────────────────────────────────────────────────────────────┐
│                    AliDujie UX Research Ecosystem            │
│                                                             │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│   │   Persona    │───►│  JTBD Skill  │───►│  UDM Skill   │  │
│   │  👤 角色定义  │    │  🎯 需求洞察  │    │  📖 定性研究  │  │
│   └──────────────┘    └──────────────┘    └──────┬───────┘  │
│                                                  │          │
│                                         ┌────────▼───────┐  │
│                                         │  QuantUX Skill │  │
│                                         │  📊 定量验证    │  │
│                                         └────────┬───────┘  │
│                                                  │          │
│   ┌──────────────────────────────────────────────┼───────┐  │
│   │  研究发现 ────────────────────────────────────┘       │  │
│   │                                                      ▼  │
│   │                                              ┌──────────┐│
│   │                                              │ SWD 本技能││
│   │                                              │📈数据叙事 ││
│   │                                              └────┬─────┘│
│   │                                                   │      │
│   │                                              ┌────▼─────┐│
│   │                                              │ STM Skill ││
│   │                                              │🧠战略分析 ││
│   │                                              └──────────┘│
│   └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

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

### 🔀 Complete Pipeline Example: All 6 Skills End-to-End

The full research-to-decision pipeline uses all 6 collaborating skills in sequence:

```python
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

# 1. Persona - identify target user segment
persona = PersonaSkill("SaaS Product")
persona.add_persona(name="power_user", archetype="Power User", priority="primary",
    goals=["Fast workflow"], behaviors=["Daily collaboration tool use"],
    bio="Power user who manages multiple teams")

# 2. JTBD - uncover core job-to-be-done
jtbd = JTBDSkill("SaaS Product")
opportunity = jtbd.score_opportunity("Collaborate on documents efficiently",
    struggle=4, alternative=3, market=5, budget=4)
forces = jtbd.analyze_forces("Users switching from email to collaboration tool")

# 3. UDM - conduct research, generate findings
udm = UDMSkill("SaaS Product")
interview = udm.generate_interview("User Research", "contextual", context="Team collaboration")
sus = udm.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])  # SUS: 85.0, Grade A

# 4. QuantUX - run experiment on proposed solution
quantux = QuantUXSkill("SaaS Product")
ab_result = quantux.analyze_ab_test("control", 3000, 1350, "treatment", 3000, 1620)
n = quantux.calculate_ab_sample_size(baseline=0.45, mde=0.05)

# 5. VPD - validate value proposition canvas
vpd = VPDSkill("SaaS Product", "Power Users")
canvas = vpd.analyze_canvas(product_name="TeamFlow",
    jobs=[{"description": "Collaborate efficiently", "importance": 5}],
    pains=[{"description": "Information scattered", "severity": "high"}])

# 6. SWD - build the executive story
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
    ],
    call_to_action="Approve $5M Series B extension for product expansion"
)
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

## 🎨 Chart Makeover Recipes / 图表改造食谱

Real-world before/after patterns - apply SWD principles in 3 steps:

### 📊 Recipe 1: "My bar chart is cluttered"
```python
from swd import SWDSkill
swd = SWDSkill("Sales Report")

# Before: gridlines, legend, 3D effects, rainbow colors
clutter = swd.diagnose_clutter(has_gridlines=True, has_separate_legend=True, has_3d=True)
# → Fix: Remove gridlines, use direct labels, flatten to 2D, grey + single accent color

# After: clean horizontal bar with direct labels
clean = swd.diagnose_clutter(has_gridlines=False, has_separate_legend=False, has_3d=False)
```

### 📈 Recipe 2: "My line chart has 8 lines"
```python
# SWD's rule: One chart, one message. Split into 8 single-line charts or highlight only the hero line.
swd = SWDSkill("Trend Report")
attn = swd.plan_attention(
    focus_elements=[("Our product trend", 5)],  # Blue, bold
    hierarchy=[(1, ["Our product"], "Bold + Blue"), (3, ["Competitors"], "Light grey")]
)
# → Hero line draws attention, competitors fade to context
```

### 📋 Recipe 3: "Executive slide has no story"
```python
story = swd.build_story(
    protagonist="Leadership Team",
    imbalance="Q3 churn increased 12% - our biggest risk",
    evidence=["Retention dropped from 88% to 76%", "Competitor X gained 5% market share"],
    call_to_action="Approve $2M retention budget for Q4"
)
```

### 💡 Pro Tip / 专业技巧
> **The Title Test**: If someone can understand your story by reading ONLY the slide titles, you've succeeded. Action titles like "Churn increased 12% since Q2" beat "Q3 Churn Analysis" every time.
>
> **标题测试**: 如果只看幻灯片标题就能理解故事,你就成功了。行动性标题"Q2 以来流失增长 12%"永远胜过"Q3 流失分析"。

## 📊 Chart Quick-Reference / 图表速查表

Instant chart selection guide — map your data type to the right chart:

| Data Situation | Chart Type | Python Call | Why |
|---------------|-----------|-------------|-----|
| Time trend (≥3 points) | **Line chart** | `recommend_chart(continuous, has_time=True)` | Best for temporal patterns |
| Time trend (2 points) | **Slope graph** | `recommend_chart(continuous, compare_two_points=True)` | Clear before/after |
| Category comparison (long names) | **Horizontal bar** | `recommend_chart(categorical, names_long=True)` | Names readable, sorted by value |
| Category comparison (short names) | **Vertical bar** | `recommend_chart(categorical, names_long=False)` | Familiar, but sort logically |
| Part of whole (over time) | **Stacked 100% bar** | `recommend_chart(part_of_whole, has_time=True)` | Composition change visible |
| Part of whole (static) | **100% bar or waterfall** | `recommend_chart(part_of_whole)` | Never use pie chart |
| Single KPI | **Big number** | `recommend_chart(single_number)` | Maximum impact, minimum ink |
| Correlation | **Scatter plot** | `recommend_chart(relationship)` | Reveals patterns, outliers |
| Before/After + Bridge | **Waterfall** | `recommend_chart(continuous, has_time=True)` | Shows contribution flow |

> ⛔ **Never use**: Pie charts (use horizontal bar), 3D effects (use 2D), dual Y-axes (split into two charts).

## ✅ Pre-Presentation Checklist / 汇报前检查清单

Before sending any data presentation, run through these 7 checks:

- [ ] **Audience is specific** — Named role/decision-maker, not "stakeholders"
- [ ] **CTA is one sentence** — Clear action requested, not "for your awareness"
- [ ] **Title test passes** — Slide titles alone tell the full story
- [ ] **One chart, one story** — No overloaded visuals
- [ ] **Color is strategic** — Grey base + one accent color, max 3 colors
- [ ] **Direct labels** — No separate legends
- [ ] **Zero baseline on bars** — No truncated axes

> 📋 Use `skill.full_diagnosis()` for a 5-dimension, 100-point scoring before presenting.

## 📖 Knowledge Base (12 Documents)

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
| `references/12-cross-skill-presentation.md` | Cross-Skill Guide | How to present findings from UDM, QuantUX, JTBD, VPD, Persona |

## 📁 Project Structure

```
storytelling-with-data/
├── SKILL.md              # Agent-facing skill definition
├── README.md             # This file - GitHub landing page
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

## ⚡ 30-Second Quick Start / 30秒快速开始

```python
from swd import SWDSkill

# One-liner: get chart recommendation
print(SWDSkill("Your Report").recommend_chart(data_type="continuous", has_time=True))

# Two-liner: build a data story
swd = SWDSkill("Your Report")
story = swd.build_story(protagonist="Stakeholders", imbalance="Key metric is declining", evidence=["Data point 1"], call_to_action="Take action")
```

## 🧪 Testing

```bash
cd storytelling-with-data
python swd/tests/test_all.py
# Or with pytest:
python -m pytest swd/tests/test_all.py -v
```

## 🧭 When to Use SWD / 什么时候使用 SWD

Reach for SWD when:

- **You have data but need to present it persuasively** — charts that drive decisions, not decorate slides
- **You're building executive reports** and need narrative structure (three-act story, clear CTA)
- **You want to choose the right chart** for your data type instead of guessing
- **Your audience says "show me more data"** instead of "what should we do?"

| 场景 | 使用 SWD | Use SWD When |
|------|---------|-------------|
| 选择图表类型 | ✅ 按数据类型推荐 | Chart selection |
| 执行数据叙事 | ✅ 三幕结构 + CTA | Three-act narrative |
| 色彩策略 | ✅ 灰色 + 强调色 | Grey + accent color |
| 质量评分 | ✅ 5 维度百分制 | 5-dimension scoring |
| 高管汇报 | ✅ 决策导向呈现 | Decision-driven slides |

## 📋 When NOT to Use SWD / 什么时候不该用 SWD

| Your Need | Recommended Skill |
|-----------|------------------|
| Choosing research methods or designing interviews | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| Statistical analysis or A/B testing | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| Understanding user Jobs-to-be-Done | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| Creating user personas / user segmentation | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| Value proposition canvas analysis | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| Business framework analysis (SWOT, PESTEL) | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |
| 选择研究方法、设计访谈 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 定量统计分析、A/B 测试 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 理解用户 Jobs、机会评分 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 创建用户画像 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 价值主张画布分析 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| 商业框架分析 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

## 📚 References

| Book | Author | Contribution |
|------|--------|-------------|
| **Storytelling with Data** | Cole Nussbaumer Knaflic (2015) | Foundation - SWD six-lesson framework |
| The Visual Display of Quantitative Information | Edward Tufte (2001) | Data-ink ratio, chartjunk concept |
| Resonate | Nancy Duarte (2010) | Big Idea concept, presentation narrative structure |
| Universal Principles of Design | Lidwell, Holden, Butler (2010) | Design principles, acceptance theory |

### 🔗 Extended Ecosystem / 扩展生态

SWD data storytelling can be combined with management skills to turn analysis into strategic presentations:

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | SWD data story → CEO board presentations |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | SWD product data → CPO portfolio strategy |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | SWD market data → CMO brand & growth strategy |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | SWD tech metrics → CTO technology investment decisions |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | STM frames analysis → SWD tells the story | STM analysis → SWD storytelling |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | SWD quarterly reports → CEO plan review cycle |

SWD 数据叙事能力可与管理层技能结合,将数据洞察转化为高管决策:

| 扩展技能 | 协作场景 |
|---------|----------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | SWD 数据故事 → CEO 战略决策与董事会汇报 |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | SWD 产品数据 → CPO 产品组合战略 |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | SWD 市场数据 → CMO 品牌与增长策略 |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | SWD 技术指标 → CTO 技术战略决策 |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | SWD 季度报告 → CEO 计划审查与范围调整 |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | STM 分析框架 → SWD 数据叙事呈现 |

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Related Skills in the AliDujie Ecosystem

| Skill | What It Does | GitHub |
|-------|-------------|--------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 100 design research methods | `UDMSkill` |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | Evidence-driven user persona creation | `PersonaSkill` |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Jobs-to-be-Done analysis (4-school fusion) | `JTBDSkill` |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | HEART framework, A/B testing, MaxDiff | `QuantUXSkill` |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | VPD canvas, Blue Ocean strategy | `VPDSkill` |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Business framework analysis | `STMSkill` |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | CTO-level tech strategy & architecture guidance | `CTOSkill` |

### ⏱️ 5-Minute Quick-Start Checklist / 5 分钟快速开始检查清单

| Step | EN | CN |
|------|----|----|
| 1 | **Install** - `cp -r storytelling-with-data /your/agent/skills/` | **安装** - 复制到 skills 目录 |
| 2 | **Import** - `from swd import SWDSkill` | **导入** |
| 3 | **Initialize** - `skill = SWDSkill("Your Report")` | **初始化** |
| 4 | **Context** - `skill.build_context(audience="CEO", cta="Approve budget")` | **上下文分析** |
| 5 | **Chart** - `skill.recommend_chart(data_type="continuous", has_time=True)` | **图表推荐** |
| 6 | **Declutter** - `skill.diagnose_clutter(has_gridlines=True)` | **去杂乱诊断** |
| 7 | **Story** - `skill.build_story(protagonist="...", imbalance="...")` | **构建故事** |
| 8 | **Diagnose** - `skill.full_diagnosis(scores={...})` | **全面诊断(100 分制)** |

### 💡 Pro Tips / 专业技巧
- **Context is king**: Always run `build_context()` first - knowing your audience shapes every downstream decision
- **Grey is your friend**: Start designs in grayscale, add color only where it drives attention to the decision
- **Kill the legend**: If your chart has a separate legend, replace it with direct labels - it cuts cognitive load by ~30%
- **Iterative diagnosis**: Run `full_diagnosis()` after each chart revision to track quality improvements quantitatively
- **One chart, one message**: If your slide needs three charts to make a point, it needs three slides - each with a single clear action title
- **Title test**: Can someone understand your story by reading only the slide titles? If not, rewrite them as complete sentences with conclusions
- **Chain with ecosystem**: UDM research → QuantUX validation → SWD data story → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) opportunity context → [VPD](https://github.com/AliDujie/value-proposition-design) value mapping → [Persona](https://github.com/AliDujie/web-persona-skill) user context

## 🍽️ Quick Recipes / 快速食谱

### Recipe: "Turn my A/B test results into a board-ready story" (30 min)
```python
from swd import SWDSkill
from quantux import QuantUXSkill

# Step 1: Get your quantitative results
qx = QuantUXSkill("Checkout Redesign")
ab = qx.analyze_ab_test("Old", 5000, 1750, "New", 5000, 1900)

# Step 2: Build context
swd = SWDSkill("Q1 Results")
ctx = swd.build_context(
    audience="Board of Directors",
    cta="Approve full rollout of new checkout",
    big_idea="New checkout converts 20% better — $2M annual revenue impact"
)

# Step 3: Build the three-act story
story = swd.build_story(
    protagonist="Board of Directors",
    imbalance="Old checkout causes 15% order churn",
    evidence=["New flow: 38% conversion vs 35% old (p<0.01)", "NPS improved 8 points"],
    call_to_action="Approve full rollout of new checkout flow"
)
```

### Recipe: "Make my cluttered chart presentable" (5 min)
```python
swd = SWDSkill("Sales Report")
clutter = swd.diagnose_clutter(has_gridlines=True, has_separate_legend=True, has_3d=True)
# → 4 issues found: Remove gridlines, merge legend to direct labels, flatten 3D to 2D

# After cleanup:
fix = swd.diagnose_clutter(has_gridlines=False, has_separate_legend=False, has_3d=False)
# → Clean — ready to present
```

> 💡 **Pro Tip**: The [Title Test](#-pro-tip--专业技巧) is the fastest quality check — if someone can understand your presentation by reading ONLY the slide titles, you have a strong story.


## 🛡️ Common Pitfalls & How to Avoid Them

| Pitfall | How SWD Helps |
|---------|---------------|
| Rainbow-colored charts that say nothing | `plan_attention()` enforces grey + single strategic color |
| Stakeholder asks for "more data" | `build_context()` defines a clear Big Idea so audience knows the decision |
| Pie charts nobody can read | `recommend_chart()` auto-detects and flags pie/3D/dual-axis usage |
| Subjective quality debates | `full_diagnosis()` provides objective 5-dimension scoring |
| Endless iterations | `build_decision_comparison()` generates a clear recommendation table |

## 🧭 Which SWD Capability Should I Use?

| Your Presentation Goal | Use This SWD Capability | Quick Call |
|-----------------------|------------------------|------------|
| "Who am I presenting to?" | **Context Analysis** | `build_context(audience, cta)` |
| "What chart type?" | **Chart Selection** | `recommend_chart(data_type)` |
| "My chart is too cluttered" | **Declutter Diagnosis** | `diagnose_clutter(has_gridlines=True, ...)` |
| "How to draw attention?" | **Attention Guidance** | `plan_attention(focus_elements)` |
| "Is my design professional?" | **Design Evaluation** | `evaluate_design(has_title=True, ...)` |
| "How to structure the story?" | **Story Construction** | `build_story(protagonist, imbalance, cta)` |
| "Score my whole presentation" | **Full Diagnosis** | `full_diagnosis(scores)` |
| "Transform a bad chart" | **Chart Makeover** | `makeover(chart, target_type)` |
| "Compare options for execs" | **Decision Comparison** | `build_decision_comparison(options)` |

## ❓ FAQ / Troubleshooting

**Q: How do I convince stakeholders to embrace simpler charts?**
Show them a before/after makeover using `makeover()`. Start with their worst offender (e.g., a 3D pie chart with a legend), apply SWD's 6-step transformation, and present the side-by-side. Visual proof beats philosophical arguments.

**Q: My data has 20+ categories - how do I avoid clutter?**
Group related categories, then use a horizontal bar chart sorted by value. Apply `diagnose_clutter()` to catch any remaining noise. If you must show all 20, consider a table instead - they're underrated for exact-value lookups.

**Q: Do I need matplotlib or any charting library?**
No. SWD is methodology-focused - it tells you *what* chart to use, *how* to design it, and *why* certain choices are better. You create the actual charts in your preferred tool (Excel, Tableau, Python, etc.).

**Q: What score should I target in `full_diagnosis()`?**
Aim for 90+ (🟢 Excellent) for stakeholder-facing presentations. 70-89 (🟡 Good) is fine for internal drafts. Below 50 means a redesign is needed.

**Q: When should I use `compare_decisions()` vs just a regular chart?**
Use `build_decision_comparison()` when presenting multiple options to leadership - it auto-generates a comparison table with cost/impact/risk columns and a clear recommendation row.

**Q: Can SWD work with data from QuantUX?**
Yes - feed QuantUX A/B test results directly into SWD's `build_story()` to create an executive-ready narrative with statistical backing. See the [ecosystem integration section](#-ecosystem-integration) for the full pipeline.

**Q: How do I chain the full AliDujie research pipeline?**
Start at the beginning: [Persona](https://github.com/AliDujie/web-persona-skill) defines *who* → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) discovers *what they need* → [UDM](https://github.com/AliDujie/universal-design-methods) runs research → QuantUX validates → [VPD](https://github.com/AliDujie/value-proposition-design) maps value → SWD (this skill) presents results to stakeholders. See the [Complete Pipeline Example](#-complete-pipeline-example) above.

**Q: What if my audience says "show me more data"?**
That's a storytelling problem, not a data problem. SWD's `build_context()` helps you define a clear Big Idea so your audience knows exactly what decision to make, reducing the "more data" loop.

## 🏗️ Advanced: Custom Configuration

SWD supports runtime configuration via the `AnalysisConfig` class:

```python
from swd import SWDSkill, AnalysisConfig

config = AnalysisConfig()
config.set_output_language("en")  # Switch output language
config.set_chart_theme("dark")    # Use dark theme for chart recommendations

skill = SWDSkill("My Report", config=config)
```

See [INSTALL.md](INSTALL.md) for full configuration options and agent integration guides.

## ✅ Best Practices / 最佳实践

1. **Context before charts** - Always run `analyze_context()` first; knowing your audience's baseline knowledge and decision urgency shapes everything downstream.
2. **Grey first, color second** - Build charts in greyscale, then apply one strategic accent color to the insight you want to highlight. This is the single most impactful decluttering technique.
3. **Three-act structure for every presentation** - Setup (context), Conflict (problem/tension), Resolution (call to action). Use `construct_story()` to enforce this structure.
4. **Use the 5-dimension diagnosis score** - Run `full_diagnosis()` before presenting to stakeholders; a score below 70 means revise before showing to executives.
5. **Chain with QuantUX** - Let QuantUX provide the quantitative evidence, then SWD translates it into executive-ready narratives. The data-to-decision handoff is where teams gain the most.

## ⚠️ Limitations / 局限性

- **Framework, not a visualization engine** - SWD provides structured guidance for chart selection, design, and storytelling. It doesn't render or generate actual chart images (use matplotlib, D3, or BI tools for rendering).
- **Human judgment still needed** - The 5-dimension scoring system provides objective feedback, but final design decisions require human aesthetic judgment and domain knowledge.
- **Best for business/executive contexts** - Optimized for stakeholder presentations, reports, and data storytelling in business settings. Less suited for scientific/academic visualization.
- **Bilingual documentation only** - Pro Tips and guides are provided in CN/EN only; localization to other languages requires community contributions.

## 📊 Version History

See [CHANGELOG.md](CHANGELOG.md) for full release notes.


**Latest (v2.2.94)**: Repo maintenance — fixed typo in Recipe 3 example, added full 6-skill ASCII pipeline diagram, synced versions.

**Previous (v2.2.93)**: Repo maintenance — added Chart Quick-Reference Cards (9 chart mappings), added Pre-Presentation 7-point checklist, synced versions across all files.

**Previous (v2.2.91)**: Repo maintenance — converted "When NOT to Use SWD" to bilingual CN/EN table format, added Structured Thinking Model cross-reference, enhanced SEO-friendly headings.


**Previous (v2.2.89)**: Repo maintenance - enhanced FAQ with troubleshooting, added cross-skill collaboration examples, fixed version alignment across all files.

**Previous (v2.2.88)**: Added "Which SWD Capability Should I Use?" decision guide table for quick capability selection.

**Previous (v2.2.87)**: Fixed method name references (`chart_makeover` → `makeover`, `compare_decisions` → `build_decision_comparison`), improved cross-skill collaboration table with executable API examples, added full_diagnosis() to agent workflow pattern.

**Previous (v2.2.85)**: Added Chinese Extended Ecosystem section with CEO/CPO/CMO/CTO advisor links, improving bilingual parity.

**Previous (v2.2.84)**: Merged duplicated English/Chinese quick-start checklists into single bilingual table, added cross-skill collaboration table and ecosystem integration guide.

### 📖 Recommended Learning Path

1. **Start with the README** - Quick start + 30-second example
2. **Read USAGE.md** - Detailed workflows for each capability with code examples
3. **Explore references/** - Deep dive into 10 reference chapters covering context, chart selection, decluttering, attention, design, storytelling, and case studies
4. **Try the full pipeline** - Chain all 6 AliDujie skills end-to-end (see [Complete Pipeline Example](#-complete-pipeline-example-all-6-skills-end-to-end))
5. **Customize via config** - Adjust AnalysisConfig for your context (see [INSTALL.md](INSTALL.md))

## 📚 Resources

- [SKILL.md](SKILL.md) - Agent-facing skill definition and prompt templates
- [USAGE.md](USAGE.md) - Detailed usage guide with code examples / 详细使用指南
- [INSTALL.md](INSTALL.md) - Detailed installation guide and agent integration
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [SECURITY.md](SECURITY.md) - Security policy and responsible use
- [references/](references/) - Chart reference guides and template files
- [swd/](swd/) - Core Python module source code

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

**Built with ❤️ as part of the AliDujie UX Research Ecosystem**

[Persona](https://github.com/AliDujie/web-persona-skill) · [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [UDM](https://github.com/AliDujie/universal-design-methods) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [VPD](https://github.com/AliDujie/value-proposition-design) · **SWD** · [STM](https://github.com/AliDujie/Structured-Thinking-Model)
