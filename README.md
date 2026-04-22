# Storytelling with Data (SWD) Skill

> 📊 **用数据讲故事，让洞察直抵人心**

基于 Cole Nussbaumer Knaflic《Storytelling with Data》的完整数据叙事与可视化技能。

[English](#english) | [中文](#中文说明)

---

## 中文说明

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **经典框架** — 基于全球畅销书《Storytelling with Data》，数据可视化领域必读
- **8 大执行能力** — 上下文分析、图表选择、去杂乱、注意力引导、设计评估、故事构建、综合诊断、图表改造
- **实战导向** — 内置图表推荐引擎、去杂乱诊断器、注意力规划器，即刻优化你的可视化
- **零依赖** — 纯 Python 标准库，5 分钟上手，即刻产出
- **双语支持** — 完整中英文文档，适合国际化团队
- **专业可靠** — 基于权威著作，避免常见可视化陷阱

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r skills/storytelling-with-data ~/.aoneclaw/skills/
```

#### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/storytelling-with-data")
from swd import SWDSkill

# 初始化技能
skill = SWDSkill("季度业绩汇报")
```

#### 步骤 3: 开始使用

```python
# ===== 场景 1: 上下文分析 =====
ctx = skill.build_context(
    audience="产品 VP",
    need="了解 Q3 业绩表现",
    cta="批准 Q4 新功能投入"
)
print(skill.analyze_context(ctx))

# ===== 场景 2: 图表选择推荐 =====
rec = skill.recommend_chart(
    data_type="continuous",
    has_time=True,
    comparison="yes"
)
print(rec)  # 推荐：折线图、柱状图等

# ===== 场景 3: 去杂乱诊断 =====
clutter = skill.diagnose_clutter(
    has_border=True,
    has_gridlines=True,
    has_legend=True,
    colors=8
)
print(clutter)  # 识别杂乱元素，给出简化建议

# ===== 场景 4: 注意力引导规划 =====
attn = skill.plan_attention(
    focus_elements=[("关键指标", 5), ("趋势线", 3)],
    use_color_strategically=True
)
print(attn)

# ===== 场景 5: 设计评估 =====
design = skill.evaluate_design(
    has_title=True,
    has_subtitle=True,
    color_strategic=True,
    labels_clear=True
)
print(design)  # 设计评分 + 改进建议

# ===== 场景 6: 故事构建 =====
story = skill.build_story(
    protagonist="产品团队",
    imbalance="用户流失加剧",
    resolution="新功能提升留存"
)
print(story)  # 三幕式故事结构

# ===== 场景 7: 综合诊断 =====
diag = skill.full_diagnosis(
    scores={
        "context": {"audience_clear": 4, "cta_clear": 3},
        "visual": {"chart_appropriate": 5, "clutter_free": 2},
        "story": {"narrative_clear": 4}
    }
)
print(diag)  # 综合评分 + 优先级改进建议

# ===== 场景 8: 图表改造 =====
makeover = skill.makeover(
    issues=["使用了饼图", "无标题", "颜色过多", "网格线太密"],
    chart_type="bar"
)
print(makeover)  # 改造前后对比 + 具体建议
```

### 💡 8 大核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **上下文分析** | `context.py` | 分析受众、需求、行动号召，确保图表服务于目标 |
| 2 | **图表选择** | `chart_selector.py` | 根据数据类型、比较需求推荐最佳图表类型 |
| 3 | **去杂乱诊断** | `declutter.py` | 识别并消除不必要的视觉元素 |
| 4 | **注意力引导** | `attention.py` | 规划视觉层次，引导受众关注重点 |
| 5 | **设计评估** | `designer.py` | 评估可视化设计的专业性和有效性 |
| 6 | **故事构建** | `storyteller.py` | 构建三幕式数据叙事结构 |
| 7 | **综合诊断** | `diagnosis.py` | 全维度评估，给出优先级改进建议 |
| 8 | **图表改造** | `makeover.py` | 针对问题图表提供具体改造方案 |

### 🔧 实用示例

#### 示例 1: 完整可视化优化流程

```python
from swd import SWDSkill

skill = SWDSkill("月度销售报告")

# 步骤 1: 明确上下文
ctx = skill.build_context(
    audience="销售总监",
    need="了解各区域表现",
    cta="调整资源分配"
)

# 步骤 2: 选择合适图表
rec = skill.recommend_chart(
    data_type="categorical",
    comparison="between_groups"
)
# → 推荐：柱状图、条形图

# 步骤 3: 诊断当前图表
clutter = skill.diagnose_clutter(
    has_border=True, has_gridlines=True, has_3d=True
)
# → 发现：3D 效果、网格线、边框都是不必要的

# 步骤 4: 规划注意力
attn = skill.plan_attention(
    focus_elements=[("表现最佳区域", 5), ("表现最差区域", 4)]
)
# → 建议：使用强调色突出关键区域

# 步骤 5: 生成改造方案
makeover = skill.makeover(
    issues=["3D 效果", "过多网格线", "无数据标签"],
    chart_type="bar"
)
```

#### 示例 2: 数据叙事构建

```python
from swd import SWDSkill

skill = SWDSkill("用户增长汇报")

# 构建故事框架
story = skill.build_story(
    protagonist="增长团队",
    context="Q3 用户增长放缓",
    imbalance="新用户获取成本上升 50%",
    resolution="优化渠道策略，CAC 下降 30%",
    call_to_action="继续投资高效渠道"
)

print(story)
# 输出：
# 第一幕：设定场景 (Q3 增长挑战)
# 第二幕：冲突与洞察 (CAC 上升原因分析)
# 第三幕：解决方案 (渠道优化成果)
# 行动号召 (资源分配建议)
```

#### 示例 3: 图表选择决策树

```python
from swd import SWDSkill

skill = SWDSkill("数据分析")

# 场景 1: 展示趋势
rec1 = skill.recommend_chart(
    data_type="continuous",
    has_time=True
)
# → 折线图

# 场景 2: 比较类别
rec2 = skill.recommend_chart(
    data_type="categorical",
    comparison="between_groups"
)
# → 柱状图/条形图

# 场景 3: 展示占比
rec3 = skill.recommend_chart(
    data_type="categorical",
    comparison="part_to_whole"
)
# → 堆叠柱状图 (避免饼图)

# 场景 4: 展示关系
rec4 = skill.recommend_chart(
    data_type="continuous",
    relationship="correlation"
)
# → 散点图
```

### 📁 项目结构

```
storytelling-with-data/
├── skills/swd/SKILL.md          # AI Agent 技能定义
├── swd/                         # Python 工具包
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
├── knowledge/                   # 知识库文档 (11 个)
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
└── README.md
```

### 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的呈现层核心：

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

- **SWD + QuantUX** → 将量化分析结果用故事方式呈现
- **SWD + UDM** → 将用户研究发现转化为有说服力的叙事
- **SWD + JTBD** → 用故事传达用户动机和进步需求
- **SWD + VPD** → 向利益相关者展示价值主张验证结果
- **SWD + Persona** → 让人物角色"活"起来，增强共情

👉 **探索完整生态系统**: [JTBD](../jtbd-knowledge-skill/) | [价值主张设计](../value-proposition-design/) | [量化 UX 研究](../quantitative-ux-research/) | [人物角色](../web-persona-skill/) | [通用设计方法](../universal-design-methods/)

### 🤝 最佳实践

#### 图表选择速查

| 目的 | 推荐图表 | 避免 |
|------|---------|------|
| **展示趋势** | 折线图 | 饼图、3D 图 |
| **比较类别** | 柱状图/条形图 | 雷达图 (类别>5) |
| **展示占比** | 堆叠柱状图 | 饼图 (类别>5) |
| **展示关系** | 散点图、气泡图 | 3D 散点图 |
| **展示分布** | 直方图、箱线图 | 饼图 |

#### 去杂乱检查清单

- [ ] 移除不必要的边框
- [ ] 减少或移除网格线
- [ ] 移除图例 (直接标注)
- [ ] 移除 3D 效果
- [ ] 减少颜色数量 (≤5 种)
- [ ] 移除装饰性元素
- [ ] 简化坐标轴标签

#### 注意力引导技巧

1. **位置** — 重要信息放左上或顶部
2. **颜色** — 用强调色突出关键点 (其他用灰色)
3. **大小** — 重要元素更大
4. **对比** — 用对比创造视觉层次
5. **留白** — 给重点内容呼吸空间

### 🛠️ 故障排查

#### 问题 1: 不知道选什么图表

**解决**: 使用图表选择决策树

```python
rec = skill.recommend_chart(
    data_type="continuous",  # 或 categorical
    has_time=True,           # 是否有时间维度
    comparison="yes"         # 是否需要比较
)
```

#### 问题 2: 图表太杂乱

**解决**: 运行去杂乱诊断

```python
clutter = skill.diagnose_clutter(
    has_border=True,
    has_gridlines=True,
    has_legend=True,
    colors=8
)
# → 逐项列出杂乱元素和简化建议
```

#### 问题 3: 汇报缺乏说服力

**解决**: 构建数据故事

```python
story = skill.build_story(
    protagonist="你的团队",
    imbalance="问题/挑战",
    resolution="你的方案/成果"
)
```

### 📚 关于《Storytelling with Data》

- **书名**: Storytelling with Data: A Data Visualization Guide for Business Professionals
- **作者**: Cole Nussbaumer Knaflic
- **出版**: Wiley, 2015
- **地位**: 数据可视化领域经典，全球畅销
- **适用**: 数据分析师、产品经理、市场人员、管理者

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 🌟 Why Use This Skill?

- **Classic Framework** — Based on the bestselling book "Storytelling with Data"
- **8 Core Capabilities** — Context analysis, chart selection, decluttering, attention guidance, design evaluation, storytelling, diagnosis, makeover
- **Production-Ready** — Built-in chart recommender, clutter diagnostician, attention planner
- **Zero Dependencies** — Pure Python standard library, 5-minute setup
- **Bilingual** — Complete CN/EN documentation
- **Professional** — Based on authoritative work, avoid common visualization pitfalls

### 🚀 Quick Start

```python
from swd import SWDSkill

skill = SWDSkill("Quarterly Report")

# Context analysis
ctx = skill.build_context(audience="VP", need="Understand performance", cta="Approve budget")

# Chart selection
rec = skill.recommend_chart(data_type="continuous", has_time=True)

# Declutter diagnosis
clutter = skill.diagnose_clutter(has_border=True, has_gridlines=True)

# Attention planning
attn = skill.plan_attention(focus_elements=[("Key Metric", 5)])

# Story building
story = skill.build_story(protagonist="Team", imbalance="Problem", resolution="Solution")
```

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

- **[Quantitative-UX-Research](../quantitative-ux-research/)** — Quantitative analysis, HEART framework
- **[Universal-Design-Methods](../universal-design-methods/)** — 100 design research methods
- **[JTBD-Knowledge-Skill](../jtbd-knowledge-skill/)** — Jobs-to-be-Done theory
- **[Value-Proposition-Design](../value-proposition-design/)** — Value proposition canvas
- **[Web-Persona-Skill](../web-persona-skill/)** — Persona creation

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies**
- Cross-platform: macOS / Linux / Windows

---

## 📜 许可 (License)

本技能仅供内部学习和研究使用。

## 👨‍💻 作者 (Credits)

- 基于《Storytelling with Data》by Cole Nussbaumer Knaflic
- 技能开发：AliDujie 团队
- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫
