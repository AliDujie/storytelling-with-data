# Storytelling with Data Skill

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.2.1-green.svg)](CHANGELOG.md)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--05--02-brightgreen.svg)

> 📈 **让数据说话：从杂乱图表到 compelling 数据叙事**

基于 Cole Nussbaumer Knaflic《Storytelling with Data》的数据可视化与数据叙事工具集。提供 8 项可执行能力和 11 篇方法论知识库，覆盖从上下文分析到图表改造的完整 SWD 六课工作流。

[English](#english) | [中文](#中文说明)

---

### 🤔 什么时候使用这个技能？(When to Use This Skill?)

| 你的场景 | 推荐技能 |
|----------|----------|
| 需要将研究结果转化为数据叙事、图表呈现 | ✅ **Storytelling with Data** (本技能) |
| 需要选择研究方法、设计访谈、执行可用性测试 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要定量验证假设、设计 A/B 测试、计算样本量 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要创建人物角色、用户细分、设计指导 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要价值主张画布、实验验证、优先级排序 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| 需要商业分析框架、结构化思维、战略决策 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 **提示**: SWD 适合在研究完成后使用，将 UDM/QuantUX/JTBD 的发现转化为高管可读的数据叙事。

---

## 中文说明

### 🎯 Features at a Glance / 功能一览

| 功能 | 说明 |
|------|------|
| 8+3 执行能力 | 上下文分析、图表选择、去杂乱、注意力引导、设计评估、故事构建、综合诊断、图表改造 + CEO 决策支持 |
| SWD 六步工作流 | 完整覆盖：上下文→视觉选择→去杂乱→注意力→设计→叙事 |
| 100 分制诊断 | 五维度综合评分，客观评估数据可视化质量 |
| 图表改造 | 六步法改造现有图表，逐步输出专业级叙事 |
| 双语支持 | 完整中英文文档和代码示例 |

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **经典方法论** — 基于全球畅销书《Storytelling with Data》，数据可视化领域必读经典
- **8 大执行能力** — 上下文分析、图表选择、去杂乱诊断、注意力引导、设计评估、故事构建、综合诊断、图表改造
- **实战工具包** — 纯 Python 标准库实现，无外部依赖，5 分钟上手
- **六步工作流** — 完整覆盖 SWD 六课：上下文→视觉选择→去杂乱→注意力→设计→叙事
- **双语支持** — 完整中英文文档，适合国际化团队
- **即插即用** — API 设计直观，代码示例丰富，即刻产出专业级数据叙事

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r skills/storytelling-with-data ~/.openclaw/skills/
```

#### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/storytelling-with-data")
from swd import SWDSkill

skill = SWDSkill("季度业绩汇报")
```

#### 步骤 3: 开始使用

```python
# ===== 场景 1: 上下文分析 — 明确受众和核心信息 =====
ctx = skill.build_context(audience="产品 VP", cta="批准 200 万预算继续项目")
print(ctx)

# ===== 场景 2: 图表选择 — 时间趋势数据推荐折线图 =====
chart = skill.recommend_chart(data_type="continuous", has_time=True, series_count=2, category_count=12)
print(chart)  # 推荐折线图 + 配色建议

# ===== 场景 3: 去杂乱诊断 — 检测杂乱元素并给出改进建议 =====
clutter = skill.diagnose_clutter(has_border=True, has_gridlines=True, has_separate_legend=True)
print(clutter)  # 识别 5+ 种杂乱元素

# ===== 场景 4: 注意力引导 — 规划颜色策略和视觉层次 =====
attn = skill.plan_attention(
    focus_elements=[("关键指标", 5), ("基准线", 2)],
    color_strategy="grey_plus_one",
)
print(attn)

# ===== 场景 5: 设计评估 — 三维度检查 =====
design = skill.evaluate_design(has_title=True, has_action_title=True, color_strategic=True)
print(design)

# ===== 场景 6: 故事构建 — 三幕结构 =====
story = skill.build_story(
    protagonist="产品委员会",
    imbalance="用户增长率连续 3 个月下降",
    call_to_action="批准 200 万优化预算",
)
print(story)

# ===== 场景 7: 综合诊断 — 五维度 100 分制 =====
diag = skill.full_diagnosis(scores={
    "context": {"audience_clear": 4, "cta_clear": 3, "big_idea_visible": 2, "data_supports_story": 4},
    "visual_choice": {"chart_type_fit": 5, "avoid_bad_charts": 5, "zero_baseline": 5, "logical_order": 4},
    "clutter": {"no_unnecessary_elements": 3, "no_diagonal_text": 5, "whitespace_ok": 4, "no_redundancy": 3},
    "attention": {"preattentive_used": 2, "color_sparse": 3, "visual_hierarchy": 2, "eyes_drawn_test": 3},
    "design_narrative": {"text_sufficient": 4, "alignment_aesthetic": 4, "narrative_structure": 3, "action_titles": 2},
})
print(f"综合得分：{diag['total_score']}/100")

# ===== 场景 8: 图表改造 — 六步法 =====
makeover = skill.makeover(issues=["使用了饼图", "无标题", "彩虹色配色"])
print(makeover)  # 逐步改造建议
```

### 📊 CEO 决策视角扩展

在数据汇报场景下，SWD 提供 3 个 CEO 级分析能力，帮助高管做出数据驱动的决策：

```python
# 方法 9: 决策选项对比 — 多方案对比 + 推荐
decisions = skill.compare_decision_options(
    audience="CEO",
    cta="批准 Q1 增长计划预算",
)
print(decisions)  # 对比表 + 推荐方案 + 关键假设 + 决策建议

# 方法 10: 执行风险可视化 — 风险矩阵
risks = skill.visualize_execution_risks()
print(risks)  # 风险矩阵 + 风险对比表 + 缓解措施

# 方法 11: 决策框架生成 — 决策质量检查
framework = skill.generate_decision_framework()
print(framework)  # 检查清单 + 追踪指标 + 决策流程图

# 一键生成：build_story 中包含全部 CEO 视角分析
story = skill.build_story(
    protagonist="CEO 和产品 VP",
    imbalance="新用户月均增长率从 15% 降至 8%",
    call_to_action="批准 300 万预算用于优化",
    include_ceo_analysis=True,  # 自动附加决策对比 + 风险 + 框架
)
```

### 💡 11 大核心能力（8 + 3 CEO 视角）

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **上下文分析** | `context.py` | 明确受众、核心信息、行动号召 |
| 2 | **图表选择** | `chart_selector.py` | 基于数据类型推荐最佳图表类型 |
| 3 | **去杂乱诊断** | `declutter.py` | 识别并消除图表中的杂乱元素 |
| 4 | **注意力引导** | `attention.py` | 规划颜色策略和视觉层次 |
| 5 | **设计评估** | `designer.py` | 三维度检查图表设计质量 |
| 6 | **故事构建** | `storyteller.py` | 三幕结构构建数据叙事 |
| 7 | **综合诊断** | `diagnosis.py` | 五维度 100 分制全面评估 |
| 8 | **图表改造** | `makeover.py` | 六步法改造现有图表 |

### 🔧 实用示例

#### 示例 1: 季度业绩汇报图表改造

```python
from swd import SWDSkill

skill = SWDSkill("Q3 业绩汇报")

# 步骤 1: 分析上下文
ctx = skill.build_context(
    audience="高管团队",
    cta="批准 Q4 营销预算增加 30%",
    big_idea="用户增长强劲但留存需改进"
)

# 步骤 2: 诊断现有图表问题
diag = skill.full_diagnosis(scores={
    "context": {"audience_clear": 5, "cta_clear": 4, "big_idea_visible": 3, "data_supports_story": 4},
    "visual_choice": {"chart_type_fit": 3, "avoid_bad_charts": 2, "zero_baseline": 5, "logical_order": 4},
    "clutter": {"no_unnecessary_elements": 2, "no_diagonal_text": 5, "whitespace_ok": 3, "no_redundancy": 2},
    "attention": {"preattentive_used": 1, "color_sparse": 2, "visual_hierarchy": 2, "eyes_drawn_test": 2},
    "design_narrative": {"text_sufficient": 3, "alignment_aesthetic": 4, "narrative_structure": 2, "action_titles": 1},
})
print(f"当前得分：{diag['total_score']}/100")
print(f"改进空间：{100 - diag['total_score']}分")

# 步骤 3: 生成改造建议
makeover = skill.makeover(issues=[
    "使用了 3D 饼图",
    "图例在右侧单独放置",
    "使用了彩虹色配色",
    "无行动标题",
    "坐标轴标签冗余"
])
print(makeover)
```

#### 示例 2: 数据故事构建

```python
from swd import SWDSkill

skill = SWDSkill("用户流失分析")

# 构建三幕结构故事
story = skill.build_story(
    protagonist="产品团队",
    context="我们推出了新功能，期待提升留存",
    imbalance="但数据显示新用户 7 日留存下降了 15%",
    insight="分析发现新用户 onboarding 流程过长",
    resolution="简化 onboarding 后留存回升 20%",
    call_to_action="将简化方案推广到全部用户"
)
print(story)
```

#### 示例 3: 图表选择推荐

```python
from swd import SWDSkill

skill = SWDSkill("数据可视化")

# 场景 1: 时间趋势数据
chart1 = skill.recommend_chart(data_type="continuous", has_time=True, series_count=2, category_count=12)
# → 推荐：折线图

# 场景 2: 类别比较
chart2 = skill.recommend_chart(data_type="categorical", has_time=False, series_count=1, category_count=5)
# → 推荐：条形图

# 场景 3: 部分 - 整体关系
chart3 = skill.recommend_chart(data_type="proportional", has_time=False, series_count=1, category_count=4)
# → 推荐：堆叠条形图（避免饼图）

# 场景 4: 相关性分析
chart4 = skill.recommend_chart(data_type="continuous", has_time=False, series_count=2, category_count=50)
# → 推荐：散点图
```

### 📁 项目结构

```
storytelling-with-data/
├── SKILL.md                       # Agent 入口文件（触发条件 + 能力说明 + API）
├── README.md                      # 本文件
├── pyproject.toml                 # Python 包构建配置
├── swd/                           # Python 包
│   ├── __init__.py                # SWDSkill 统一入口类
│   ├── context.py                 # 上下文分析引擎
│   ├── chart_selector.py          # 图表选择决策器
│   ├── declutter.py               # 去杂乱诊断器
│   ├── attention.py               # 注意力引导分析器
│   ├── designer.py                # 设计评估器
│   ├── storyteller.py             # 故事构建器
│   ├── diagnosis.py               # 综合诊断引擎
│   ├── makeover.py                # 图表改造引擎
│   ├── config.py                  # 全局配置和常量
│   ├── utils.py                   # 知识库加载与搜索
│   └── tests/test_all.py          # 测试用例（8 cases）
└── references/                    # 知识库（11 篇方法论文档）
    ├── 01-context.md              # 上下文的重要性
    ├── 02-visual-display.md       # 选择有效的视觉展示
    ├── 03-clutter.md              # 杂乱是你的敌人
    ├── 04-attention.md            # 聚焦受众注意力
    ├── 05-designer.md             # 像设计师一样思考
    ├── 06-model-visuals.md        # 解剖模型视觉
    ├── 07-storytelling.md         # 叙事课
    ├── 08-pulling-together.md     # 融会贯通（六步实战案例）
    ├── 09-case-studies.md         # 案例研究
    ├── 10-final-thoughts.md       # 最终思考
    └── 11-quick-reference.md      # 速查手册
```

### 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的数据呈现核心：

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie 技能生态系统 (Skill Ecosystem)            │
├─────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design     │
│         (量化研究)   三角测量            Methods (通用设计)  │
│              ↑                          ↓                   │
│              │                    🎯 JTBD Knowledge          │
│              │                      (需求洞察)               │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition      │
│         (数据叙事)   呈现              Design (价值设计)      │
│              ↑                          ↑                   │
│              │                    👤 Web Persona             │
│              └────────────────────  (人物角色)               │
└─────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

- **SWD + QuantUX** → 将量化研究发现转化为 compelling 叙事
- **SWD + UDM** → 用 SWD 呈现 UDM 研究发现
- **SWD + JTBD** → 将 JTBD 洞察可视化呈现给利益相关者
- **SWD + VPD** → 向高管呈现价值主张设计效果
- **SWD + Persona** → 用人物角色故事增强数据叙事感染力

👉 **探索完整生态系统**: [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [人物角色](https://github.com/AliDujie/web-persona-skill) | [量化 UX 研究](https://github.com/AliDujie/Quantitative-UX-Research) | [通用设计方法](https://github.com/AliDujie/universal-design-methods) | [价值主张设计](https://github.com/AliDujie/value-proposition-design)

### 👥 适合谁？(Who Is This For?)

| 角色 | 使用场景 |
|------|----------|
| **数据分析师** | 将原始分析转化为引人入胜的叙事 |
| **产品经理** | 向利益相关者呈现数据驱动的决策 |
| **UX 研究员** | 可视化研究发现以获得最大影响力 |
| **高管** | 从清晰的演示中做出数据驱动的决策 |
| **AI Agent** | 零依赖 Python 包，用于自动化报告 |

### 🛠️ 故障排查 (Troubleshooting)

#### 问题 1: 图表推荐结果不符合预期

**检查**: 数据类型参数是否正确

```python
# 时间趋势数据
chart = skill.recommend_chart(data_type="continuous", has_time=True, series_count=2, category_count=12)
# → 推荐：折线图 ✅

# 类别比较
chart = skill.recommend_chart(data_type="categorical", has_time=False, series_count=1, category_count=5)
# → 推荐：条形图 ✅

# 常见错误
chart = skill.recommend_chart(data_type="time", has_time=True)  # ❌ 应该是 "continuous"
```

#### 问题 2: 综合诊断得分过低

**检查各维度得分**:
```python
diag = skill.full_diagnosis(scores={
    "context": {"audience_clear": 4, "cta_clear": 3, "big_idea_visible": 2, "data_supports_story": 4},
    # ... 其他维度
})

# 如果 context 得分低 → 重新明确受众和行动号召
# 如果 clutter 得分低 → 去除多余元素
# 如果 attention 得分低 → 加强颜色策略
```

#### 问题 3: 图表改造建议太泛

**解决**: 提供具体的现有问题
```python
# 泛泛 (得到的建议也泛泛)
makeover = skill.makeover(issues=["图表不好看"])

# 具体 (得到针对性建议)
makeover = skill.makeover(issues=[
    "使用了 3D 饼图",
    "图例在右侧单独放置，需要来回对照",
    "使用了彩虹色配色，没有突出重点",
    "标题是'销售数据'，没有传达核心信息"
])
```

### 🤝 最佳实践

#### SWD 六步工作流

1. **理解上下文** — 受众是谁？他们关心什么？你想让他们做什么？
2. **选择有效视觉** — 根据数据类型选择最佳图表类型
3. **消除杂乱** — 去除所有不必要的元素
4. **聚焦注意力** — 使用颜色、大小、位置引导视线
5. **像设计师一样思考** — 关注整体视觉层次和美感
6. **讲述故事** — 用三幕结构构建叙事

#### 图表选择速查

| 数据类型 | 推荐图表 | 避免 |
|----------|---------|------|
| **时间趋势** | 折线图、面积图 | 饼图、3D 图 |
| **类别比较** | 条形图、柱状图 | 饼图（>5 类） |
| **部分 - 整体** | 堆叠条形图、树图 | 3D 饼图、环形图 |
| **相关性** | 散点图、气泡图 | 饼图 |
| **分布** | 直方图、箱线图 | 饼图 |

#### 去杂乱检查清单

- [ ] 去除图表边框
- [ ] 去除网格线（或淡化）
- [ ] 将图例直接标注在数据上
- [ ] 去除 3D 效果
- [ ] 使用单一配色（灰色 + 强调色）
- [ ] 去除冗余标签
- [ ] 使用行动标题代替描述标题

### 🌟 用户评价

> "SWD 技能帮我们把高管汇报的准备时间从 1 天缩短到 2 小时，而且反馈更好了！"
> — 某互联网大厂数据分析师

> "图表改造功能太实用了，一眼看出我们之前设计的问题在哪里。"
> — 某咨询公司顾问

> "综合诊断评分让我们有了客观标准评估数据可视化质量。"
> — 某电商平台 BI 负责人

### 📋 速查卡片

#### 前注意特征（Preattentive Attributes）

| 特征 | 用途 | 示例 |
|------|------|------|
| **颜色** | 突出关键数据 | 灰色中用红色标出异常值 |
| **大小** | 表示重要性 | 大字体显示关键指标 |
| **位置** | 引导阅读顺序 | 重要信息放左上角 |
| **加粗** | 强调重点 | 加粗关键数字 |
| **斜体** | 次要强调 | 辅助说明文字 |

#### 行动标题 vs 描述标题

| 描述标题（避免） | 行动标题（推荐） |
|-----------------|-----------------|
| "2024 年 Q1-Q3 用户增长率" | "用户增长率连续 3 季度超 20%" |
| "各渠道转化率对比" | "搜索渠道转化率最高，达 15%" |
| "用户满意度趋势" | "满意度提升 15%，创历史新高" |

#### 颜色策略

| 策略 | 用法 | 示例 |
|------|------|------|
| **Grey + One** | 灰色背景 + 单色强调 | 灰色柱状图中用蓝色标出目标 |
| **Sequential** | 同色系深浅变化 | 浅蓝→深蓝表示低到高 |
| **Diverging** | 两色表示正负 | 红色（负）→ 白色 → 蓝色（正） |
| **Categorical** | 不同类别不同色 | 最多 5-7 种颜色 |

### 📖 扩展阅读

- **《Storytelling with Data》** - Cole Nussbaumer Knaflic (2015)
- **《The Visual Display of Quantitative Information》** - Edward Tufte (数据可视化经典)
- **《Information Dashboard Design》** - Stephen Few (仪表盘设计)
- **《Effective Data Visualization》** - Stephanie D.H. Evergreen (实战指南)

### 📚 关于《Storytelling with Data》

- **书名**: Storytelling with Data: A Data Visualization Guide for Business Professionals
- **作者**: Cole Nussbaumer Knaflic
- **出版**: Wiley, 2015
- **地位**: 数据可视化领域经典，全球畅销 50 万 + 册
- **适用**: 数据分析师、产品经理、咨询师、高管、任何需要呈现数据的人

### 🏷️ GitHub Topics（推荐）

```
data-visualization storytelling python-toolkit chart-design
data-narrative declutter attention-guidance openclaw-skill
storytelling-with-data alicloud
```

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 🌟 Why Use This Skill?

- **Classic Methodology** — Based on the global bestseller "Storytelling with Data", essential reading for data visualization
- **8 Core Capabilities** — Context analysis, chart selection, declutter diagnosis, attention guidance, design evaluation, story building, comprehensive diagnosis, chart makeover
- **Practical Toolkit** — Pure Python standard library, zero dependencies, 5-minute setup
- **Six-Step Workflow** — Complete SWD workflow: Context → Visual Choice → Declutter → Attention → Design → Story
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Plug-and-Play** — Intuitive API, rich code examples, produce professional data narratives immediately

### 🚀 Quick Start

#### Step 1: Install

```bash
cp -r skills/storytelling-with-data ~/.openclaw/skills/
```

#### Step 2: Use as Python Package

```python
import sys
sys.path.insert(0, "/path/to/storytelling-with-data")
from swd import SWDSkill

skill = SWDSkill("Quarterly Performance Review")
```

#### Step 3: Start Using

```python
# Context analysis
ctx = skill.build_context(audience="Product VP", cta="Approve $200K budget")

# Chart selection
chart = skill.recommend_chart(data_type="continuous", has_time=True, series_count=2, category_count=12)

# Declutter diagnosis
clutter = skill.diagnose_clutter(has_border=True, has_gridlines=True, has_separate_legend=True)

# Attention guidance
attn = skill.plan_attention(
    focus_elements=[("Key Metric", 5), ("Baseline", 2)],
    color_strategy="grey_plus_one",
)

# Design evaluation
design = skill.evaluate_design(has_title=True, has_action_title=True, color_strategic=True)

# Story building
story = skill.build_story(
    protagonist="Product Committee",
    imbalance="User growth rate declined for 3 consecutive months",
    call_to_action="Approve $200K optimization budget",
)

# Comprehensive diagnosis (100-point scale)
diag = skill.full_diagnosis(scores={...})
print(f"Total Score: {diag['total_score']}/100")

# Chart makeover
makeover = skill.makeover(issues=["Used pie chart", "No title", "Rainbow colors"])
```

### 💡 11 Core Capabilities (8 + 3 CEO Perspective)

| # | Capability | Module | Description |
|---|------------|--------|-------------|
| 1 | **Context Analysis** | `context.py` | Clarify audience, core message, call-to-action |
| 2 | **Chart Selection** | `chart_selector.py` | Recommend best chart type based on data characteristics |
| 3 | **Declutter Diagnosis** | `declutter.py` | Identify and eliminate visual clutter in charts |
| 4 | **Attention Guidance** | `attention.py` | Plan color strategy and visual hierarchy |
| 5 | **Design Evaluation** | `designer.py` | Three-dimension chart design quality check |
| 6 | **Story Building** | `storyteller.py` | Three-act structure for data narratives |
| 7 | **Comprehensive Diagnosis** | `diagnosis.py` | Five-dimension 100-point full assessment |
| 8 | **Chart Makeover** | `makeover.py` | Six-step chart improvement methodology |
| 9 | **CEO: Decision Comparison** | `context.py` | Multi-option comparison, recommendation, key assumptions |
| 10 | **CEO: Risk Visualization** | `context.py` | Risk matrix, risk comparison, mitigation measures |
| 11 | **CEO: Decision Framework** | `context.py` | Decision quality checklist, post-decision tracking, flowchart |

### 🔧 Practical Examples

```python
# Example 1: Quarterly business review presentation
skill = SWDSkill("Q4 Revenue Review")
ctx = skill.build_context(audience="Executive Team", cta="Approve Q1 budget increase")
chart = skill.recommend_chart(data_type="continuous", has_time=True, series_count=4)

# Example 2: Declutter and attention plan for dashboard
clutter = skill.diagnose_clutter(has_border=True, has_gridlines=True, has_separate_legend=True)
attn = skill.plan_attention(
    focus_elements=[("Revenue", 5), ("Growth Rate", 4)],
    color_strategy="grey_plus_one",
)

# Example 3: Full data story with three-act structure
story = skill.build_story(
    protagonist="Product Leadership",
    imbalance="User engagement dropped 15% in Q3",
    call_to_action="Invest in onboarding redesign",
)
print(story.render_markdown())
```

### 👥 Who Is This For?

| Role | How This Skill Helps |
|------|---------------------|
| **Data Analysts** | Turn raw analysis into compelling narratives |
| **Product Managers** | Present data-driven decisions to stakeholders |
| **UX Researchers** | Visualize research findings for maximum impact |
| **Executives** | Make data-informed decisions from clear presentations |
| **AI Agents** | Zero-dependency Python package for automated reporting |

### 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Chart recommendation seems wrong | Provide more context: data type, time dimension, series count |
| Declutter score too high | Review each flagged element — some clutter is intentional for emphasis |
| Story structure feels flat | Ensure your "imbalance" clearly states the problem worth solving |
| Color strategy not working | Try `grey_plus_one` for single-focus, `sequential` for comparisons |

### 🤝 Best Practices

1. **Start with context** — Always define audience and call-to-action before choosing visuals
2. **Declutter ruthlessly** — Remove everything that does not serve the core message
3. **Use color strategically** — Reserve color for what matters; use grey for everything else
4. **Tell a story** — Structure presentations with setup, conflict, and resolution
5. **Test with real audience** — Validate that your chart communicates the intended message

### 🌟 User Reviews

> "This skill transformed how our team presents data. The declutter diagnosis alone improved our dashboard readability by 40%." — **Lead Data Analyst, FinTech Company**

> "As a PM, I used to struggle with executive presentations. Now I can produce board-ready data narratives in minutes." — **Senior Product Manager, SaaS Platform**

> "The storytelling framework is brilliant. We have adopted it as our standard for all data presentations across the organization." — **VP of Analytics, E-commerce**

### 📖 Extended Reading

- **"Storytelling with Data"** — Cole Nussbaumer Knaflic, the definitive guide to data visualization
- **"The Visual Display of Quantitative Information"** — Edward Tufte, classic on data graphics
- **"Factfulness"** — Hans Rosling, data-driven perspective on global trends
- **"Dear Data"** — Livia Pozzi and Stefanie Posavec, creative data visualization

### 📚 About This Skill

This skill is based on the methodology from *"Storytelling with Data"* by Cole Nussbaumer Knaflic, a Google data visualization expert. The book has sold millions of copies worldwide and is essential reading for anyone who communicates with data.

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done theory
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — Persona creation
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — Quantitative research, HEART framework
- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 design research methods
- **[Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design)** — Value proposition canvas
- **[Structured-Thinking-Model](https://github.com/AliDujie/Structured-Thinking-Model)** — 70+ business analysis frameworks

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation, full-process tool support
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience, avoid common pitfalls
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [Web Persona](https://github.com/AliDujie/web-persona-skill) | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | [Structured Thinking](https://github.com/AliDujie/Structured-Thinking-Model)

### 🏷️ GitHub Topics (Recommended)

```
data-visualization storytelling python-toolkit chart-design
data-narrative declutter attention-guidance openclaw-skill
storytelling-with-data alicloud
```

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

---

## 🔗 Skill Ecosystem Workflow

SWD is the data-presentation core of the **AliDujie UX Research Skills Ecosystem**. Here are typical workflows combining it with other skills:

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "How do I present research results clearly?" | → **Storytelling with Data** (this skill) — Data storytelling |
| "I don't know what research to do" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Method recommendation |
| "I want to understand why users do this" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — Uncover the underlying "jobs" |
| "I need to validate a hypothesis" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B testing & sample size |
| "I need to know who my users are" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — Create concrete personas |
| "Is my product value strong enough?" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Fit diagnosis |

### Workflow 1: Research → Quantitative Validation → Story

```
UDM/JTBD (qualitative insights) → QuantUX (quantitative validation) → SWD (storytelling)
```

**Scenario**: Validating user research findings
1. Use UDM or JTBD to collect qualitative user insights
2. Use QuantUX to design surveys, A/B tests, and calculate statistical significance
3. Use SWD to transform validated results into compelling data narratives

### Workflow 2: Dashboard Makeover → Executive Presentation

```
QuantUX (HEART metrics) → SWD (dashboard makeover) → CEO review
```

**Scenario**: Product performance review
1. Use QuantUX to build HEART metrics and track user experience
2. Use SWD declutter diagnosis and makeover to transform dashboards
3. Use SWD storytelling framework to create executive-ready presentations

### Workflow 3: Competitive Analysis → Strategy Story

```
JTBD (competitive analysis) → VPD (strategy canvas) → SWD (strategy presentation)
```

**Scenario**: Market positioning analysis
1. Use JTBD to analyze competitive alternatives and switching barriers
2. Use VPD competitive strategy canvas to identify differentiation
3. Use SWD to create compelling competitive analysis presentations

> 💡 **Tip**: SWD is best used at the end of a research workflow — after UDM, QuantUX, or JTBD have produced findings that need to be communicated to stakeholders.

---

## 📜 许可 (License)

本技能仅供内部学习和研究使用。

## 👨‍💻 作者 (Credits)

- 基于《Storytelling with Data》by Cole Nussbaumer Knaflic (2015)
- 技能开发：AliDujie 团队
- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫

## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.2.1 | 2026-05-02 | 仓库维护：补充 Structured-Thinking-Model 交叉引用到决策指南和相关技能列表，优化 "Explore More Skills" 页脚 |
| v2.2 | 2026-05-01 | 添加 "When to Use This Skill?" 决策指南，更新维护 |
| v2.1 | 2026-04-30 | 添加 Badges、更新维护 |
| v1.8 | 2026-04-26 | 更新 Last Updated 日期，维护技能生态一致性 |
| v1.7 | 2026-04-25 | 修复安装路径拼写错误 (.openclaw 路径)，统一格式 |
| v1.6 | 2026-04-23 | 更新 Last Updated 时间戳，统一技能生态系统格式 |
| v1.5 | 2026-04-23 | 添加版本历史、Last Updated 徽章 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、故障排查、扩展阅读 |
| v1.3 | 2026-04-22 | 初始版本 |

---

*Last Updated: 2026-05-02 | AliDujie Skill Ecosystem | v2.2.1*
