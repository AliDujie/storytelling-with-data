---
name: storytelling-with-data
version: "2.2.55"
description: >
  数据可视化与数据叙事技能，基于 Cole Nussbaumer Knaflic《Storytelling with Data》
  方法论。提供 8 项可执行能力和 11 篇知识库文档，覆盖上下文分析→图表选择→去杂乱→
  注意力引导→设计评估→故事构建→综合诊断→图表改造完整工作流，以及 CEO 决策视角扩展。
---

# SWD (Storytelling with Data) Skill

数据可视化与数据叙事技能，基于 Cole Nussbaumer Knaflic《Storytelling with Data》方法论。

## 🌐 AliDujie 技能生态系统

SWD 是 **数据叙事与可视化呈现层**，在研究流程末端将各技能的发现转化为高管可读的数据故事：

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
│   │                                              └──────────┘│
│   └─────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**SWD 的典型输入**：UDM 研究报告、QuantUX 实验数据、JTBD 机会评分、VPD 画布数据、Persona 角色统计

## 🧭 快速决策：什么时候使用 SWD？

| 你的需求 | 推荐技能 |
|---------|---------|
| 需要将研究结果转化为数据叙事、图表呈现 | ✅ **SWD（本技能）** |
| 需要选择研究方法、设计访谈、执行可用性测试 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要定量验证假设、设计 A/B 测试、计算样本量 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要创建人物角色、用户细分、设计指导 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要价值主张画布、实验验证、优先级排序 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |

> 💡 SWD 是研究流程的末端：当其他技能产出数据后，用 SWD 转化为高管可读的叙事。

## 🌟 为什么选择 SWD？

- **经典方法论** — 基于 Cole Nussbaumer Knaflic《Storytelling with Data》，数据可视化领域全球畅销书
- **8+3 执行能力** — 上下文分析、图表选择、去杂乱、注意力引导、设计评估、故事构建、综合诊断、图表改造 + CEO 决策扩展
- **100 分制诊断** — 五维度综合评分，客观评估数据可视化质量，输出可操作的改进建议
- **零学习成本** — 纯 Python 标准库，无外部依赖，`from swd import SWDSkill` 即可使用
- **六步工作流** — 完整覆盖 SWD 六课：上下文→视觉选择→去杂乱→注意力→设计→叙事
- **生态末端** — 接收 UDM/QuantUX/JTBD/VPD/Persona 的研究发现，输出高管可读的数据故事

## 技能入口

主技能定义文件：[skills/swd/SKILL.md](skills/swd/SKILL.md)

## 一、核心方法论（SWD 六课）

| 课程 | 核心问题 | 关键行动 |
|------|---------|---------|
| 1. 理解上下文 | 受众是谁？需要他们做什么？ | Who-What-How → Big Idea → 故事板 |
| 2. 选择合适展示 | 什么图表最容易被受众理解？ | 决策树选图 → 避免饼图/3D/双Y轴 |
| 3. 消除杂乱 | 哪些元素不增加信息价值？ | 六步去杂乱 → 格式塔原则 |
| 4. 聚焦注意力 | 受众应该先看什么？ | 灰色基底 + 强调色 → 视觉层次 |
| 5. 像设计师思考 | 是否专业且易理解？ | 可供性 + 可访问性 + 美学 |
| 6. 讲述故事 | 数据讲了什么故事？ | 三幕结构 → 行动标题 → BBB |

**黄金法则**：探索性 ≠ 解释性（只展示珍珠不展示牡蛎）；柱状图必须零基线；颜色稀疏使用；每图必有标题和轴标题；直接标注不用图例。

## 二、8 大执行能力 + CEO 视角扩展

### 核心能力（8 大）

1. **上下文分析** — 受众画像、Big Idea、3 分钟故事、故事板
2. **图表选择推荐** — 决策树、12 种图表类型、避免检测
3. **去杂乱诊断** — 格式塔原则、认知负荷、六步去杂乱
4. **注意力引导** — 前注意属性、颜色策略、视觉层次
5. **设计评估** — 可供性 / 可访问性 / 美学三维度
6. **数据故事构建** — 三幕结构、BBB、水平逻辑
7. **可视化综合诊断** — 五维度 100 分制
8. **图表改造** — 六步法、渐进式揭示

### CEO 视角扩展（新增）

9. **决策选项对比** — 多方案对比表、推荐方案、关键假设、决策建议
10. **执行风险可视化** — 风险矩阵、风险对比表、缓解措施
11. **决策框架生成** — 决策质量检查清单、决策后追踪、决策流程图

**使用方式**：在 `build_story()` 方法中设置 `include_ceo_analysis=True` 即可自动包含 CEO 视角扩展分析。

## 三、触发条件总表

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
| CEO 决策 / 方案对比 / 投资回报 | 九：决策选项对比 | 对比表 + 推荐方案 + 关键假设 |
| 风险评估 / 风险矩阵 / 执行风险 | 十：执行风险可视化 | 风险矩阵 + 风险对比 + 缓解措施 |
| 决策框架 / 质量检查 / 决策流程 | 十一：决策框架生成 | 检查清单 + 追踪指标 + 流程图 |
| 综合数据汇报任务 | 按顺序执行一→八 | 完整数据故事 |
| CEO 级别汇报任务 | 一→八 + 九→十一 | 数据故事 + CEO 决策支持 |

## 四、目录结构

```
storytelling-with-data-skill/
├── SKILL.md                    # 本文件（顶层索引 + 工具包 + 最佳实践）
├── skills/swd/SKILL.md         # 主技能定义（8 大执行能力详细协议）
├── knowledge/                  # 11 个知识库文档
│   ├── 01-context.md           # 上下文的重要性
│   ├── 02-visual-display.md    # 选择有效的视觉展示
│   ├── 03-clutter.md           # 杂乱是你的敌人
│   ├── 04-attention.md         # 聚焦受众注意力
│   ├── 05-designer.md          # 像设计师一样思考
│   ├── 06-model-visuals.md     # 解剖模型视觉
│   ├── 07-storytelling.md      # 叙事课
│   ├── 08-pulling-together.md  # 融会贯通（六步实战案例）
│   ├── 09-case-studies.md      # 案例研究
│   ├── 10-final-thoughts.md    # 最终思考
│   └── 11-quick-reference.md   # 速查手册
├── swd/                        # Python 工具包
│   ├── __init__.py             # SWDSkill 统一入口类
│   ├── config.py               # 全局配置和常量
│   ├── context.py              # 上下文分析引擎
│   ├── chart_selector.py       # 图表选择决策器
│   ├── declutter.py            # 去杂乱诊断器
│   ├── attention.py            # 注意力引导分析器
│   ├── designer.py             # 设计评估器
│   ├── storyteller.py          # 故事构建器
│   ├── diagnosis.py            # 综合诊断引擎
│   ├── makeover.py             # 图表改造引擎
│   ├── templates.py            # 报告模板
│   ├── utils.py                # 工具函数
│   └── tests/
│       ├── __init__.py
│       └── test_all.py         # 8 个测试用例
├── README.md
├── pyproject.toml
├── requirements.txt
└── .gitignore
```

---

## 五、知识库

详细知识文档位于 `knowledge/` 目录，按书的章节组织：

| 文件 | 对应章节 | 核心内容 |
|------|---------|---------|
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

---

## 六、图表选择决策树

```
你要展示什么？
├── 1-2 个数字 → 简单文本（大字号 + 支撑文字）
├── 精确数值查找 → 表格 / 热力图
├── 两变量关系 → 散点图
├── 时间趋势
│   ├── 两个时间点 → 坡度图
│   └── 多个时间点 → 折线图
├── 分类数据
│   ├── 类别名长 / 类别 > 5 → 水平柱状图 ⭐首选
│   ├── 类别名短 → 垂直柱状图
│   └── 起点 + 增减 + 终点 → 瀑布图
├── 部分与整体 → 100% 堆叠水平柱状图
└── 永远避免
    ├── 饼图 → 替代：水平柱状图
    ├── 3D → 替代：2D 版本
    └── 双 Y 轴 → 替代：拆分 / 直接标注
```

## 七、五维度诊断评分体系

每维度 20 分，总分 100 分：

| 维度 | 评分项（每项 5 分） | 关注点 |
|------|-------------------|--------|
| 上下文 (20) | audience_clear / cta_clear / big_idea_visible / data_supports_story | 受众明确？行动号召清晰？ |
| 视觉选择 (20) | chart_type_fit / avoid_bad_charts / zero_baseline / logical_order | 图表类型合适？零基线？ |
| 杂乱 (20) | no_unnecessary_elements / no_diagonal_text / whitespace_ok / no_redundancy | 无多余元素？白空间恰当？ |
| 注意力 (20) | preattentive_used / color_sparse / visual_hierarchy / eyes_drawn_test | 颜色稀疏？眼睛测试通过？ |
| 设计叙事 (20) | text_sufficient / alignment_aesthetic / narrative_structure / action_titles | 行动标题？叙事结构？ |

**评级标准**：90+ 🟢卓越 ｜ 70-89 🟡良好 ｜ 50-69 🟠需改进 ｜ <50 🔴需重做


---

## 八、Python 可执行工具包

### 8.1 安装与依赖

纯 Python 实现，无外部依赖，仅需 Python 3.8+。

```bash
# 方式 1：直接引用项目路径
import sys; sys.path.insert(0, "/path/to/storytelling-with-data-skill")
from swd import SWDSkill

# 方式 2：复制 swd/ 和 knowledge/ 目录到你的项目
cp -r swd/ knowledge/ /your/project/

# 方式 3：作为 AI Skill 安装
cp -r skills/swd ~/.aoneclaw/skills/swd
```

**依赖清单**：

| 依赖 | 版本 | 说明 |
|------|------|------|
| Python | ≥ 3.8 | 标准库 dataclasses, pathlib, typing |
| 外部包 | 无 | 纯标准库实现 |

### 8.2 SWDSkill 统一入口类

`SWDSkill` 封装全部 8 大执行能力，每个方法返回格式化的 Markdown 报告字符串。

```python
from swd import SWDSkill

# 初始化：传入项目名称
skill = SWDSkill("Q4 季度业绩汇报")

# 可选：传入自定义配置
from swd import AnalysisConfig
config = AnalysisConfig()
skill = SWDSkill("Q4 季度业绩汇报", config=config)
```

**SWDSkill 方法一览**：

| 方法 | 能力 | 必填参数 | 返回值 |
|------|------|---------|--------|
| `build_context()` | 上下文分析 | audience, cta | Markdown 报告 |
| `recommend_chart()` | 图表选择 | data_type | Markdown 报告 |
| `diagnose_clutter()` | 去杂乱 | 至少一个 has_* 标志 | Markdown 报告 |
| `plan_attention()` | 注意力引导 | focus_elements | Markdown 报告 |
| `evaluate_design()` | 设计评估 | 至少一个检查项 | Markdown 报告 |
| `build_story()` | 故事构建 | protagonist, imbalance | Markdown 报告 |
| `full_diagnosis()` | 综合诊断 | scores 字典 | Markdown 报告 |
| `makeover()` | 图表改造 | issues 列表 | Markdown 报告 |
| `search_knowledge()` | 知识检索 | keyword | Dict[str, List[str]] |

### 8.3 八大核心模块详解

#### 模块 1：上下文分析 — `context.py`

**类**：`ContextBuilder` → `ContextAnalysis`

**使用场景**：准备数据汇报前，明确受众、目的和核心信息。

**参数说明**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| audience | str | ✅ | 主要受众（具体职位，如"产品VP"） |
| cta | str | ✅ | 行动号召（如"批准200万预算"） |
| decision_maker | str | | 最终决策者 |
| knowledge_level | str | | expert / general / novice |
| relationship | str | | first_contact / established / need_credibility |
| mechanism | str | | live_presentation / written_report / email |
| tone | str | | serious / urgent / celebratory / neutral |
| three_min_story | str | | 3 分钟故事文本 |
| big_idea | str | | Big Idea 完整句子 |
| supporting_data | List[str] | | 支撑数据列表 |
| risks | List[str] | | 风险 / 反面证据 |

**返回值**：Markdown 报告，包含受众画像表、3 分钟故事、Big Idea、支撑数据清单、风险清单、行动号召。

```python
result = skill.build_context(
    audience="产品VP", cta="批准200万预算",
    decision_maker="CTO", knowledge_level="general",
    three_min_story="用户增长在Q3放缓，需要投入新功能拉动。",
    big_idea="新用户引导体验是增长瓶颈，投入200万可在Q1恢复增长",
    supporting_data=["新用户7日留存率从45%降至32%"],
    risks=["效果可能需要2个季度显现"],
)
```

#### 模块 2：图表选择 — `chart_selector.py`

**类**：`ChartSelector` → `ChartRecommendation`

**使用场景**：选择最适合数据特征的图表类型，检测应避免的图表。

**参数说明**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| data_type | str | ✅ | categorical / continuous / relationship / single_number |
| series_count | int | | 数据系列数（默认 1） |
| category_count | int | | 类别数（默认 0） |
| has_time | bool | | 是否有时间维度 |
| show_part_of_whole | bool | | 是否展示部分与整体 |
| category_names_long | bool | | 类别名是否较长 |
| compare_two_points | bool | | 是否比较两个时间点 |
| proposed_chart | str | | 检测用户提出的图表是否应避免（pie/3d/dual_axis） |

**返回值**：Markdown 报告，包含推荐图表（含理由）、备选图表、设计要点、避免项警告。

```python
result = skill.recommend_chart(
    data_type="continuous", has_time=True,
    series_count=2, category_count=12,
    proposed_chart="pie",  # 触发饼图避免警告
)
```

#### 模块 3：去杂乱诊断 — `declutter.py`

**类**：`DeclutterAnalyzer` → `DeclutterReport`

**使用场景**：诊断图表中的杂乱元素，给出基于格式塔原则的改进建议。

**参数说明**：

| 参数 | 类型 | 说明 |
|------|------|------|
| has_border | bool | 是否有图表边框 |
| has_gridlines | bool | 是否有网格线 |
| has_3d | bool | 是否有 3D 效果 |
| has_diagonal_text | bool | 是否有对角文本 |
| has_separate_legend | bool | 是否有独立图例 |
| has_trailing_zeros | bool | 是否有尾部零（250.00） |
| has_data_markers | bool | 是否有不必要的数据标记 |
| gestalt_issues | List[Tuple] | 格式塔问题：(原则, 问题, 建议) |
| alignment_issues | List[str] | 对齐问题列表 |
| whitespace_issues | List[str] | 白空间问题列表 |

**返回值**：Markdown 报告，包含杂乱元素清单（含严重度）、去杂乱六步骤（标记已检测项）、格式塔建议、认知负荷估算。

```python
result = skill.diagnose_clutter(
    has_border=True, has_gridlines=True, has_3d=True,
    gestalt_issues=[("proximity", "标签离数据太远", "缩小间距")],
)
```

#### 模块 4：注意力引导 — `attention.py`

**类**：`AttentionAnalyzer` → `AttentionPlan`

**使用场景**：规划视觉焦点引导方案，设计颜色策略和视觉层次。

**参数说明**：

| 参数 | 类型 | 说明 |
|------|------|------|
| focus_elements | List[Tuple[str, int]] | 焦点元素：(名称, 重要性 1-5) |
| color_strategy | str | grey_plus_one / sequential / diverging |
| accent_color | str | 强调色（默认蓝色） |
| hierarchy | List[Tuple[int, List[str], str]] | 层次：(级别, 元素列表, 处理方式) |

**返回值**：Markdown 报告，包含焦点分析表、颜色方案、视觉层次设计、"眼睛看向哪里"诊断。

```python
result = skill.plan_attention(
    focus_elements=[("流失率趋势", 5), ("基准线", 2)],
    hierarchy=[(1, ["流失率趋势"], "大号+粗体+蓝色"),
               (3, ["轴标签"], "小号+浅灰")],
)
```

#### 模块 5：设计评估 — `designer.py`

**类**：`DesignEvaluator` → `DesignAssessment`

**使用场景**：从可供性、可访问性、美学三个维度评估图表设计质量。

**参数说明**：全部为 bool 类型检查项，包括 has_title / has_axis_titles / has_action_title / has_annotations / color_strategic / alignment_clean / whitespace_ok / hierarchy_clear / highlight_limited / distractions_removed。

**返回值**：Markdown 报告，包含三维度检查结果（✅/❌）、总通过率和评级、按优先级排序的改进建议。

```python
result = skill.evaluate_design(
    has_title=True, has_action_title=False,
    color_strategic=False, alignment_clean=True,
)
```

#### 模块 6：故事构建 — `storyteller.py`

**类**：`StoryBuilder` → `DataStory`

**使用场景**：构建完整的数据故事，包含三幕结构和幻灯片标题序列。

**关键参数**：protagonist（主角/受众）、imbalance（冲突）、evidence（数据证据列表）、call_to_action（行动号召）、narrative_flow（chronological / lead_with_ending）、slide_titles（标题序列）。

**返回值**：Markdown 报告，包含三幕结构、BBB、标题序列（含水平逻辑检查）。

```python
result = skill.build_story(
    protagonist="产品委员会", imbalance="用户增长率下降",
    evidence=["留存率降至32%", "竞品NPS高出20分"],
    call_to_action="批准200万优化预算",
    slide_titles=["增长率降至8%", "根因：首周留存骤降", "建议投入200万优化"],
)
```

#### 模块 7：综合诊断 — `diagnosis.py`

**类**：`DiagnosisEngine` → `DiagnosisResult`

**使用场景**：对一个数据可视化进行五维度 100 分制综合诊断。

**参数**：scores 字典，五个维度各含 4 个评分项（每项 1-5 分）。

**返回值**：Markdown 报告，包含总分 + 徽章、各维度明细表、Top 改进建议。

```python
result = skill.full_diagnosis(scores={
    "context": {"audience_clear": 4, "cta_clear": 3,
                "big_idea_visible": 2, "data_supports_story": 4},
    "visual_choice": {"chart_type_fit": 5, "avoid_bad_charts": 5,
                      "zero_baseline": 5, "logical_order": 4},
    "clutter": {"no_unnecessary_elements": 3, "no_diagonal_text": 5,
                "whitespace_ok": 4, "no_redundancy": 3},
    "attention": {"preattentive_used": 2, "color_sparse": 3,
                  "visual_hierarchy": 2, "eyes_drawn_test": 3},
    "design_narrative": {"text_sufficient": 4, "alignment_aesthetic": 4,
                         "narrative_structure": 3, "action_titles": 2},
})
```

#### 模块 8：图表改造 — `makeover.py`

**类**：`MakeoverEngine` → `MakeoverPlan`

