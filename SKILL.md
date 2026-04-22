---
name: storytelling-with-data
description: >
  数据可视化与数据叙事工具集。基于 Cole Nussbaumer Knaflic《Storytelling with Data》方法论，
  提供 8 项可执行能力（上下文分析、图表选择、去杂乱诊断、注意力引导、设计评估、故事构建、
  综合诊断、图表改造）和 11 篇方法论知识库。附带完整 Python API（SWDSkill 统一入口），
  覆盖 SWD 六课体系，支持从数据到故事的全流程结构化输出。
---

# SWD (Storytelling with Data) 执行技能

基于 Cole Nussbaumer Knaflic《Storytelling with Data》的数据可视化方法论。本 Skill 具备 8 项直接执行能力，可以分析上下文、推荐图表、诊断杂乱、规划注意力、评估设计、构建故事、综合诊断和改造图表。

## 核心方法论（SWD 六课）

1. **理解上下文** — Who-What-How → Big Idea → 故事板
2. **选择合适展示** — 决策树选图表；避免饼图/3D/双Y轴
3. **消除杂乱** — 格式塔原则 + 去杂乱六步骤
4. **聚焦注意力** — 灰色基底 + 单一强调色 + 视觉层次
5. **像设计师思考** — 可供性 + 可访问性 + 美学
6. **讲述故事** — 三幕结构 + 行动标题 + Bing-Bang-Bongo

**黄金法则**：探索性 ≠ 解释性（只展示珍珠不展示牡蛎）；柱状图必须零基线；颜色稀疏使用；每图必有标题和轴标题；直接标注不用图例。

## 触发条件

| 触发词 / 场景 | 执行能力 | 输出物 |
|---|---|---|
| 做汇报 / 给谁看 / 受众 / Big Idea | 一：上下文分析 | 受众画像表、Big Idea、故事板 |
| 用什么图 / 选图表 / 怎么展示数据 | 二：图表选择 | 推荐图表 + 设计要点 + 避免项 |
| 图太乱 / 太复杂 / 简化 / 去杂乱 | 三：去杂乱诊断 | 杂乱清单 + 六步骤 + 格式塔建议 |
| 突出重点 / 颜色怎么用 / 注意力 | 四：注意力引导 | 焦点分析 + 颜色方案 + 层次设计 |
| 好不好看 / 专不专业 / 设计评估 | 五：设计评估 | 三维度检查 + 通过率 + 改进建议 |
| 怎么讲故事 / 叙事结构 / 汇报结构 | 六：故事构建 | 三幕结构 + BBB + 标题序列 |
| 帮我看看这个图 / 诊断 / 评分 | 七：综合诊断 | 五维度总分 + 各维度明细 + Top 3 建议 |
| 改造 / 优化 / 改进 / makeover | 八：图表改造 | 六步方案 + 设计规范 + 叙事幻灯片 |
| 综合数据汇报任务 | 按顺序执行一→八 | 完整数据故事 |

## 执行能力概览

**能力一：上下文分析** — 收集主题、受众角色、目的后，输出受众画像表、3 分钟故事、Big Idea（独特观点+利害关系+完整句子）、支撑数据清单、风险清单、行动号召和故事板。详见 `references/01-context.md`。

**能力二：图表选择推荐** — 基于数据类型、系列数、类别数等特征，通过决策树推荐 12 种图表类型中的最佳选项。永远避免饼图→水平柱状图、3D→2D、双Y轴→拆分。详见 `references/02-visual-display.md`。

**能力三：去杂乱诊断** — 自动检测 8 种杂乱元素（边框/网格线/数据标记/尾部零/对角文本/独立图例/3D/背景阴影），应用格式塔六原则，输出去杂乱六步骤和认知负荷估算。详见 `references/03-clutter.md`。

**能力四：注意力引导** — 识别焦点元素、设计颜色策略（灰色基底+强调色）、规划三层视觉层次（L1 标题/L2 数据/L3 标签），执行"眼睛首先看向哪里"诊断。详见 `references/04-attention.md`。

**能力五：设计评估** — 从可供性（重要内容突出？）、可访问性（有标题？有轴标题？）、美学（颜色有策略？对齐干净？）三维度评估，输出 ✅/❌ 检查结果和改进建议。详见 `references/05-designer.md`。

**能力六：数据故事构建** — 三幕结构（开始：背景+冲突 → 中间：证据+方案 → 结尾：行动号召）、Bing-Bang-Bongo、水平逻辑检查（只读标题应能讲完整故事）、叙事流选择（时间顺序/结论先行）。详见 `references/07-storytelling.md`。

**能力七：综合诊断** — 五维度 100 分制（上下文/视觉选择/杂乱/注意力/设计叙事，每维度 20 分，每项 5 分）。90+ 卓越、70-89 良好、50-69 需改进、<50 需重做。输出总分、各维度明细和 Top 3 改进建议。

