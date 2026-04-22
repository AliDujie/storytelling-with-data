# Storytelling with Data Skill

基于 Cole Nussbaumer Knaflic《Storytelling with Data》的数据可视化与数据叙事工具集。提供 8 项可执行能力和 11 篇方法论知识库，覆盖从上下文分析到图表改造的完整 SWD 六课工作流。

## 快速开始

作为 Agent Skill 使用：将整个目录复制到你的 skills 目录即可。Agent 会自动读取 `SKILL.md` 获取执行指令。

作为 Python 包使用：

```python
import sys
sys.path.insert(0, "/path/to/storytelling-with-data")
from swd import SWDSkill

skill = SWDSkill("季度业绩汇报")

# 上下文分析 — 明确受众和核心信息
ctx = skill.build_context(audience="产品VP", cta="批准200万预算继续项目")

# 图表选择 — 时间趋势数据推荐折线图
chart = skill.recommend_chart(data_type="continuous", has_time=True, series_count=2, category_count=12)

# 去杂乱诊断 — 检测杂乱元素并给出改进建议
clutter = skill.diagnose_clutter(has_border=True, has_gridlines=True, has_separate_legend=True)

# 注意力引导 — 规划颜色策略和视觉层次
attn = skill.plan_attention(
    focus_elements=[("关键指标", 5), ("基准线", 2)],
    color_strategy="grey_plus_one",
)

# 设计评估 — 三维度检查
design = skill.evaluate_design(has_title=True, has_action_title=True, color_strategic=True)

# 故事构建 — 三幕结构
story = skill.build_story(
    protagonist="产品委员会",
    imbalance="用户增长率连续3个月下降",
    call_to_action="批准200万优化预算",
)

# 综合诊断 — 五维度100分制
diag = skill.full_diagnosis(scores={
    "context": {"audience_clear": 4, "cta_clear": 3, "big_idea_visible": 2, "data_supports_story": 4},
    "visual_choice": {"chart_type_fit": 5, "avoid_bad_charts": 5, "zero_baseline": 5, "logical_order": 4},
    "clutter": {"no_unnecessary_elements": 3, "no_diagonal_text": 5, "whitespace_ok": 4, "no_redundancy": 3},
    "attention": {"preattentive_used": 2, "color_sparse": 3, "visual_hierarchy": 2, "eyes_drawn_test": 3},
    "design_narrative": {"text_sufficient": 4, "alignment_aesthetic": 4, "narrative_structure": 3, "action_titles": 2},
})

# 图表改造 — 六步法
makeover = skill.makeover(issues=["使用了饼图", "无标题", "彩虹色配色"])
```

## 核心能力

本 Skill 提供 8 项执行能力：上下文分析、图表选择推荐、去杂乱诊断、注意力引导规划、设计评估、数据故事构建、五维度综合诊断、图表改造。所有方法通过 `SWDSkill` 统一入口调用，返回 Markdown 格式报告。详细说明见 `SKILL.md`。

纯标准库实现，无外部依赖，仅需 Python 3.8+。

## 文件结构

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

## 运行测试

```bash
cd /path/to/storytelling-with-data
python3 swd/tests/test_all.py
# 或使用 pytest
python3 -m pytest swd/tests/test_all.py -v
```

## 许可

基于《Storytelling with Data》by Cole Nussbaumer Knaflic (2015)。

v2.0.0
