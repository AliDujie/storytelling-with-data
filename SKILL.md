---
name: storytelling-with-data
description: 数据可视化与数据叙事技能，基于《Storytelling with Data》方法论。提供上下文分析、图表选择、去杂乱、注意力引导、设计评估、故事构建、综合诊断、图表改造八大能力，含 Python 可执行工具包。
---

# SWD (Storytelling with Data) Skill

数据可视化与数据叙事技能，基于 Cole Nussbaumer Knaflic《Storytelling with Data》方法论。

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

## 二、8 大执行能力

1. **上下文分析** — 受众画像、Big Idea、3 分钟故事、故事板
2. **图表选择推荐** — 决策树、12 种图表类型、避免检测
3. **去杂乱诊断** — 格式塔原则、认知负荷、六步去杂乱
4. **注意力引导** — 前注意属性、颜色策略、视觉层次
5. **设计评估** — 可供性 / 可访问性 / 美学三维度
6. **数据故事构建** — 三幕结构、BBB、水平逻辑
7. **可视化综合诊断** — 五维度 100 分制
8. **图表改造** — 六步法、渐进式揭示

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
| 综合数据汇报任务 | 按顺序执行一→八 | 完整数据故事 |

## 四、目录结构

```
storytelling-with-data/
├── SKILL.md              # 本文件（顶层索引 + 工具包 + Agent 规则）
├── references/            # 11 个知识库文档 (01-context ~ 11-quick-reference)
├── swd/                   # Python 工具包
│   ├── __init__.py        # SWDSkill 统一入口类
│   ├── config.py          # 全局配置和常量
│   ├── context.py         # 上下文分析引擎
│   ├── chart_selector.py  # 图表选择决策器
│   ├── declutter.py       # 去杂乱诊断器
│   ├── attention.py       # 注意力引导分析器
│   ├── designer.py        # 设计评估器
│   ├── storyteller.py     # 故事构建器
│   ├── diagnosis.py       # 综合诊断引擎
│   ├── makeover.py        # 图表改造引擎
│   ├── utils.py           # 工具函数
│   └── tests/test_all.py  # 8 个测试用例
├── README.md
├── pyproject.toml
└── .gitignore
```

## 五、知识库（references/）

| 文件 | 核心内容 |
|------|---------|
| `01-context.md` | Who-What-How、Big Idea、3 分钟故事、故事板 |
| `02-visual-display.md` | 12 种图表类型、决策树、避免的图表 |
| `03-clutter.md` | 认知负荷、格式塔 6 原则、去杂乱六步骤 |
| `04-attention.md` | 12 种前注意属性、颜色五原则、渐进式揭示 |
| `05-designer.md` | 可供性、可访问性、美学、接受度 |
| `06-model-visuals.md` | 5 个模型视觉的设计解剖 |
| `07-storytelling.md` | 三幕结构、BBB、水平 / 垂直逻辑 |
| `08-pulling-together.md` | 六步法完整实战案例 |
| `09-case-studies.md` | 深色背景、动画、排序、意面图、饼图替代 |
| `10-final-thoughts.md` | 5 个实践建议、团队能力建设 |
| `11-quick-reference.md` | 决策树、检查清单、评分表、问题修复映射 |

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

**评级**：90+ 卓越 | 70-89 良好 | 50-69 需改进 | <50 需重做

## 八、Python 工具包

### 8.1 安装

纯 Python，无外部依赖，Python 3.8+。

```python
from swd import SWDSkill
skill = SWDSkill("Q4 季度业绩汇报")
# 可选：自定义配置
from swd import AnalysisConfig
skill = SWDSkill("Q4 季度业绩汇报", config=AnalysisConfig())
```

### 8.2 SWDSkill 方法一览

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

### 8.3 八大核心模块

#### 模块 1：上下文分析 — `context.py`
`ContextBuilder` → `ContextAnalysis`

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| audience | str | ✅ | 主要受众（如"产品VP"） |
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

