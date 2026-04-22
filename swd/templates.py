"""SWD Skill 模板模块 - 报告、分析、检查清单的模板定义"""

from typing import Dict, List

# ── 上下文分析报告模板 ──
CONTEXT_REPORT_TEMPLATE = """# 📋 上下文分析报告：{title}

## 受众画像
| 维度 | 内容 |
|------|------|
| 主要受众 | {audience} |
| 决策者 | {decision_maker} |
| 了解程度 | {knowledge_level} |
| 关系状态 | {relationship} |
| 动机 | {motivation} |

## 沟通机制
- **形式**: {mechanism}
- **语气**: {tone}

## 核心信息
### 3分钟故事
{three_min_story}

### 大创意 (Big Idea)
> {big_idea}

### 支撑数据
{supporting_data}

### 风险与反面证据
{risks}

## 行动号召
{call_to_action}
"""

# ── 图表选择报告模板 ──
CHART_SELECTION_TEMPLATE = """# 📊 图表选择建议

## 数据特征
- **数据类型**: {data_type}
- **数据系列数**: {series_count}
- **类别数**: {category_count}
- **时间维度**: {has_time}

## 推荐图表
### 首选: {primary_chart}
{primary_reason}

### 备选: {secondary_chart}
{secondary_reason}

## 避免使用
{avoid_charts}

## 设计要点
{design_notes}
"""

# ── 去杂乱诊断报告模板 ──
DECLUTTER_REPORT_TEMPLATE = """# 🧹 去杂乱诊断报告

## 诊断摘要
- **检测到的杂乱元素**: {clutter_count} 项
- **预计可减少的认知负荷**: {reduction_pct}%

## 杂乱元素清单
{clutter_items}

## 去杂乱步骤建议
{declutter_steps}

## 格式塔原则应用建议
{gestalt_suggestions}
"""

# ── 注意力引导报告模板 ──
ATTENTION_REPORT_TEMPLATE = """# 🎯 注意力引导分析

## 当前焦点分析
{current_focus}

## 建议使用的前注意属性
{preattentive_suggestions}

## 颜色策略
- **推荐策略**: {color_strategy}
- **基色**: {base_color}
- **强调色**: {accent_color}
{color_notes}

## 视觉层次设计
{visual_hierarchy}
"""

# ── 设计评估报告模板 ──
DESIGN_REPORT_TEMPLATE = """# 🎨 设计评估报告

## 可供性 (Affordances)
{affordances}

## 可访问性 (Accessibility)
{accessibility}

## 美学 (Aesthetics)
{aesthetics}

## 改进建议
{improvements}
"""

# ── 故事构建模板 ──
STORY_TEMPLATE = """# 📖 数据故事构建

## 故事结构

### 第一幕：开始 (Setup)
- **设定**: {setting}
- **主角**: {protagonist}（受众视角）
- **不平衡**: {imbalance}
- **期望平衡**: {desired_balance}

### 第二幕：中间 (Conflict)
{middle_content}

### 第三幕：结尾 (Resolution)
- **行动号召**: {call_to_action}
- **回扣开头**: {tie_back}

## 叙事流
- **叙事顺序**: {narrative_flow}
- **沟通形式**: {delivery_mode}

## Bing, Bang, Bongo
- **Bing (预告)**: {bing}
- **Bang (主体)**: {bang}
- **Bongo (回顾)**: {bongo}

## 幻灯片标题序列（水平逻辑）
{slide_titles}
"""

# ── 综合诊断报告模板 ──
DIAGNOSIS_REPORT_TEMPLATE = """# 🔍 SWD 综合诊断报告：{title}

## 总分: {total_score}/100 {score_badge}

{dimension_details}

## 优先改进建议（Top 3）
{top_improvements}

## 改造前后对比建议
{makeover_suggestions}
"""

# ── 图表改造报告模板 ──
MAKEOVER_REPORT_TEMPLATE = """# ✨ 图表改造方案：{title}

## 原始问题诊断
{original_issues}

## 改造步骤
{makeover_steps}

## 改造后设计规范
{design_spec}

## 叙事增强
{narrative_enhancement}
"""

# ── 图表制作检查清单 ──
CHART_CHECKLIST: List[tuple] = [
    ("图表标题", "使用行动标题而非描述标题"),
    ("轴标题", "每个轴都需要标题"),
    ("零基线", "柱状图必须有零基线"),
    ("时间轴一致", "时间间隔必须一致"),
    ("直接标注", "直接标注数据系列而非使用图例"),
    ("图表边框", "移除不必要的图表边框"),
    ("网格线", "移除或弱化网格线"),
    ("数据标记", "移除不必要的数据标记"),
    ("轴标签", "清晰简洁，无尾部零，无对角文本"),
    ("颜色策略", "使用有意义的颜色而非工具默认"),
    ("符号保留", "保留美元符号、百分号、千位分隔符"),
    ("数据来源", "标注数据来源"),
]

# ── 颜色策略模板 ──
COLOR_STRATEGY_TEMPLATES: Dict[str, Dict[str, str]] = {
    "grey_plus_one": {
        "name": "灰色基底+单一强调色",
        "base": "灰色 (#808080)",
        "accent": "蓝色 (#4472C4)",
        "negative": "橙色 (#ED7D31)",
        "description": "所有非焦点元素用灰色，仅焦点用强调色。最通用的策略。",
    },
    "sequential": {
        "name": "单色渐变",
        "base": "浅蓝 (#D6E4F0)",
        "accent": "深蓝 (#1F4E79)",
        "negative": "",
        "description": "同一色调的不同饱和度，适合热力图和排名数据。",
    },
    "diverging": {
        "name": "双色分歧",
        "base": "灰色 (#808080)",
        "accent": "蓝色 (#4472C4)",
        "negative": "橙色 (#ED7D31)",
        "description": "蓝色=正面，橙色=负面。避免红绿（色盲友好）。",
    },
    "categorical_limited": {
        "name": "有限分类色",
        "base": "灰色 (#808080)",
        "accent": "蓝色 (#4472C4)",
        "negative": "",
        "description": "最多4-5种颜色区分类别，避免彩虹色。",
    },
}
