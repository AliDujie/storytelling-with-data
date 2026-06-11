# Storytelling with Data (SWD) — Usage Guide

> 数据可视化与数据叙事 · 使用指南

## 📐 Where SWD Fits in the Pipeline

```
Persona (Who) → JTBD (What) → UDM (Research) → QuantUX (Validate) → VPD (Value) → SWD (Present)
                                                                                    ↑
                                                                              SWD sits here
```

- **Last in the pipeline** — takes research findings and turns them into executive-ready stories
- **Consumes** output from all upstream skills (UDM reports, QuantUX stats, VPD canvas, JTBD scores)
- **Produces** three-act narratives, chart recommendations, and decision frameworks

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
options = [
    {"name": "Optimize onboarding", "投入": "200万", "预期回报": "350万/年",
     "ROI": "75%", "风险": "中", "时间": "3个月", "可逆性": "可逆", "推荐度": "⭐⭐⭐⭐"},
    {"name": "Launch referral program", "投入": "100万", "预期回报": "280万/年",
     "ROI": "180%", "风险": "低", "时间": "2个月", "可逆性": "可逆", "推荐度": "⭐⭐⭐⭐⭐"},
]
decisions = swd.build_decision_comparison(options=options)

# Risk visualization (returns template with placeholder analysis)
risks = swd.visualize_execution_risks()

# Decision framework (returns checklist + flowchart template)
framework = swd.generate_decision_framework()
```

## 📋 Common Scenarios / 常见场景

| Scenario | Flow | APIs |
|----------|------|------|
| Quarterly business review | Context → Charts → Story | `build_context()` → `recommend_chart()` → `build_story()` |
| A/B test results presentation | QuantUX data → Makeover → Story | `makeover()` → `plan_attention()` → `build_story()` |
| Slide deck quality check | Draft slides → Diagnosis → Improvement | `full_diagnosis()` → `makeover()` |
| Board fundraising | Context → Story → Risk → Decision framework | `build_context()` → `build_story()` → `visualize_execution_risks()` |

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

## 🔧 Troubleshooting / 故障排查

| Problem / 问题 | Fix / 解决 |
|---------------|----------|
| `ModuleNotFoundError: No module named 'swd'` | Ensure the repo root is in `sys.path` or install via `pip install -e .` |
| `TypeError` on `build_context()` | Make sure `audience` and `cta` are both provided (required parameters) |
| Chart recommendation seems wrong | Double-check `data_type` — valid values: `categorical`, `continuous`, `relationship`, `single_number`, `part_of_whole` |
| Diagnosis scores don't add up | Each dimension has 4 items × 5 points = 20 max; total = 100 |
| CEO methods return generic text | `build_decision_comparison()`, `visualize_execution_risks()`, and `generate_decision_framework()` use template defaults — pass custom `options` for tailored output |

## 📚 Resources / 资源

- [README.md](README.md) — Full documentation
- [SKILL.md](SKILL.md) — Agent-facing skill definition
- [INSTALL.md](INSTALL.md) — Installation guide
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [references/](references/) — Chapter-by-chapter methodology guides
- [knowledge/](knowledge/) — Bilingual knowledge base documents

## 🏆 Best Practices / 最佳实践

1. **Start with Context / 始终从上下文开始**
   - Run `build_context()` before any chart or story work. If you can't name your audience and the decision they need to make, you're not ready to visualize.
   - 在画任何图之前先做上下文分析——叫不出受众的名字和要做的决策，就别急着做可视化。

2. **One Chart, One Message / 一图一意**
   - Each visual should communicate a single takeaway. If a chart needs a paragraph to explain, redesign it. Use action titles that state the conclusion, not the topic.
   - 每张图表只传达一个观点。如果需要一段文字来解释一张图，那就重新设计。标题应该是结论，而不是话题。

3. **Grey First, Color for Attention / 先灰度后强调色**
   - Build everything in grayscale first. Add a single strategic color only to guide the audience's eye to the key data point. Rainbow charts dilute every signal.
   - 先用灰度构建所有元素，只用一种强调色引导观众看向关键数据点。彩虹配色会稀释所有信号。

4. **Diagnose Before You Defend / 先诊断再答辩**
   - Run `full_diagnosis()` on every stakeholder-facing deck. Fix the lowest-scoring dimension first. Objective scores > subjective opinions.
   - 每次给利益相关方演示前跑一遍 `full_diagnosis()`，优先修复得分最低的维度。客观分数胜过主观意见。

5. **Kill the Legend, Use Direct Labels / 干掉图例，用直接标注**
   - A separate legend adds cognitive overhead. Replace it with direct labels on the chart itself. This single change reduces cognitive load by ~30%.
   - 单独的图例会增加认知负担。改用直接在图表上标注的方式——仅此一项改动就能降低约 30% 的认知负荷。

## 🔗 AliDujie Ecosystem Quick Reference / 生态技能速查

The full research-to-presentation pipeline:

```
Persona (Who) → JTBD (What) → UDM (Research) → QuantUX (Validate) → VPD (Value) → SWD (Present) → STM (Strategy)
```

| Upstream Skill | SWD Capability | Example |
|---------------|---------------|--------|
| [Persona](https://github.com/AliDujie/web-persona-skill) | Chart selection + story building | Role data → `recommend_chart()` → `build_story()` |
| [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | Context analysis + report story | Opportunity scores → `build_context()` → `build_story()` |
| [UDM](https://github.com/AliDujie/universal-design-methods) | Full data story pipeline | Research findings → all 8 capabilities |
| [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) | Chart makeover + attention | A/B results → `makeover()` → `plan_attention()` |
| [VPD](https://github.com/AliDujie/value-proposition-design) | Key data visualization | Canvas data → `recommend_chart()` + `build_story()` |
| [STM](https://github.com/AliDujie/Structured-Thinking-Model) | Strategic decision support | SWD output → `build_decision_comparison()` → STM analysis |
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | Board-level presentation | SWD narrative → CEO board deck |

> 💡 **Pro Tip**: Chain SWD at the end of any research pipeline. After QuantUX validates your hypothesis, feed results into `build_story()` for an executive-ready narrative.

## 🔗 Extended Ecosystem / 扩展生态

SWD data storytelling can be combined with management skills to turn analysis into strategic presentations:

| Extended Skill | Collaboration Scenario |
|---------------|------------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | SWD data story → CEO board presentations / SWD 数据故事 → CEO 董事会汇报 |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | SWD product data → CPO portfolio strategy / SWD 产品数据 → CPO 产品组合战略 |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | SWD market data → CMO brand & growth strategy / SWD 市场数据 → CMO 品牌增长策略 |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | SWD tech metrics → CTO tech investment decisions / SWD 技术指标 → CTO 技术投资决策 |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | SWD quarterly reports → CEO plan review cycle / SWD 季度报告 → CEO 计划审查 |

## ❓ FAQ / Troubleshooting

**Q: Should I start with `build_context()` or `recommend_chart()`?**
Always start with `build_context()`. Knowing your audience and core message shapes every downstream decision — chart type, color strategy, and story structure all flow from context.
*永远从 `build_context()` 开始。了解受众和核心信息决定所有后续决策。*

**Q: My slide has 10 charts — is that too many?**
Yes. Rule of thumb: one chart = one message = one slide. If you need 10 charts to make a point, you need 10 slides, each with a clear action title. Or better yet, find the one chart that tells the story.
*一个图表 = 一个信息 = 一页幻灯片。需要 10 个图表说明一个观点时，找到能讲清故事的那个。*

**Q: Can SWD generate actual charts?**
No — SWD is methodology-focused. It tells you what chart to use, how to design it, and why. You create the actual charts in Excel, Tableau, Python, etc.
*SWD 不生成实际图表——它是方法论工具，告诉你用什么图表、怎么设计、为什么。*

**Q: How does SWD chain with other skills?**
SWD is the presentation layer: all upstream skills (UDM, QuantUX, JTBD, VPD, Persona) produce findings → SWD turns them into executive-ready data stories. See ecosystem pipeline in README.md.
*SWD 是呈现层：所有上游技能的产出 → SWD 转化为高管可读的数据故事。*
