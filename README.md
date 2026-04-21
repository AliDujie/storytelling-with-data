# Storytelling with Data (SWD) Skill

> 📊 **让数据讲故事，让洞察更有力**

基于 Cole Nussbaumer Knaflic《Storytelling with Data》的完整 AI Skill，覆盖数据可视化与数据叙事的 8 大执行能力。

## 🌟 为什么使用这个技能？

- **专业级数据叙事** — 基于全球畅销书，掌握顶级咨询公司的数据呈现方法
- **8 大核心能力** — 从上下文分析到图表改造，覆盖数据沟通全流程
- **开箱即用** — Python 工具包 + AI Skill 双模式，5 分钟上手
- **实战导向** — 提供真实案例、诊断清单、改造模板
- **双语支持** — 完整中英文文档，适合国际化团队

## 🚀 5 分钟快速开始

### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r skills/swd ~/.aoneclaw/skills/swd
```

### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/storytelling-with-data")
from swd import SWDSkill

# 初始化技能
skill = SWDSkill("季度业绩汇报")
```

### 步骤 3: 开始使用

```python
# 场景 1: 分析汇报受众，明确 Big Idea
ctx = skill.build_context(
    audience="产品 VP",
    need="了解新功能投入的必要性",
    cta="批准新功能投入预算"
)
print(ctx)

# 场景 2: 不知道用什么图表？AI 推荐！
rec = skill.recommend_chart(
    data_type="continuous",
    has_time=True,
    comparison=True
)
print(rec)  # 推荐折线图/柱状图，并说明理由

# 场景 3: 图表太乱？一键诊断！
clutter = skill.diagnose_clutter(
    has_border=True,
    has_gridlines=True,
    has_legend=True,
    colors=8
)
print(clutter)  # 识别杂乱元素，给出简化建议

# 场景 4: 需要突出重点？注意力引导方案！
attn = skill.plan_attention(
    focus_elements=[("关键指标", 5), ("趋势线", 3)],
    color_strategy="strategic"
)
print(attn)  # 颜色、位置、大小组合方案

# 场景 5: 设计好不好？专业评估！
design = skill.evaluate_design(
    has_title=True,
    color_strategic=True,
    consistent_fonts=True
)
print(design)  # 评分 + 改进建议

# 场景 6: 构建数据故事框架！
story = skill.build_story(
    protagonist="产品团队",
    setting="竞争加剧的市场环境",
    imbalance="用户流失率上升 30%",
    resolution="新功能可将流失率降低 15%"
)
print(story)  # 完整故事结构

# 场景 7: 综合诊断现有图表！
diag = skill.full_diagnosis(
    scores={"context": {"audience_clear": 4}, "visual": {"clutter_free": 3}}
)
print(diag)  # 6 维度评分 + 优先级建议

# 场景 8: 图表改造！
makeover = skill.makeover(
    chart_type="pie",
    issues=["使用了饼图", "无标题", "颜色过多", "无重点标注"]
)
print(makeover)  # 改造方案 + 前后对比说明
```

## 💡 8 大执行能力

| # | 能力 | 触发词示例 | 输出 |
|---|------|-----------|------|
| 1 | **上下文分析** | "帮我分析受众"、"Big Idea" | 受众画像、需求分析、核心主张 |
| 2 | **图表选择** | "用什么图"、"怎么展示数据" | 图表推荐 + 选择理由 |
| 3 | **去杂乱诊断** | "图太乱"、"简化" | 杂乱元素清单 + 简化方案 |
| 4 | **注意力引导** | "突出重点"、"颜色怎么用" | 视觉层次方案 |
| 5 | **设计评估** | "好不好看"、"专不专业" | 6 维度评分 + 改进建议 |
| 6 | **故事构建** | "怎么讲故事"、"汇报结构" | 完整故事框架 |
| 7 | **综合诊断** | "帮我看看这个图"、"评分" | 全方位诊断报告 |
| 8 | **图表改造** | "改造"、"优化" | 改造方案 + 对比说明 |

## 📁 目录结构

```
storytelling-with-data/
├── skills/swd/
│   └── SKILL.md                 # AI Agent 技能定义
├── swd/                         # Python 工具包（纯标准库）
│   ├── __init__.py              # SWDSkill 统一入口
│   ├── config.py                # 全局配置和常量
│   ├── context.py               # 上下文分析引擎
│   ├── chart_selector.py        # 图表选择决策器
│   ├── declutter.py             # 去杂乱诊断器
│   ├── attention.py             # 注意力引导分析器
│   ├── designer.py              # 设计评估器
│   ├── storyteller.py           # 故事构建器
│   ├── diagnosis.py             # 综合诊断引擎
│   ├── makeover.py              # 图表改造引擎
│   ├── templates.py             # 报告模板
│   └── utils.py                 # 工具函数
├── knowledge/                   # 知识库文档（11 个）
│   ├── 01-context.md            # 上下文的重要性
│   ├── 02-visual-display.md     # 选择有效的视觉展示
│   ├── 03-clutter.md            # 杂乱是你的敌人
│   ├── 04-attention.md          # 聚焦受众注意力
│   ├── 05-designer.md           # 像设计师一样思考
│   ├── 06-model-visuals.md      # 解剖模型视觉
│   ├── 07-storytelling.md       # 叙事课
│   ├── 08-pulling-together.md   # 融会贯通
│   ├── 09-case-studies.md       # 案例研究
│   ├── 10-final-thoughts.md     # 最终思考
│   └── 11-quick-reference.md    # 速查手册
├── pyproject.toml
├── requirements.txt
└── README.md                    # 本文件
```

## 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的一部分：

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 种设计研究方法
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — 量化研究、HEART 框架、A/B 测试
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done 理论
- **[Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design)** — 价值主张画布
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — 人物角色创建

**推荐工作流**：
1. 用 Universal-Design-Methods 收集用户数据
2. 用 Quantitative-UX-Research 分析量化指标
3. **用本技能将分析结果转化为有说服力的数据故事** ← 你的价值在此体现！

## 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

## 📚 关于《Storytelling with Data》

- **书名**: Storytelling with Data: A Data Visualization Guide for Business Professionals
- **作者**: Cole Nussbaumer Knaflic
- **出版**: Wiley, 2015
- **地位**: 数据可视化领域经典著作，Google 前人力分析团队负责人作品
- **适用**: 数据分析师、产品经理、咨询顾问、市场人员

## 📜 许可

本技能仅供内部学习和研究使用。

## 👨‍💻 作者

- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫
