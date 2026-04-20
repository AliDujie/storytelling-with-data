"""SWD 注意力引导分析器

基于前注意属性和颜色策略，分析和规划视觉焦点引导方案。
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict

from .config import (
    PREATTENTIVE_ATTRIBUTES, QUANTITATIVE_ATTRIBUTES,
    CATEGORICAL_ATTRIBUTES, COLOR_STRATEGIES, COLOR_LABELS,
)


@dataclass
class FocusPoint:
    """视觉焦点"""
    element: str
    importance: int = 3          # 1-5
    current_emphasis: int = 1    # 1-5 当前被强调程度
    desired_emphasis: int = 5    # 1-5 期望被强调程度
    attributes_used: List[str] = field(default_factory=list)

    @property
    def emphasis_gap(self) -> int:
        return self.desired_emphasis - self.current_emphasis


@dataclass
class ColorPlan:
    """颜色方案"""
    strategy: str = "grey_plus_one"
    base_color: str = "灰色 (#808080)"
    accent_color: str = "蓝色 (#4472C4)"
    negative_color: str = "橙色 (#ED7D31)"
    notes: List[str] = field(default_factory=list)
    colorblind_safe: bool = True


@dataclass
class VisualHierarchyLevel:
    """视觉层次级别"""
    level: int
    elements: List[str] = field(default_factory=list)
    treatment: str = ""


@dataclass
class AttentionPlan:
    """注意力引导方案"""
    focus_points: List[FocusPoint] = field(default_factory=list)
    color_plan: ColorPlan = field(default_factory=ColorPlan)
    hierarchy: List[VisualHierarchyLevel] = field(default_factory=list)
    preattentive_suggestions: List[str] = field(default_factory=list)


class AttentionAnalyzer:
    """注意力引导分析器 — 规划前注意属性和颜色策略"""

    def __init__(self):
        self._plan = AttentionPlan()

    def add_focus(self, element: str, importance: int = 3,
                  current_emphasis: int = 1,
                  desired_emphasis: int = 5) -> "AttentionAnalyzer":
        self._plan.focus_points.append(FocusPoint(
            element=element, importance=importance,
            current_emphasis=current_emphasis,
            desired_emphasis=desired_emphasis))
        return self

    def set_color_plan(self, strategy: str = "grey_plus_one",
                       accent: str = "蓝色 (#4472C4)",
                       negative: str = "橙色 (#ED7D31)",
                       colorblind_safe: bool = True) -> "AttentionAnalyzer":
        self._plan.color_plan = ColorPlan(
            strategy=strategy, accent_color=accent,
            negative_color=negative, colorblind_safe=colorblind_safe)
        return self

    def add_hierarchy_level(self, level: int, elements: List[str],
                            treatment: str) -> "AttentionAnalyzer":
        self._plan.hierarchy.append(VisualHierarchyLevel(
            level=level, elements=elements, treatment=treatment))
        return self

    def auto_suggest(self) -> "AttentionAnalyzer":
        """基于焦点分析自动生成前注意属性建议"""
        suggestions: List[str] = []
        high_gap = [f for f in self._plan.focus_points if f.emphasis_gap >= 3]
        mid_gap = [f for f in self._plan.focus_points if 1 <= f.emphasis_gap < 3]

        if high_gap:
            suggestions.append("高优先级焦点建议叠加多个前注意属性：颜色 + 大小 + 粗体")
            suggestions.append("先将所有元素推到背景（灰色），再用颜色突出焦点")
        if mid_gap:
            suggestions.append("中优先级焦点可使用单个前注意属性：颜色或粗体")

        total_focus = len(self._plan.focus_points)
        if total_focus > 3:
            suggestions.append(f"⚠️ 当前有{total_focus}个焦点，建议减少到1-3个以保持有效性")
            suggestions.append("前注意属性稀疏使用时最有效——突出越多，效果越弱")

        suggestions.append("使用'眼睛首先看向哪里'测试验证效果")
        suggestions.append("颜色变化=内容变化，不要为新颖而变色")

        self._plan.preattentive_suggestions = suggestions
        return self

    def diagnose_eyes_drawn(self) -> List[str]:
        """执行'眼睛首先看向哪里'诊断"""
        insights: List[str] = []
        sorted_points = sorted(self._plan.focus_points,
                               key=lambda x: -x.current_emphasis)

        if sorted_points:
            top = sorted_points[0]
            most_important = max(self._plan.focus_points, key=lambda x: x.importance)
            if top.element != most_important.element:
                insights.append(
                    f"⚠️ 当前最突出的元素是'{top.element}'，"
                    f"但最重要的元素是'{most_important.element}'——需要调整视觉权重")
            else:
                insights.append(f"✅ 最突出的元素'{top.element}'与最重要的元素一致")

        high_emphasis_count = sum(1 for f in self._plan.focus_points
                                 if f.current_emphasis >= 4)
        if high_emphasis_count > 2:
            insights.append(
                f"⚠️ 有{high_emphasis_count}个元素被高度强调——"
                "太多突出等于没有突出（鸽群中找老鹰原理）")

        return insights

    def build(self) -> AttentionPlan:
        if not self._plan.preattentive_suggestions:
            self.auto_suggest()
        return self._plan

    @staticmethod
    def render_markdown(plan: AttentionPlan) -> str:
        lines = ["# 🎯 注意力引导分析\n"]

        if plan.focus_points:
            lines.append("## 焦点分析\n")
            lines.append("| 元素 | 重要性 | 当前强调 | 期望强调 | 差距 |")
            lines.append("|------|--------|---------|---------|------|")
            for f in sorted(plan.focus_points, key=lambda x: -x.importance):
                imp = "█" * f.importance + "░" * (5 - f.importance)
                cur = "█" * f.current_emphasis + "░" * (5 - f.current_emphasis)
                des = "█" * f.desired_emphasis + "░" * (5 - f.desired_emphasis)
                gap = f.emphasis_gap
                icon = "🔴" if gap >= 3 else "🟡" if gap >= 1 else "🟢"
                lines.append(f"| {f.element} | {imp} | {cur} | {des} | {icon} {gap} |")

        cp = plan.color_plan
        lines.append(f"\n## 颜色策略\n")
        lines.append(f"- **策略**: {COLOR_LABELS.get(cp.strategy, cp.strategy)}")
        lines.append(f"- **基色**: {cp.base_color}")
        lines.append(f"- **强调色**: {cp.accent_color}")
        lines.append(f"- **负面色**: {cp.negative_color}")
        lines.append(f"- **色盲友好**: {'✅ 是' if cp.colorblind_safe else '❌ 否'}")
        for n in cp.notes:
            lines.append(f"- {n}")

        if plan.hierarchy:
            lines.append("\n## 视觉层次设计\n")
            for h in sorted(plan.hierarchy, key=lambda x: x.level):
                elements = ", ".join(h.elements)
                lines.append(f"**Level {h.level}**: {elements}")
                lines.append(f"  处理方式: {h.treatment}\n")

        if plan.preattentive_suggestions:
            lines.append("## 前注意属性建议\n")
            for s in plan.preattentive_suggestions:
                lines.append(f"- {s}")

        return "\n".join(lines)