**使用场景**：从原始问题图表到数据故事的完整改造流程。

**参数**：issues（问题列表）、chart_type / title / color_accent（设计规范）、narrative_slides（叙事幻灯片序列）。

**返回值**：Markdown 报告，包含问题诊断、六步改造方案（改造前/后/原理）、设计规范表、叙事幻灯片序列。

```python
result = skill.makeover(
    issues=["使用了饼图", "无标题", "彩虹色"],
    chart_type="水平柱状图",
    title="客户满意度最高的三个功能贡献了75%的好评",
    narrative_slides=[("整体满意度82%", "建立信任"),
                      ("功能C和D满意度偏低", "揭示问题")],
)
```

### 8.4 完整使用示例

#### 示例 1：季度业绩汇报（端到端流程）

```python
from swd import SWDSkill

skill = SWDSkill("Q4季度业绩汇报")

# Step 1: 上下文分析 — 明确受众和核心信息
ctx = skill.build_context(
    audience="CEO和产品VP",
    cta="批准Q1增长计划的300万预算",
    decision_maker="CEO",
    knowledge_level="general",
    mechanism="live_presentation",
    big_idea="用户增长放缓源于新用户引导体验不佳，投入300万优化可在Q1恢复15%月均增长",
    supporting_data=["新用户7日留存率从45%降至32%", "竞品首周体验NPS高出20分"],
)
print(ctx)

# Step 2: 选择图表 — 时间趋势用折线图
chart = skill.recommend_chart(
    data_type="continuous", has_time=True,
    series_count=3, category_count=12,
)
print(chart)

# Step 3: 去杂乱 — 诊断现有图表问题
clutter = skill.diagnose_clutter(
    has_border=True, has_gridlines=True,
    has_separate_legend=True, has_trailing_zeros=True,
)
print(clutter)

# Step 4: 注意力引导 — 突出流失率趋势
attn = skill.plan_attention(
    focus_elements=[("流失率趋势线", 5), ("行业基准", 2), ("轴标签", 1)],
    hierarchy=[
        (1, ["流失率趋势线", "关键数字"], "大号+粗体+蓝色"),
        (2, ["行业基准"], "中号+深灰+虚线"),
        (3, ["轴标签", "数据来源"], "小号+浅灰"),
    ],
)
print(attn)

# Step 5: 设计评估 — 检查改进后的图表
design = skill.evaluate_design(
    has_title=True, has_axis_titles=True, has_action_title=True,
    has_annotations=True, color_strategic=True, alignment_clean=True,
    whitespace_ok=True, hierarchy_clear=True,
)
print(design)

# Step 6: 构建故事 — 三幕结构
story = skill.build_story(
    protagonist="CEO和产品VP",
    imbalance="新用户月均增长率从15%降至8%，连续3个月下滑",
    setting="公司进入成熟期，获客成本持续上升",
    desired_balance="恢复15%月均新用户增长率",
    evidence=["首周留存率从45%降至32%", "竞品首周NPS高出20分", "A/B测试显示优化可提升留存12%"],
    call_to_action="批准300万预算用于Q1新用户引导体验优化",
    narrative_flow="lead_with_ending",
    slide_titles=[
        "建议投入300万优化新用户引导，Q1可恢复15%增长",
        "新用户增长率连续3月下降至8%",
        "根因：首周留存率从45%骤降至32%",
        "竞品首周体验NPS高出我们20分",
        "A/B测试证明优化引导可提升留存12%",
    ],
)
print(story)
```

#### 示例 2：图表改造（问题图表 → 数据故事）

```python
from swd import SWDSkill

skill = SWDSkill("客户满意度报告改造")

# Step 1: 诊断问题
diag = skill.full_diagnosis(scores={
    "context":          {"audience_clear": 2, "cta_clear": 1, "big_idea_visible": 1, "data_supports_story": 3},
    "visual_choice":    {"chart_type_fit": 1, "avoid_bad_charts": 1, "zero_baseline": 5, "logical_order": 2},
    "clutter":          {"no_unnecessary_elements": 2, "no_diagonal_text": 1, "whitespace_ok": 2, "no_redundancy": 2},
    "attention":        {"preattentive_used": 1, "color_sparse": 1, "visual_hierarchy": 1, "eyes_drawn_test": 1},
    "design_narrative": {"text_sufficient": 2, "alignment_aesthetic": 2, "narrative_structure": 1, "action_titles": 1},
})
print(diag)  # 预期：🔴 需重做

# Step 2: 执行改造
makeover = skill.makeover(
    issues=["使用了饼图展示5个类别", "无标题", "彩虹色配色", "独立图例", "对角文本标签", "居中对齐"],
    chart_type="水平柱状图",
    title="客户满意度最高的三个功能贡献了75%的好评",
    color_accent="蓝色",
    narrative_slides=[
        ("整体满意度达到82%，高于行业均值", "先展示好消息建立信任"),
        ("但功能C和D的满意度显著低于平均", "用橙色强调问题区域"),
        ("建议优先优化功能C的用户体验", "给出明确行动号召"),
    ],
)
print(makeover)

# Step 3: 搜索相关知识
kb = skill.search_knowledge("饼图")
for topic, lines in kb.items():
    print(f"\n--- {topic} ---")
    for line in lines:
        print(f"  {line}")
```

