"""SWD 去杂乱诊断器

基于格式塔原则和认知负荷理论，诊断可视化中的杂乱元素并给出去除建议。
"""

from dataclasses import dataclass, field
from typing import List, Dict

from .config import CLUTTER_ELEMENTS, CLUTTER_LABELS, GESTALT_PRINCIPLES, GESTALT_LABELS


@dataclass
class ClutterItem:
    """单个杂乱元素"""
    element_type: str
    description: str
    severity: int = 3          # 1-5
    recommendation: str = ""

    def validate(self) -> List[str]:
        issues: List[str] = []
        if self.element_type not in CLUTTER_ELEMENTS:
            issues.append(f"未知杂乱元素: {self.element_type}，可选: {CLUTTER_ELEMENTS}")
        if not 1 <= self.severity <= 5:
            issues.append(f"严重度 {self.severity} 超出范围 1-5")
        return issues


@dataclass
class GestaltApplication:
    """格式塔原则应用建议"""
    principle: str
    current_issue: str
    suggestion: str

    def validate(self) -> List[str]:
        issues: List[str] = []
        if self.principle not in GESTALT_PRINCIPLES:
            issues.append(f"未知格式塔原则: {self.principle}，可选: {GESTALT_PRINCIPLES}")
        return issues


@dataclass
class DeclutterReport:
    """去杂乱诊断报告"""
    clutter_items: List[ClutterItem] = field(default_factory=list)
    gestalt_apps: List[GestaltApplication] = field(default_factory=list)
    alignment_issues: List[str] = field(default_factory=list)
    whitespace_issues: List[str] = field(default_factory=list)
    contrast_issues: List[str] = field(default_factory=list)


class DeclutterAnalyzer:
    """去杂乱诊断器 — 识别并建议去除可视化中的杂乱元素"""

    DECLUTTER_STEPS = [
        ("移除图表边框", "chart_border", "利用闭合性原则，用白色空间替代边框"),
        ("移除或弱化网格线", "gridlines", "如需保留则用浅灰色细线，不要与数据竞争"),
        ("移除不必要的数据标记", "data_markers", "除非有目的，否则线条本身已表达数据"),
        ("清理轴标签", "trailing_zeros", "去掉尾部零、缩写月份、消除对角文本"),
        ("直接标注数据", "legend_separate", "消除图例来回查看的工作，利用邻近性原则"),
        ("使用一致颜色", "redundant_labels", "标签颜色与数据颜色匹配，利用相似性原则"),
    ]

    def __init__(self):
        self._report = DeclutterReport()

    def add_clutter(self, element_type: str, description: str,
                    severity: int = 3, recommendation: str = "") -> "DeclutterAnalyzer":
        if not recommendation:
            recommendation = CLUTTER_LABELS.get(element_type, "建议移除")
        item = ClutterItem(element_type=element_type, description=description,
                           severity=severity, recommendation=recommendation)
        self._report.clutter_items.append(item)
        return self

    def add_gestalt(self, principle: str, current_issue: str,
                    suggestion: str) -> "DeclutterAnalyzer":
        self._report.gestalt_apps.append(
            GestaltApplication(principle=principle, current_issue=current_issue,
                               suggestion=suggestion))
        return self

    def add_alignment_issue(self, issue: str) -> "DeclutterAnalyzer":
        self._report.alignment_issues.append(issue)
        return self

    def add_whitespace_issue(self, issue: str) -> "DeclutterAnalyzer":
        self._report.whitespace_issues.append(issue)
        return self

    def add_contrast_issue(self, issue: str) -> "DeclutterAnalyzer":
        self._report.contrast_issues.append(issue)
        return self

    def auto_detect(self, has_border: bool = False, has_gridlines: bool = False,
                    has_data_markers: bool = False, has_trailing_zeros: bool = False,
                    has_diagonal_text: bool = False, has_separate_legend: bool = False,
                    has_3d: bool = False, has_background_shading: bool = False,
                    ) -> "DeclutterAnalyzer":
        """自动检测常见杂乱元素"""
        checks = [
            (has_border, "chart_border", "检测到图表边框", 2),
            (has_gridlines, "gridlines", "检测到网格线", 2),
            (has_data_markers, "data_markers", "检测到数据标记", 2),
            (has_trailing_zeros, "trailing_zeros", "检测到尾部零（如250.00）", 3),
            (has_diagonal_text, "diagonal_text", "检测到对角文本", 4),
            (has_separate_legend, "legend_separate", "检测到独立图例", 3),
            (has_3d, "3d_effects", "检测到3D效果", 5),
            (has_background_shading, "background_shading", "检测到背景阴影", 2),
        ]
        for flag, etype, desc, sev in checks:
            if flag:
                self.add_clutter(etype, desc, sev)
        return self

    def build(self) -> DeclutterReport:
        return self._report

    def total_cognitive_load(self) -> int:
        """估算总认知负荷分数"""
        return sum(item.severity for item in self._report.clutter_items)

    def reduction_estimate(self) -> int:
        """估算去杂乱后可减少的认知负荷百分比"""
        total = self.total_cognitive_load()
        if total == 0:
            return 0
        return min(int(total / (total + 5) * 100), 90)

    @staticmethod
    def render_markdown(report: DeclutterReport) -> str:
        lines = ["# 🧹 去杂乱诊断报告\n"]

        total_load = sum(item.severity for item in report.clutter_items)
        lines.append(f"## 诊断摘要")
        lines.append(f"- **检测到的杂乱元素**: {len(report.clutter_items)} 项")
        lines.append(f"- **总认知负荷分数**: {total_load}")
        lines.append("")

        if report.clutter_items:
            lines.append("## 杂乱元素清单\n")
            lines.append("| 元素 | 描述 | 严重度 | 建议 |")
            lines.append("|------|------|--------|------|")
            for item in sorted(report.clutter_items, key=lambda x: -x.severity):
                bar = "█" * item.severity + "░" * (5 - item.severity)
                lines.append(f"| {item.element_type} | {item.description} | {bar} | {item.recommendation} |")

        lines.append("\n## 去杂乱六步骤\n")
        for i, (step, etype, detail) in enumerate(DeclutterAnalyzer.DECLUTTER_STEPS, 1):
            detected = any(c.element_type == etype for c in report.clutter_items)
            icon = "🔴" if detected else "🟢"
            lines.append(f"{i}. {icon} **{step}** — {detail}")

        if report.gestalt_apps:
            lines.append("\n## 格式塔原则应用建议\n")
            for g in report.gestalt_apps:
                label = GESTALT_LABELS.get(g.principle, g.principle)
                lines.append(f"### {label}")
                lines.append(f"- **当前问题**: {g.current_issue}")
                lines.append(f"- **建议**: {g.suggestion}\n")

        if report.alignment_issues:
            lines.append("## 对齐问题\n")
            for a in report.alignment_issues:
                lines.append(f"- ❌ {a}")

        if report.whitespace_issues:
            lines.append("\n## 白色空间问题\n")
            for w in report.whitespace_issues:
                lines.append(f"- ❌ {w}")

        if report.contrast_issues:
            lines.append("\n## 对比问题\n")
            for c in report.contrast_issues:
                lines.append(f"- ❌ {c}")

        return "\n".join(lines)