**能力八：图表改造** — 六步法（上下文→选择→去杂乱→注意力→设计→故事），自动修复映射（饼图→水平柱状图、3D→2D、彩虹色→灰+单色、图例→直接标注），输出改造步骤、设计规范和叙事幻灯片序列。详见 `references/08-pulling-together.md`。

## 图表选择决策树

```
你要展示什么？
├── 1-2 个数字 → 简单文本（大字号 + 支撑文字）
├── 精确数值查找 → 表格 / 热力图
├── 两变量关系 → 散点图
├── 时间趋势
│   ├── 两个时间点 → 坡度图
│   └── 多个时间点 → 折线图
├── 分类数据
│   ├── 类别名长 / 类别 > 5 → 水平柱状图（首选）
│   ├── 类别名短 → 垂直柱状图
│   └── 起点 + 增减 + 终点 → 瀑布图
├── 部分与整体 → 100% 堆叠水平柱状图
└── 永远避免：饼图 / 3D / 双 Y 轴
```

## Python 工具包

位于 `swd/` 目录，纯标准库实现，无外部依赖。

| 模块 | 核心类 | 用途 |
|---|---|---|
| `__init__.py` | `SWDSkill` | 统一入口类，封装全部 8 大能力 |
| `context.py` | `ContextBuilder` | 上下文分析：受众画像、Big Idea |
| `chart_selector.py` | `ChartSelector` | 图表选择：决策树 + 避免检测 |
| `declutter.py` | `DeclutterAnalyzer` | 去杂乱：auto_detect + 格式塔 |
| `attention.py` | `AttentionAnalyzer` | 注意力：颜色策略 + 眼睛诊断 |
| `designer.py` | `DesignEvaluator` | 设计评估：三维度 auto_evaluate |
| `storyteller.py` | `StoryBuilder` | 故事构建：三幕 + BBB + 水平逻辑 |
| `diagnosis.py` | `DiagnosisEngine` | 综合诊断：五维度 100 分制 |
| `makeover.py` | `MakeoverEngine` | 图表改造：六步法 + 渐进式揭示 |
| `config.py` | `AnalysisConfig` | 全局配置和常量 |
| `utils.py` | `load_knowledge`, `search_knowledge` | 知识库加载与搜索 |

### 快速使用

```python
import sys
sys.path.insert(0, "/path/to/storytelling-with-data")
from swd import SWDSkill

skill = SWDSkill("季度业绩汇报")

# 上下文分析
ctx = skill.build_context(audience="产品VP", cta="批准200万预算")

# 图表选择
chart = skill.recommend_chart(data_type="continuous", has_time=True, series_count=2)

# 去杂乱
clutter = skill.diagnose_clutter(has_border=True, has_gridlines=True, has_3d=True)

# 注意力引导
attn = skill.plan_attention(focus_elements=[("关键指标", 5)], color_strategy="grey_plus_one")

# 设计评估
design = skill.evaluate_design(has_title=True, has_action_title=False, color_strategic=False)

# 故事构建
story = skill.build_story(protagonist="产品委员会", imbalance="用户增长率下降")

# 综合诊断
diag = skill.full_diagnosis(scores={"context": {"audience_clear": 4, "cta_clear": 3, "big_idea_visible": 2, "data_supports_story": 4}})

# 图表改造
makeover = skill.makeover(issues=["使用了饼图", "无标题", "彩虹色"])

# 知识库搜索
results = skill.search_knowledge("格式塔")
```

## 知识库索引

所有文档位于 `references/` 目录：

| 文件 | 对应章节 | 核心内容 |
|---|---|---|
| `01-context.md` | Ch.1 上下文 | Who-What-How、Big Idea、3 分钟故事、故事板 |
| `02-visual-display.md` | Ch.2 选择展示 | 12 种图表类型、决策树、避免的图表 |
| `03-clutter.md` | Ch.3 杂乱 | 认知负荷、格式塔 6 原则、去杂乱六步骤 |
| `04-attention.md` | Ch.4 注意力 | 12 种前注意属性、颜色五原则、渐进式揭示 |
| `05-designer.md` | Ch.5 设计师 | 可供性、可访问性、美学、接受度 |
| `06-model-visuals.md` | Ch.6 模型视觉 | 5 个模型视觉的设计解剖 |
| `07-storytelling.md` | Ch.7 叙事 | 三幕结构、BBB、水平 / 垂直逻辑 |
| `08-pulling-together.md` | Ch.8 融会贯通 | 六步法完整实战案例 |
| `09-case-studies.md` | Ch.9 案例 | 深色背景、动画、排序、意面图、饼图替代 |
| `10-final-thoughts.md` | Ch.10 最终思考 | 5 个实践建议、团队能力建设 |
| `11-quick-reference.md` | 速查手册 | 决策树、检查清单、评分表、问题修复映射 |
