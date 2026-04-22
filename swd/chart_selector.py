"""SWD 图表选择决策器

基于数据特征自动推荐最佳图表类型，并给出设计要点。
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict

from .config import CHART_LABELS, CHARTS_TO_AVOID, AVOID_LABELS


@dataclass
class ChartRecommendation:
    """图表推荐结果"""
    chart_type: str
    label: str
    reason: str
    design_notes: List[str] = field(default_factory=list)
    priority: int = 1  # 1=首选, 2=备选


@dataclass
class DataProfile:
    """数据特征描述"""
    data_type: str = "categorical"          # categorical/continuous/relationship/single_number
    series_count: int = 1
    category_count: int = 0
    has_time_dimension: bool = False
    has_negative_values: bool = False
    show_part_of_whole: bool = False
    category_names_long: bool = False
    compare_two_points: bool = False
    show_start_end_changes: bool = False
    magnitude_difference_large: bool = False


class ChartSelector:
    """图表选择决策器 — 基于数据特征推荐最佳图表"""

    def __init__(self):
        self._profile: Optional[DataProfile] = None
        self._avoid_detected: List[str] = []

    def set_profile(self, **kwargs) -> "ChartSelector":
        self._profile = DataProfile(**kwargs)
        return self

    def check_avoid(self, proposed_chart: str) -> List[str]:
        """检查提议的图表类型是否应该避免"""
        warnings: List[str] = []
        key = proposed_chart.lower().replace(" ", "_")
        if key in CHARTS_TO_AVOID:
            warnings.append(f"⚠️ {AVOID_LABELS.get(key, proposed_chart)} — 建议使用替代方案")
        if key == "pie":
            warnings.append("替代方案: 水平柱状图（按大小排序）或直接展示数字")
        if key == "donut":
            warnings.append("替代方案: 水平柱状图 或 100%堆叠水平柱状图")
        if key == "3d":
            warnings.append("替代方案: 使用对应的2D版本")
        if key in ("secondary_y_axis", "dual_y"):
            warnings.append("替代方案1: 直接标注第二轴数据点")
            warnings.append("替代方案2: 垂直拆分为两个图，共享x轴")
        return warnings

    def recommend(self, profile: Optional[DataProfile] = None) -> List[ChartRecommendation]:
        """基于数据特征推荐图表类型"""
        p = profile or self._profile
        if not p:
            raise ValueError("请先通过 set_profile() 设置数据特征")

        recs: List[ChartRecommendation] = []

        # 单个/少量数字
        if p.data_type == "single_number" or (p.series_count <= 2 and p.category_count == 0):
            recs.append(ChartRecommendation(
                "simple_text", CHART_LABELS["simple_text"], "只有1-2个数字时，直接使用文本最有冲击力",
                ["配以少量支撑文字", "使用大字号突出关键数字", "可用颜色强调变化方向"], 1))
            return recs

        # 两个变量关系
        if p.data_type == "relationship":
            recs.append(ChartRecommendation(
                "scatterplot", CHART_LABELS["scatterplot"], "展示两个变量之间的关系",
                ["可添加参考线（如平均线）聚焦特定区域", "考虑标注关键数据点"], 1))
            return recs

        # 连续数据/时间序列
        if p.has_time_dimension or p.data_type == "continuous":
            if p.compare_two_points:
                recs.append(ChartRecommendation(
                    "slopegraph", CHART_LABELS["slopegraph"],
                    "两个时间点比较，同时展示绝对值和变化率",
                    ["线条重叠严重时可能不适用", "可用颜色强调单个系列"], 1))
            recs.append(ChartRecommendation(
                "line", CHART_LABELS["line"],
                "连续数据趋势展示的最佳选择",
                ["x轴时间间隔必须一致", "直接标注数据系列而非使用图例",
                 "预测数据用虚线区分", "避免超过4-5条线（意面图）"],
                1 if not p.compare_two_points else 2))
            return recs

        # 部分与整体
        if p.show_part_of_whole:
            recs.append(ChartRecommendation(
                "stacked_horizontal_bar", CHART_LABELS["stacked_horizontal_bar"],
                "100%形式适合展示部分与整体关系，左右两端有一致基线",
                ["适合Likert量表调查数据", "正面在右/负面在左"], 1))
            if p.magnitude_difference_large:
                recs.append(ChartRecommendation(
                    "square_area", CHART_LABELS["square_area"],
                    "数量级差异巨大时，方形面积图更紧凑",
                    ["通常应避免面积图，此为例外"], 2))
            return recs

        # 起点+增减+终点
        if p.show_start_end_changes:
            recs.append(ChartRecommendation(
                "waterfall", CHART_LABELS["waterfall"], "展示起点、增减和终点",
                ["可通过堆叠柱+隐形底部系列实现"], 1))
            return recs

        # 分类数据（默认）
        if p.category_names_long or p.category_count > 5:
            recs.append(ChartRecommendation(
                "horizontal_bar", CHART_LABELS["horizontal_bar"],
                "分类数据的首选图表，类别名从左到右书写极易阅读",
                ["类别排序要有逻辑：自然顺序或按数值大小",
                 "柱宽应大于柱间白色空间", "必须有零基线"], 1))
        else:
            recs.append(ChartRecommendation(
                "vertical_bar", CHART_LABELS["vertical_bar"],
                "类别名较短时可用垂直柱状图",
                ["必须有零基线", "多系列时注意分组间距"], 1))
            recs.append(ChartRecommendation(
                "horizontal_bar", CHART_LABELS["horizontal_bar"],
                "水平柱状图也是优秀的备选方案",
                ["类别名更易阅读", "符合Z型阅读模式"], 2))

        if p.series_count > 1 and p.category_count > 0:
            recs.append(ChartRecommendation(
                "stacked_vertical_bar", CHART_LABELS["stacked_vertical_bar"],
                "可展示总量和子组件，但用例有限",
                ["超过底部系列后难以比较（缺乏一致基线）", "谨慎使用"], 2))

        return recs

    @staticmethod
    def render_markdown(recs: List[ChartRecommendation],
                        avoid_warnings: Optional[List[str]] = None) -> str:
        lines = ["# 📊 图表选择建议\n"]

        primary = [r for r in recs if r.priority == 1]
        secondary = [r for r in recs if r.priority == 2]

        if primary:
            lines.append("## ✅ 推荐图表")
            for r in primary:
                lines.append(f"\n### {r.label}")
                lines.append(f"**推荐理由**: {r.reason}\n")
                if r.design_notes:
                    lines.append("**设计要点**:")
                    for n in r.design_notes:
                        lines.append(f"- {n}")

        if secondary:
            lines.append("\n## 🔄 备选图表")
            for r in secondary:
                lines.append(f"\n### {r.label}")
                lines.append(f"**理由**: {r.reason}\n")
                if r.design_notes:
                    for n in r.design_notes:
                        lines.append(f"- {n}")

        if avoid_warnings:
            lines.append("\n## ⛔ 避免使用")
            for w in avoid_warnings:
                lines.append(f"- {w}")

        return "\n".join(lines)