### 8.5 AI Agent 调用规则

| # | 规则 | 说明 |
|---|------|------|
| 1 | **统一入口** | 始终通过 `SWDSkill` 类调用，不直接实例化 `ContextBuilder` 等子模块 |
| 2 | **返回值** | 所有方法返回 Markdown 格式字符串，可直接展示给用户 |
| 3 | **触发映射** | 根据用户意图自动选择对应能力（参见触发条件总表） |
| 4 | **组合调用** | 综合任务按 能力一→八 顺序依次执行 |
| 5 | **知识优先** | 遇到理论问题时先调用 `search_knowledge()` 查询知识库 |
| 6 | **渐进式** | 先诊断（能力七）再改造（能力八），不要跳过诊断直接改造 |
| 7 | **上下文先行** | 任何数据可视化任务都应先执行上下文分析（能力一） |
| 8 | **验证闭环** | 改造完成后用设计评估（能力五）验证改造效果 |

### 8.6 测试说明

```bash
# 运行全部 8 个测试用例
cd storytelling-with-data-skill
python swd/tests/test_all.py

# 使用 pytest（如已安装）
python -m pytest swd/tests/test_all.py -v
```

**测试覆盖**：

| 测试用例 | 覆盖能力 | 验证内容 |
|---------|---------|---------|
| `test_build_context()` | 上下文分析 | 受众画像、Big Idea、支撑数据、风险 |
| `test_recommend_chart()` | 图表选择 | 折线图/水平柱状图/坡度图推荐、饼图避免 |
| `test_diagnose_clutter()` | 去杂乱 | 6种杂乱检测、格式塔建议、对齐/白空间 |
| `test_plan_attention()` | 注意力引导 | 焦点分析、颜色策略、视觉层次、眼睛诊断 |
| `test_evaluate_design()` | 设计评估 | 全通过→卓越、多项未通过→需改进 |
| `test_build_story()` | 故事构建 | 三幕结构、BBB、标题序列、水平逻辑 |
| `test_full_diagnosis()` | 综合诊断 | 五维度评分、总分计算、评级、改进建议 |
| `test_makeover()` | 图表改造 | 问题识别、改造步骤、设计规范、叙事幻灯片 |

### 8.7 与其他 Skill 的协作

SWD Skill 可与其他 Skill 组合使用，形成完整的数据驱动决策工作流：

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 用户研究报告可视化 | Quantitative-UX-Research | UXR 产出数据 → SWD 选图表 → SWD 构建故事 |
| 价值主张数据展示 | value-proposition-design | VPD 产出画布 → SWD 可视化关键数据 → SWD 改造图表 |
| JTBD 研究结果汇报 | jtbd-knowledge-skill | JTBD 产出分析 → SWD 上下文分析 → SWD 构建汇报故事 |
| 竞品分析数据展示 | 竞品分析 Skill | 竞品数据 → SWD 图表选择 → SWD 注意力引导 → SWD 故事构建 |
| 用户研究发现可视化 | universal-design-methods | UDM 研究发现 → SWD 图表选择 → SWD 数据故事 |
| 人物角色数据展示 | web-persona-skill | Persona 角色数据 → SWD 选图表 → SWD 构建故事 |
| 战略分析数据可视化 | structured-thinking-model | STM 分析框架 → SWD 数据可视化 → STM 决策建议 |

**协作示例（JTBD + SWD）**：

```python
# Step 1: JTBD Skill 产出用户需求分析
# jtbd_result = jtbd_skill.analyze(...)

# Step 2: SWD Skill 将分析结果可视化并构建汇报
swd = SWDSkill("JTBD研究结果汇报")

# 上下文：向产品委员会汇报JTBD研究发现
ctx = swd.build_context(
    audience="产品委员会",
    cta="基于JTBD发现调整Q2产品路线图",
    big_idea="用户核心Job是'快速完成任务'而非'探索功能'，应简化而非增加功能",
)

# 选择图表：需求优先级用水平柱状图
chart = swd.recommend_chart(
    data_type="categorical", category_count=8, category_names_long=True,
)

# 构建故事
story = swd.build_story(
    protagonist="产品委员会",
    imbalance="当前产品功能过多导致用户完成核心任务的时间增加了40%",
    evidence=["JTBD访谈发现80%用户的核心Job是快速完成任务", "功能使用率数据显示60%功能使用率<5%"],
    call_to_action="精简产品功能，聚焦核心Job",
)
```

