"""SWD Skill 配置模块

定义知识库路径、分析维度、图表类型、颜色策略等全局配置。
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

KNOWLEDGE_BASE_DIR = Path(__file__).parent.parent / "references"

KNOWLEDGE_FILES: Dict[str, str] = {
    "context": "01-context.md",
    "visual": "02-visual-display.md",
    "clutter": "03-clutter.md",
    "attention": "04-attention.md",
    "designer": "05-designer.md",
    "model_visuals": "06-model-visuals.md",
    "storytelling": "07-storytelling.md",
    "pulling_together": "08-pulling-together.md",
    "case_studies": "09-case-studies.md",
    "final": "10-final-thoughts.md",
    "reference": "11-quick-reference.md",
}

# ── 图表类型体系 ──
CHART_TYPES = (
    "simple_text", "table", "heatmap", "scatterplot",
    "line", "slopegraph", "vertical_bar", "horizontal_bar",
    "stacked_vertical_bar", "stacked_horizontal_bar",
    "waterfall", "square_area",
)

CHART_LABELS: Dict[str, str] = {
    "simple_text": "简单文本 (Simple Text)",
    "table": "表格 (Table)",
    "heatmap": "热力图 (Heatmap)",
    "scatterplot": "散点图 (Scatterplot)",
    "line": "折线图 (Line Graph)",
    "slopegraph": "坡度图 (Slopegraph)",
    "vertical_bar": "垂直柱状图 (Vertical Bar)",
    "horizontal_bar": "水平柱状图 (Horizontal Bar)",
    "stacked_vertical_bar": "堆叠垂直柱状图 (Stacked Vertical Bar)",
    "stacked_horizontal_bar": "堆叠水平柱状图 (Stacked Horizontal Bar)",
    "waterfall": "瀑布图 (Waterfall)",
    "square_area": "方形面积图 (Square Area)",
}

CHARTS_TO_AVOID = ("pie", "donut", "3d", "secondary_y_axis")

AVOID_LABELS: Dict[str, str] = {
    "pie": "饼图 — 人眼难以比较角度和面积",
    "donut": "甜甜圈图 — 比较弧长更困难",
    "3d": "3D — 扭曲数值，永远不要使用",
    "secondary_y_axis": "双Y轴 — 难以判断数据对应哪个轴",
}

# ── 数据类型 ──
DATA_TYPES = ("single_number", "few_numbers", "categorical", "continuous", "relationship", "part_of_whole")

# ── 前注意属性 ──
PREATTENTIVE_ATTRIBUTES = (
    "orientation", "shape", "line_length", "line_width",
    "size", "curvature", "added_marks", "enclosure",
    "hue", "intensity", "spatial_position", "motion",
)

QUANTITATIVE_ATTRIBUTES = ("line_length", "spatial_position", "line_width", "size", "intensity")
CATEGORICAL_ATTRIBUTES = ("hue", "shape", "orientation", "enclosure")

# ── 格式塔原则 ──
GESTALT_PRINCIPLES = (
    "proximity", "similarity", "enclosure", "closure", "continuity", "connection",
)

GESTALT_LABELS: Dict[str, str] = {
    "proximity": "邻近性 — 物理靠近的对象被视为一组",
    "similarity": "相似性 — 相同颜色/形状/大小的对象被视为相关",
    "enclosure": "封闭性 — 被围起来的对象被视为一组",
    "closure": "闭合性 — 不完整元素被感知为完整形状",
    "continuity": "连续性 — 眼睛寻找最平滑路径",
    "connection": "连接性 — 物理连接的对象被视为一组",
}

# ── 杂乱元素 ──
CLUTTER_ELEMENTS = (
    "chart_border", "gridlines", "data_markers", "trailing_zeros",
    "diagonal_text", "legend_separate", "redundant_labels",
    "background_shading", "tick_marks", "3d_effects",
)

CLUTTER_LABELS: Dict[str, str] = {
    "chart_border": "图表边框 — 通常不必要（闭合性原则）",
    "gridlines": "网格线 — 如需保留则用浅灰色细线",
    "data_markers": "数据标记 — 除非有目的否则移除",
    "trailing_zeros": "尾部零 — 增加复杂感无信息价值",
    "diagonal_text": "对角文本 — 阅读速度慢52%",
    "legend_separate": "独立图例 — 应直接标注数据",
    "redundant_labels": "冗余标签 — 同一信息重复出现",
    "background_shading": "背景阴影 — 分散注意力",
    "tick_marks": "刻度线 — 通常可简化",
    "3d_effects": "3D效果 — 永远不要使用",
}

# ── 诊断维度 ──
DIAGNOSIS_DIMENSIONS = (
    "context", "visual_choice", "clutter", "attention", "design_narrative",
)

DIAGNOSIS_LABELS: Dict[str, str] = {
    "context": "上下文评估",
    "visual_choice": "视觉选择评估",
    "clutter": "杂乱评估",
    "attention": "注意力引导评估",
    "design_narrative": "设计与叙事评估",
}

# ── 故事结构 ──
STORY_ACTS = ("beginning", "middle", "end")

STORY_LABELS: Dict[str, str] = {
    "beginning": "开始 — 设置背景、主角、不平衡",
    "middle": "中间 — 数据证据、说服行动",
    "end": "结尾 — 行动号召",
}

NARRATIVE_FLOWS = ("chronological", "lead_with_ending")

# ── 颜色策略 ──
COLOR_STRATEGIES = ("grey_plus_one", "sequential", "diverging", "categorical_limited")

COLOR_LABELS: Dict[str, str] = {
    "grey_plus_one": "灰色基底+单一强调色（推荐）",
    "sequential": "单色渐变（适合热力图/排名）",
    "diverging": "双色分歧（适合正负对比）",
    "categorical_limited": "有限分类色（最多4-5种）",
}


@dataclass
class AnalysisConfig:
    """分析任务的运行时配置"""
    include_dimensions: List[str] = field(
        default_factory=lambda: list(DIAGNOSIS_DIMENSIONS))
    output_format: str = "markdown"
    language: str = "zh"
    color_strategy: str = "grey_plus_one"
    max_clutter_items: int = 10

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        for d in self.include_dimensions:
            if d not in DIAGNOSIS_DIMENSIONS:
                raise ValueError(f"未知诊断维度: {d}，可选: {DIAGNOSIS_DIMENSIONS}")
        if self.output_format not in ("markdown", "json", "text"):
            raise ValueError(f"未知输出格式: {self.output_format}")
        if self.color_strategy not in COLOR_STRATEGIES:
            raise ValueError(f"未知颜色策略: {self.color_strategy}")