```python
result = skill.build_context(
    audience="产品VP", cta="批准200万预算", decision_maker="CTO",
    knowledge_level="general",
    big_idea="新用户引导体验是增长瓶颈，投入200万可在Q1恢复增长",
    supporting_data=["新用户7日留存率从45%降至32%"],
)
```

#### 模块 2：图表选择 — `chart_selector.py`
`ChartSelector` → `ChartRecommendation`

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| data_type | str | ✅ | categorical / continuous / relationship / single_number |
| series_count | int | | 数据系列数（默认 1） |
| category_count | int | | 类别数（默认 0） |
| has_time | bool | | 是否有时间维度 |
| show_part_of_whole | bool | | 是否展示部分与整体 |
| category_names_long | bool | | 类别名是否较长 |
| compare_two_points | bool | | 是否比较两个时间点 |
| proposed_chart | str | | 检测是否应避免（pie/3d/dual_axis） |

```python
result = skill.recommend_chart(
    data_type="continuous", has_time=True, series_count=2, proposed_chart="pie",
)
```

#### 模块 3：去杂乱诊断 — `declutter.py`
`DeclutterAnalyzer` → `DeclutterReport`

| 参数 | 类型 | 说明 |
|------|------|------|
| has_border | bool | 图表边框 |
| has_gridlines | bool | 网格线 |
| has_3d | bool | 3D 效果 |
| has_diagonal_text | bool | 对角文本 |
| has_separate_legend | bool | 独立图例 |
| has_trailing_zeros | bool | 尾部零（250.00） |
| has_data_markers | bool | 不必要的数据标记 |
| gestalt_issues | List[Tuple] | (原则, 问题, 建议) |
| alignment_issues | List[str] | 对齐问题 |
| whitespace_issues | List[str] | 白空间问题 |

```python
result = skill.diagnose_clutter(
    has_border=True, has_gridlines=True, has_3d=True,
    gestalt_issues=[("proximity", "标签离数据太远", "缩小间距")],
)
```

#### 模块 4：注意力引导 — `attention.py`
`AttentionAnalyzer` → `AttentionPlan`

| 参数 | 类型 | 说明 |
|------|------|------|
| focus_elements | List[Tuple[str, int]] | 焦点元素：(名称, 重要性 1-5) |
| color_strategy | str | grey_plus_one / sequential / diverging |
| accent_color | str | 强调色（默认蓝色） |
| hierarchy | List[Tuple[int, List[str], str]] | (级别, 元素列表, 处理方式) |

```python
result = skill.plan_attention(
    focus_elements=[("流失率趋势", 5), ("基准线", 2)],
    hierarchy=[(1, ["流失率趋势"], "大号+粗体+蓝色"), (3, ["轴标签"], "小号+浅灰")],
)
```

#### 模块 5：设计评估 — `designer.py`
`DesignEvaluator` → `DesignAssessment`。参数均为 bool：has_title / has_axis_titles / has_action_title / has_annotations / color_strategic / alignment_clean / whitespace_ok / hierarchy_clear / highlight_limited / distractions_removed。

```python
result = skill.evaluate_design(
    has_title=True, has_action_title=False, color_strategic=False, alignment_clean=True,
)
```

#### 模块 6：故事构建 — `storyteller.py`
`StoryBuilder` → `DataStory`。关键参数：protagonist（主角）、imbalance（冲突）、evidence（数据证据列表）、call_to_action（行动号召）、narrative_flow（chronological / lead_with_ending）、slide_titles（标题序列）。

```python
result = skill.build_story(
    protagonist="产品委员会", imbalance="用户增长率下降",
    evidence=["留存率降至32%", "竞品NPS高出20分"],
    call_to_action="批准200万优化预算",
    slide_titles=["增长率降至8%", "根因：首周留存骤降", "建议投入200万优化"],
)
```

#### 模块 7：综合诊断 — `diagnosis.py`
`DiagnosisEngine` → `DiagnosisResult`。参数：scores 字典，五个维度各含 4 个评分项（每项 1-5 分）。