**协作示例（QuantUX + SWD）**：

```python
# Step 1: QuantUX 产出 A/B 测试结果
# ab_result = quantux.analyze_ab_test("新结账流程", n_a=2500, conv_a=425, n_b=2500, conv_b=500)

# Step 2: SWD 将实验结果转化为高管叙事
swd = SWDSkill("A/B 测试结果汇报")
ctx = swd.build_context(audience="产品VP", cta="批准全量发布新流程")
story = swd.build_story(
    protagonist="产品委员会",
    imbalance="旧流程导致 15% 订单流失",
    evidence=["新流程转化率 20% vs 旧流程 17%, p<0.01", "NPS 提升 8 分"],
    call_to_action="全量发布新结账流程",
)
```

---

## 九、最佳实践

### 9.1 可视化设计原则

**SWD 十大设计原则**：

| # | 原则 | 说明 | 常见违反 |
|---|------|------|---------|
| 1 | 先明确受众再动手 | 不同受众需要不同的沟通方式 | 做完图表才想受众是谁 |
| 2 | 每张图只讲一个故事 | 一张图承载太多信息会失去焦点 | 在一张图中展示所有发现 |
| 3 | 使用行动标题 | 标题告诉受众"所以呢"而非"这是什么" | "销售趋势" vs "销售额Q3下降15%" |
| 4 | 颜色稀疏使用 | 颜色是最强大的工具，但必须策略性使用 | 彩虹色、每个系列不同颜色 |
| 5 | 灰色是你的朋友 | 先全灰设计，再决定哪里需要颜色 | 默认使用工具的彩色配色 |
| 6 | 直接标注数据 | 消除图例来回查看的认知负荷 | 使用独立图例 |
| 7 | 柱状图必须零基线 | 非零基线会严重扭曲数据比例 | 从50开始的Y轴 |
| 8 | 对齐创建秩序 | 元素对齐创建干净的线条和专业感 | 居中对齐、元素随意放置 |
| 9 | 白空间是战略性的 | 不要为填满空间而添加元素 | 拉伸图表填满页面 |
| 10 | 讲故事而非展示数据 | 有开始、中间、结尾和行动号召 | 把数据倒在桌上让受众自己找 |

### 9.2 常见错误与避免

| # | 常见错误 | 问题 | 正确做法 | SWD 能力 |
|---|---------|------|---------|---------|
| 1 | 使用饼图 | 人眼难以比较角度和面积 | 水平柱状图（按大小排序） | 二：图表选择 |
| 2 | 使用3D效果 | 扭曲数值，造成误导 | 对应的2D版本 | 二：图表选择 |
| 3 | 双Y轴 | 受众难以判断对应关系 | 拆分为两个图或直接标注 | 二：图表选择 |
| 4 | 彩虹色配色 | 太多颜色失去前注意价值 | 灰色基底+单一强调色 | 四：注意力 |
| 5 | 描述标题 | 受众不知道"所以呢" | 行动标题（传达结论） | 六：故事 |
| 6 | 独立图例 | 来回查看增加认知负荷 | 直接标注在数据旁 | 三：去杂乱 |
| 7 | 对角文本 | 阅读速度慢52% | 缩写标签或用水平柱状图 | 三：去杂乱 |
| 8 | 居中对齐 | 不产生干净的线条 | 左对齐 | 五：设计 |
| 9 | 无轴标题 | 受众不知道坐标含义 | 添加简洁的轴标题 | 五：设计 |
| 10 | 意面图 | 多条线重叠无法聚焦 | 逐一强调或空间分离 | 八：改造 |
| 11 | 非零基线柱状图 | 扭曲数据比例 | 柱状图必须从零开始 | 二：图表选择 |
| 12 | 展示所有数据 | 信息过载，无焦点 | 只展示支撑故事的数据 | 一：上下文 |

### 9.3 检查清单

在发布任何数据可视化之前，逐项检查：

**上下文检查**：
- [ ] 受众已明确（具体到职位/角色）
- [ ] 行动号召已明确（受众知道该做什么）
- [ ] Big Idea 可在 5 秒内识别
- [ ] 数据支撑故事（而非仅展示数据）
- [ ] 已考虑反面数据和风险

**视觉选择检查**：
- [ ] 图表类型适合数据特征
- [ ] 未使用饼图/3D/双Y轴
- [ ] 柱状图有零基线
- [ ] 数据排序有逻辑（自然顺序或数值顺序）
- [ ] 时间轴间隔一致

**杂乱检查**：
- [ ] 无图表边框
- [ ] 无或弱化网格线（浅灰细线）
- [ ] 无不必要的数据标记
- [ ] 无尾部零（250.00→250）
- [ ] 无对角文本
- [ ] 直接标注数据（无独立图例）
- [ ] 无3D效果和背景阴影

