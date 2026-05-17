# Storytelling with Data (SWD) — Usage Guide

> 数据可视化与数据叙事 · 使用指南

## ⚡ 5-Minute Quick Start / 5分钟快速开始

```bash
cp -r storytelling-with-data /your/agent/skills/
python -c "from swd import SWDSkill; print(SWDSkill('Q4 Report').recommend_chart(data_type='continuous', has_time=True))"
```

## 🔑 Core Workflows / 核心工作流

### 1. Context Analysis / 上下文分析

```python
from swd import SWDSkill

swd = SWDSkill("Q4 Performance Report")

# Define audience and core message before building any chart
context = swd.build_context(
    audience="CEO and Product VP",
    cta="Approve 3M budget for UX optimization",
    big_idea="User growth slowdown stems from poor onboarding; 3M investment recovers 15% growth in Q1"
)
```

### 2. Chart Selection / 图表选择

```python
# Time trends
chart = swd.recommend_chart(data_type="continuous", has_time=True, series_count=3)
# → Line chart (multiple time points)

# Categorical comparison
chart = swd.recommend_chart(data_type="categorical", category_count=5, category_names_long=True)
# → Horizontal bar chart ⭐ preferred

# Avoid detection
chart = swd.recommend_chart(data_type="part_of_whole", proposed_chart="pie")
# → Warning: Avoid pie chart → Use 100% stacked horizontal bar
```

### 3. Declutter + Attention / 去杂乱 + 注意力引导

```python
# Diagnose clutter in your chart
clutter = swd.diagnose_clutter(
    has_border=True, has_gridlines=True, has_separate_legend=True, has_3d=True
)

# Plan visual attention hierarchy
attention = swd.plan_attention(
    focus_elements=[("Churn rate trend", 5), ("Industry benchmark", 2)],
    hierarchy=[
        (1, ["Churn rate"], "Bold + Blue"),
        (3, ["Axis labels"], "Small + Light grey")
    ]
)
```

### 4. Data Story Construction / 数据故事构建

```python
story = swd.build_story(
    protagonist="Product Committee",
    imbalance="New user growth dropped from 15% to 8% for 3 consecutive months",
    evidence=[
        "First-week retention fell from 45% to 32%",
        "Competitor NPS 20 points higher"
    ],
    call_to_action="Approve 3M budget for Q1 onboarding optimization"
)
```

### 5. Comprehensive Diagnosis / 综合诊断

```python
result = swd.full_diagnosis(scores={
    "context": {"audience_clear": 4, "cta_clear": 3, "big_idea_visible": 2, "data_supports_story": 4},
    "visual_choice": {"chart_type_fit": 5, "avoid_bad_charts": 5, "zero_baseline": 5, "logical_order": 4},
    "clutter": {"no_unnecessary_elements": 3, "no_diagonal_text": 5, "whitespace_ok": 4, "no_redundancy": 3},
    "attention": {"preattentive_used": 2, "color_sparse": 3, "visual_hierarchy": 2, "eyes_drawn_test": 3},
    "design_narrative": {"text_sufficient": 4, "alignment_aesthetic": 4, "narrative_structure": 3, "action_titles": 2},
})
# → 5-dimension 100-point score + rating + Top 3 improvement suggestions
```

### 6. CEO Extensions / CEO 视角扩展

```python
# Decision options comparison
decisions = swd.compare_decisions(
    options=["Optimize onboarding", "Launch referral program", "Improve ad targeting"],
    criteria=["Cost", "Time to impact", "Risk", "Expected ROI"]
)

# Risk visualization
risks = swd.visualize_risks(
    risks=[("Budget overrun", "high", "medium"), ("Low adoption", "medium", "high")],
    mitigations=["Phased rollout", "A/B test first"]
)

# Decision framework
framework = swd.generate_decision_framework(
    decision="Approve UX optimization budget",
    success_metrics=["Retention rate", "NPS", "Time-to-value"]
)
```

## 📋 Common Scenarios / 常见场景

| Scenario | Flow | APIs |
|----------|------|------|
| Quarterly business review | Context → Charts → Story | `build_context()` → `recommend_chart()` → `build_story()` |
| A/B test results presentation | QuantUX data → Makeover → Story | `makeover()` → `plan_attention()` → `build_story()` |
| Slide deck quality check | Draft slides → Diagnosis → Improvement | `full_diagnosis()` → `makeover()` |
| Board fundraising | Context → Story → Risk → Decision framework | `build_context()` → `build_story()` → `visualize_risks()` |

## 🔗 Ecosystem Integration / 生态协作

```python
# UDM/QuantUX research → VPD validation → SWD storytelling
from udm import UDMSkill
from quantux import QuantUXSkill
from swd import SWDSkill

# Step 1: UDM generates research findings
udm = UDMSkill("E-commerce")
report = udm.generate_report("User Research", summary="3 core pain points in checkout")

# Step 2: QuantUX provides A/B test results
quantux = QuantUXSkill("E-commerce")
ab = quantux.analyze_ab_test("Old Checkout", 5000, 1750, "New Checkout", 5000, 1900)

# Step 3: SWD turns everything into an executive story
swd = SWDSkill("Checkout Optimization Report")
ctx = swd.build_context(audience="Product VP", cta="Approve full rollout")
story = swd.build_story(protagonist="Product Committee",
    imbalance="Old checkout causes 15% order churn",
    evidence=["New flow: 20% vs old 17% conversion, p<0.01"],
    call_to_action="Full rollout of new checkout")
```

## ⛔ When NOT to Use SWD / 何时不使用

- **Research method selection** → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods)
- **Statistical analysis** → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research)
- **JTBD analysis** → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill)
- **Persona creation** → [Web Persona](https://github.com/AliDujie/web-persona-skill)
- **Value proposition canvas** → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)

## 🧪 Testing / 测试

```bash
cd storytelling-with-data
python swd/tests/test_all.py
```

## 📚 Resources / 资源

- [README.md](README.md) — Full documentation
- [SKILL.md](SKILL.md) — Agent-facing skill definition
- [INSTALL.md](INSTALL.md) — Installation guide
- [CHANGELOG.md](CHANGELOG.md) — Version history