```python
result = skill.full_diagnosis(scores={
    "context": {"audience_clear": 4, "cta_clear": 3, "big_idea_visible": 2, "data_supports_story": 4},
    "visual_choice": {"chart_type_fit": 5, "avoid_bad_charts": 5, "zero_baseline": 5, "logical_order": 4},
    "clutter": {"no_unnecessary_elements": 3, "no_diagonal_text": 5, "whitespace_ok": 4, "no_redundancy": 3},
    "attention": {"preattentive_used": 2, "color_sparse": 3, "visual_hierarchy": 2, "eyes_drawn_test": 3},
    "design_narrative": {"text_sufficient": 4, "alignment_aesthetic": 4, "narrative_structure": 3, "action_titles": 2},
})
```

#### 模块 8：图表改造 — `makeover.py`
`MakeoverEngine` → `MakeoverPlan`。参数：issues（问题列表）、chart_type / title / color_accent（设计规范）、narrative_slides（叙事幻灯片序列）。

```python
result = skill.makeover(
    issues=["使用了饼图", "无标题", "彩虹色"],
    chart_type="水平柱状图",
    title="客户满意度最高的三个功能贡献了75%的好评",
    narrative_slides=[("整体满意度82%", "建立信任"), ("功能C和D满意度偏低", "揭示问题")],
)
```

### 8.4 完整使用示例

#### 示例 1：季度业绩汇报（端到端）

```python
from swd import SWDSkill
skill = SWDSkill("Q4季度业绩汇报")

ctx = skill.build_context(
    audience="CEO和产品VP", cta="批准Q1增长计划的300万预算",
    decision_maker="CEO", knowledge_level="general", mechanism="live_presentation",
    big_idea="用户增长放缓源于引导体验不佳，投入300万可在Q1恢复15%月均增长",
    supporting_data=["新用户7日留存率从45%降至32%", "竞品首周体验NPS高出20分"],
)
chart = skill.recommend_chart(data_type="continuous", has_time=True, series_count=3, category_count=12)
clutter = skill.diagnose_clutter(has_border=True, has_gridlines=True, has_separate_legend=True)
attn = skill.plan_attention(
    focus_elements=[("流失率趋势线", 5), ("行业基准", 2), ("轴标签", 1)],
    hierarchy=[(1, ["流失率趋势线"], "大号+粗体+蓝色"),
               (2, ["行业基准"], "深灰+虚线"), (3, ["轴标签"], "浅灰")],
)
design = skill.evaluate_design(
    has_title=True, has_axis_titles=True, has_action_title=True,
    has_annotations=True, color_strategic=True, alignment_clean=True,
)
story = skill.build_story(
    protagonist="CEO和产品VP",
    imbalance="新用户月均增长率从15%降至8%，连续3个月下滑",
    evidence=["首周留存率从45%降至32%", "竞品首周NPS高出20分",
              "A/B测试显示优化可提升留存12%"],
    call_to_action="批准300万预算用于Q1新用户引导体验优化",
    narrative_flow="lead_with_ending",
    slide_titles=["建议投入300万优化新用户引导", "增长率连续3月降至8%",
                  "根因：首周留存骤降至32%", "A/B测试证明优化可提升12%"],
)
```

#### 示例 2：图表改造（诊断 → 改造）

