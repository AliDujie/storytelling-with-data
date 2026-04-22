"""SWD 设计评估器

基于可供性、可访问性、美学三维度评估数据可视化设计质量。
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class AffordanceCheck:
    """可供性检查项"""
    name: str
    passed: bool = False
    note: str = ""


@dataclass
class AccessibilityCheck:
    """可访问性检查项"""
    name: str
    passed: bool = False
    note: str = ""


@dataclass
class AestheticCheck:
    """美学检查项"""
    name: str
    passed: bool = False
    note: str = ""


@dataclass
class DesignAssessment:
    """设计评估结果"""
    affordances: List[AffordanceCheck] = field(default_factory=list)
    accessibility: List[AccessibilityCheck] = field(default_factory=list)
    aesthetics: List[AestheticCheck] = field(default_factory=list)
    improvements: List[str] = field(default_factory=list)

    @property
    def total_checks(self) -> int:
        return len(self.affordances) + len(self.accessibility) + len(self.aesthetics)

    @property
    def passed_checks(self) -> int:
        return (sum(1 for c in self.affordances if c.passed)
                + sum(1 for c in self.accessibility if c.passed)
                + sum(1 for c in self.aesthetics if c.passed))

    @property
    def score_pct(self) -> int:
        return int(self.passed_checks / self.total_checks * 100) if self.total_checks else 0


class DesignEvaluator:
    """设计评估器 — 三维度评估数据可视化设计质量"""

    AFFORDANCE_ITEMS = [
        ("highlight_important", "重要内容是否被突出（最多10%）"),
        ("distractions_removed", "干扰元素是否已消除"),
        ("visual_hierarchy", "是否建立了清晰的视觉层次"),
        ("data_stands_out", "数据是否比轴线/标签更突出"),
        ("preattentive_used", "是否策略性使用了前注意属性"),
    ]

    ACCESSIBILITY_ITEMS = [
        ("has_chart_title", "图表是否有标题"),
        ("has_axis_titles", "每个轴是否有标题"),
        ("action_title", "是否使用行动标题而非描述标题"),
        ("legible_font", "字体是否易读（字体和大小）"),
        ("simple_language", "是否使用简单语言"),
        ("annotations_present", "关键数据点是否有注释"),
        ("not_overcomplicated", "是否避免了过度复杂化"),
    ]

    AESTHETIC_ITEMS = [
        ("color_smart", "颜色使用是否有策略（稀疏+有意义）"),
        ("alignment_clean", "元素对齐是否创建了干净的线条"),
        ("whitespace_preserved", "白色空间是否恰当保留"),
        ("no_center_align", "是否避免了居中对齐文本"),
        ("consistent_sizing", "文字大小是否一致（除刻意强调外）"),
        ("professional_feel", "整体是否给人专业感"),
    ]

    def __init__(self):
        self._assessment = DesignAssessment()

    def check_affordance(self, item_key: str, passed: bool,
                         note: str = "") -> "DesignEvaluator":
        name = next((desc for k, desc in self.AFFORDANCE_ITEMS if k == item_key), item_key)
        self._assessment.affordances.append(AffordanceCheck(name=name, passed=passed, note=note))
        return self

    def check_accessibility(self, item_key: str, passed: bool,
                            note: str = "") -> "DesignEvaluator":
        name = next((desc for k, desc in self.ACCESSIBILITY_ITEMS if k == item_key), item_key)
        self._assessment.accessibility.append(AccessibilityCheck(name=name, passed=passed, note=note))
        return self

    def check_aesthetic(self, item_key: str, passed: bool,
                        note: str = "") -> "DesignEvaluator":
        name = next((desc for k, desc in self.AESTHETIC_ITEMS if k == item_key), item_key)
        self._assessment.aesthetics.append(AestheticCheck(name=name, passed=passed, note=note))
        return self

    def auto_evaluate(self, has_title: bool = False, has_axis_titles: bool = False,
                      has_action_title: bool = False, has_annotations: bool = False,
                      color_strategic: bool = False, alignment_clean: bool = False,
                      whitespace_ok: bool = False, hierarchy_clear: bool = False,
                      highlight_limited: bool = False, distractions_removed: bool = False,
                      legible_font: bool = True, simple_language: bool = True,
                      ) -> "DesignEvaluator":
        """自动评估常见设计要素"""
        self.check_affordance("highlight_important", highlight_limited)
        self.check_affordance("distractions_removed", distractions_removed)
        self.check_affordance("visual_hierarchy", hierarchy_clear)
        self.check_accessibility("has_chart_title", has_title)
        self.check_accessibility("has_axis_titles", has_axis_titles)
        self.check_accessibility("action_title", has_action_title)
        self.check_accessibility("legible_font", legible_font)
        self.check_accessibility("simple_language", simple_language)
        self.check_accessibility("annotations_present", has_annotations)
        self.check_aesthetic("color_smart", color_strategic)
        self.check_aesthetic("alignment_clean", alignment_clean)
        self.check_aesthetic("whitespace_preserved", whitespace_ok)
        return self

    def add_improvement(self, suggestion: str) -> "DesignEvaluator":
        self._assessment.improvements.append(suggestion)
        return self

    def auto_improvements(self) -> "DesignEvaluator":
        """基于评估结果自动生成改进建议"""
        for c in self._assessment.affordances:
            if not c.passed:
                self._assessment.improvements.append(f"[可供性] {c.name}")
        for c in self._assessment.accessibility:
            if not c.passed:
                self._assessment.improvements.append(f"[可访问性] {c.name}")
        for c in self._assessment.aesthetics:
            if not c.passed:
                self._assessment.improvements.append(f"[美学] {c.name}")
        return self

    def build(self) -> DesignAssessment:
        return self._assessment

    @staticmethod
    def _render_checks(checks: list, title: str) -> str:
        lines = [f"### {title}\n"]
        for c in checks:
            icon = "✅" if c.passed else "❌"
            line = f"- {icon} {c.name}"
            if c.note:
                line += f" — {c.note}"
            lines.append(line)
        passed = sum(1 for c in checks if c.passed)
        lines.append(f"\n通过: {passed}/{len(checks)}")
        return "\n".join(lines)

    @staticmethod
    def render_markdown(assessment: DesignAssessment) -> str:
        lines = ["# 🎨 设计评估报告\n"]
        pct = assessment.score_pct
        badge = "🟢 卓越" if pct >= 90 else "🟡 良好" if pct >= 70 else "🟠 需改进" if pct >= 50 else "🔴 需重做"
        lines.append(f"**总分: {assessment.passed_checks}/{assessment.total_checks} ({pct}%) {badge}**\n")

        if assessment.affordances:
            lines.append(DesignEvaluator._render_checks(assessment.affordances, "可供性 (Affordances)"))
        if assessment.accessibility:
            lines.append("\n" + DesignEvaluator._render_checks(assessment.accessibility, "可访问性 (Accessibility)"))
        if assessment.aesthetics:
            lines.append("\n" + DesignEvaluator._render_checks(assessment.aesthetics, "美学 (Aesthetics)"))

        if assessment.improvements:
            lines.append("\n## 改进建议\n")
            for i, imp in enumerate(assessment.improvements, 1):
                lines.append(f"{i}. {imp}")

        return "\n".join(lines)