**注意力检查**：
- [ ] 使用了前注意属性引导焦点
- [ ] 颜色稀疏且有策略（灰色基底+强调色）
- [ ] 创建了清晰的视觉层次（L1/L2/L3）
- [ ] "眼睛首先看向哪里"测试通过
- [ ] 色盲友好（避免红绿同用）

**设计检查**：
- [ ] 有行动标题（而非描述标题）
- [ ] 有轴标题
- [ ] 关键数据点有注释
- [ ] 有数据来源标注
- [ ] 元素左对齐（不居中）
- [ ] 白空间恰当保留
- [ ] 字体一致且易读

**叙事检查**：
- [ ] 有开始、中间、结尾
- [ ] 有明确的行动号召
- [ ] 水平逻辑通过（只读标题能讲完整故事）
- [ ] 垂直逻辑通过（每张幻灯片内容支撑标题）
- [ ] 区分了演示版和流通版

---

## 十、参考资料

### 10.1 核心书籍

| 书名 | 作者 | 关键贡献 |
|------|------|---------|
| **Storytelling with Data** | Cole Nussbaumer Knaflic (2015) | 本 Skill 的理论基础，SWD 六课体系 |
| The Visual Display of Quantitative Information | Edward Tufte (2001) | 数据墨水比、图表垃圾概念 |
| Resonate | Nancy Duarte (2010) | Big Idea 概念、演示叙事结构 |
| Universal Principles of Design | Lidwell, Holden, Butler (2010) | 设计原则、接受度理论 |
| Beautiful Evidence | Edward Tufte (2006) | Sparklines、数据可视化美学 |
| Information Dashboard Design | Stephen Few (2006) | 仪表盘设计最佳实践 |

### 10.2 在线资源

| 资源 | 链接 | 说明 |
|------|------|------|
| storytellingwithdata.com | Cole 的官方博客 | 持续更新的案例和教程 |
| SWD Community | 社区论坛 | 实践者分享和讨论 |
| SWD Challenge | 月度挑战 | 每月一个数据可视化练习题 |
| Datawrapper Blog | datawrapper.de/blog | 实用的图表设计指南 |
| Tableau Public | public.tableau.com | 可视化灵感和案例 |

### 10.3 相关 Skill

| Skill | 仓库 | 协作方式 |
|-------|------|---------|
| JTBD Knowledge Skill | [AliDujie/jtbd-knowledge-skill](https://github.com/AliDujie/jtbd-knowledge-skill) | JTBD 研究结果 → SWD 可视化汇报 |
| Value Proposition Design | [AliDujie/value-proposition-design](https://github.com/AliDujie/value-proposition-design) | VPD 画布数据 → SWD 图表展示 |
| Quantitative UX Research | [AliDujie/Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research) | UXR 定量数据 → SWD 故事构建 |
| Universal Design Methods | [AliDujie/universal-design-methods](https://github.com/AliDujie/universal-design-methods) | UDM 研究发现 → SWD 图表选择 → SWD 数据故事 |
| Web Persona | [AliDujie/web-persona-skill](https://github.com/AliDujie/web-persona-skill) | Persona 角色数据 → SWD 选图表 → SWD 构建故事 |
| Structured Thinking Model | [AliDujie/Structured-Thinking-Model](https://github.com/AliDujie/Structured-Thinking-Model) | STM 分析框架 → SWD 数据可视化 → STM 决策建议 |

### AliDujie 技能生态

SWD 是 **AliDujie UX 研究技能生态系统** 的数据叙事与可视化呈现层，在研究流程末端将各技能的发现转化为高管可读的数据故事：

| 技能 | 定位 | 协作模式 |
|------|------|---------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 方法论核心 | UDM 研究发现 → SWD 图表选择 → SWD 数据故事 |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 需求洞察 | JTBD 洞察 → SWD 可视化汇报 |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量研究 | QuantUX 数据 → SWD 图表改造 + 叙事构建 |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | 用户角色 | Persona 数据 → SWD 选图表 → SWD 构建故事 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值验证 | VPD 产出 → SWD 数据故事 |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 战略框架 | STM 分析框架 → SWD 数据可视化 → STM 决策建议 |

### 🔗 扩展生态 (Extended Ecosystem)

SWD 数据叙事能力可与管理层技能结合，将数据洞察转化为高管决策：

| 扩展技能 | 协作场景 |
|---------|----------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | SWD 数据故事 → CEO 战略决策与董事会汇报 |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | SWD 产品数据 → CPO 产品组合战略 |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | SWD 市场数据 → CMO 品牌与增长策略 |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | SWD 技术指标 → CTO 技术战略决策 |