```python
from swd import SWDSkill
skill = SWDSkill("客户满意度报告改造")

diag = skill.full_diagnosis(scores={
    "context":       {"audience_clear": 2, "cta_clear": 1, "big_idea_visible": 1, "data_supports_story": 3},
    "visual_choice": {"chart_type_fit": 1, "avoid_bad_charts": 1, "zero_baseline": 5, "logical_order": 2},
    "clutter":       {"no_unnecessary_elements": 2, "no_diagonal_text": 1, "whitespace_ok": 2, "no_redundancy": 2},
    "attention":     {"preattentive_used": 1, "color_sparse": 1, "visual_hierarchy": 1, "eyes_drawn_test": 1},
    "design_narrative": {"text_sufficient": 2, "alignment_aesthetic": 2, "narrative_structure": 1, "action_titles": 1},
})
makeover = skill.makeover(
    issues=["使用了饼图展示5个类别", "无标题", "彩虹色配色", "独立图例", "对角文本标签"],
    chart_type="水平柱状图", title="客户满意度最高的三个功能贡献了75%的好评", color_accent="蓝色",
    narrative_slides=[
        ("整体满意度达到82%，高于行业均值", "先展示好消息建立信任"),
        ("但功能C和D的满意度显著低于平均", "用橙色强调问题区域"),
        ("建议优先优化功能C的用户体验", "给出明确行动号召"),
    ],
)
kb = skill.search_knowledge("饼图")
```

### 8.5 AI Agent 调用规则

| # | 规则 | 说明 |
|---|------|------|
| 1 | **统一入口** | 始终通过 `SWDSkill` 类调用，不直接实例化子模块 |
| 2 | **返回值** | 所有方法返回 Markdown 字符串，可直接展示 |
| 3 | **触发映射** | 根据用户意图选择对应能力（参见触发条件总表） |
| 4 | **组合调用** | 综合任务按能力一→八顺序执行 |
| 5 | **知识优先** | 理论问题先调用 `search_knowledge()` 查询 |
| 6 | **渐进式** | 先诊断（能力七）再改造（能力八），不跳过诊断 |
| 7 | **上下文先行** | 任何可视化任务先执行上下文分析（能力一） |
| 8 | **验证闭环** | 改造后用设计评估（能力五）验证效果 |

### 8.6 测试

```bash
python swd/tests/test_all.py               # 运行全部 8 个测试
python -m pytest swd/tests/test_all.py -v   # pytest
```

| 测试用例 | 覆盖能力 | 验证内容 |
|---------|---------|---------|
| `test_build_context()` | 上下文分析 | 受众画像、Big Idea、支撑数据、风险 |
| `test_recommend_chart()` | 图表选择 | 折线图/柱状图/坡度图推荐、饼图避免 |
| `test_diagnose_clutter()` | 去杂乱 | 6 种杂乱检测、格式塔建议 |
| `test_plan_attention()` | 注意力引导 | 焦点分析、颜色策略、视觉层次 |
| `test_evaluate_design()` | 设计评估 | 全通过→卓越、多项未通过→需改进 |
| `test_build_story()` | 故事构建 | 三幕结构、BBB、标题序列 |
| `test_full_diagnosis()` | 综合诊断 | 五维度评分、总分、评级 |
| `test_makeover()` | 图表改造 | 问题识别、改造步骤、叙事幻灯片 |

### 8.7 与其他 Skill 协作

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 用户研究报告可视化 | AliDujie/Quantitative-UX-Research | UXR 数据 → SWD 选图表 → 构建故事 |
| 价值主张数据展示 | AliDujie/value-proposition-design | VPD 画布 → SWD 可视化 → 改造图表 |
| JTBD 研究结果汇报 | AliDujie/jtbd-knowledge-skill | JTBD 分析 → SWD 上下文 → 构建汇报故事 |

```python
# 协作示例：JTBD + SWD
swd = SWDSkill("JTBD研究结果汇报")
ctx = swd.build_context(
    audience="产品委员会", cta="基于JTBD发现调整Q2产品路线图",
    big_idea="用户核心Job是'快速完成任务'而非'探索功能'，应简化而非增加功能",
)
chart = swd.recommend_chart(data_type="categorical", category_count=8, category_names_long=True)
story = swd.build_story(
    protagonist="产品委员会",
    imbalance="产品功能过多导致用户完成核心任务时间增加40%",
    evidence=["80%用户核心Job是快速完成任务", "60%功能使用率<5%"],
    call_to_action="精简产品功能，聚焦核心Job",
)
```
