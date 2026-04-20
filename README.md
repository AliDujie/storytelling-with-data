# Storytelling with Data (SWD) Skill

基于 Cole Nussbaumer Knaflic《Storytelling with Data》的完整 AI Skill，覆盖数据可视化与数据叙事的 8 大执行能力。

## 安装为 AI Skill

将 `skills/swd/` 目录复制到 `~/.aoneclaw/skills/swd/`：

```bash
cp -r skills/swd ~/.aoneclaw/skills/swd
```

AI 加载后即自动具备全部 8 大执行能力，用自然语言交互即可。

## 8 大执行能力

| # | 能力 | 触发词示例 |
|---|------|-----------|
| 1 | 上下文分析 | "帮我分析受众"、"Big Idea" |
| 2 | 图表选择 | "用什么图"、"怎么展示数据" |
| 3 | 去杂乱诊断 | "图太乱"、"简化" |
| 4 | 注意力引导 | "突出重点"、"颜色怎么用" |
| 5 | 设计评估 | "好不好看"、"专不专业" |
| 6 | 故事构建 | "怎么讲故事"、"汇报结构" |
| 7 | 综合诊断 | "帮我看看这个图"、"评分" |
| 8 | 图表改造 | "改造"、"优化" |

## 目录结构

```
storytelling-with-data-skill/
├── SKILL.md                    # 顶层索引
├── README.md                   # 本文件
├── skills/
│   └── swd/
│       └── SKILL.md            # 主技能定义（234行，小模型友好）
├── knowledge/                  # 知识库文档（11个）
│   ├── 01-context.md           # 上下文的重要性
│   ├── 02-visual-display.md    # 选择有效的视觉展示
│   ├── 03-clutter.md           # 杂乱是你的敌人
│   ├── 04-attention.md         # 聚焦受众注意力
│   ├── 05-designer.md          # 像设计师一样思考
│   ├── 06-model-visuals.md     # 解剖模型视觉
│   ├── 07-storytelling.md      # 叙事课
│   ├── 08-pulling-together.md  # 融会贯通
│   ├── 09-case-studies.md      # 案例研究
│   ├── 10-final-thoughts.md    # 最终思考
│   └── 11-quick-reference.md   # 速查手册
├── swd/                        # Python 工具包
│   ├── __init__.py             # SWDSkill 统一入口
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
│   └── utils.py                # 工具函数
├── pyproject.toml
├── requirements.txt
└── .gitignore
```

## Python 工具包使用

```python
import sys
sys.path.insert(0, "/path/to/storytelling-with-data-skill")
from swd import SWDSkill

skill = SWDSkill("季度业绩汇报")

# 上下文分析
ctx = skill.build_context(audience="产品VP", cta="批准新功能投入")

# 图表选择
rec = skill.recommend_chart(data_type="continuous", has_time=True)

# 去杂乱诊断
clutter = skill.diagnose_clutter(has_border=True, has_gridlines=True)

# 注意力引导
attn = skill.plan_attention(focus_elements=[("关键指标", 5)])

# 设计评估
design = skill.evaluate_design(has_title=True, color_strategic=False)

# 故事构建
story = skill.build_story(protagonist="产品团队", imbalance="用户流失加剧")

# 综合诊断
diag = skill.full_diagnosis(scores={"context": {"audience_clear": 4}})

# 图表改造
makeover = skill.makeover(issues=["使用了饼图", "无标题"])
```

## 知识库搜索

```python
from swd import search_knowledge
results = search_knowledge("格式塔")
```

## 作者

- empId: 27768
- nickname: 渡劫
