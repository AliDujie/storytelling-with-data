"""Storytelling with Data (SWD) Python Toolkit

基于 Cole Nussbaumer Knaflic《Storytelling with Data》的完整数据可视化工具包。
覆盖 SWD 六课体系的 8 大执行能力。

快速开始::

    from swd import SWDSkill
    skill = SWDSkill("季度业绩汇报")

    # 能力1: 上下文分析
    ctx = skill.build_context(audience="产品VP", cta="批准新功能投入")

    # 能力2: 图表选择
    rec = skill.recommend_chart(data_type="continuous", has_time=True)

    # 能力3: 去杂乱诊断
    clutter = skill.diagnose_clutter(has_border=True, has_gridlines=True)

    # 能力4: 注意力引导
    attn = skill.plan_attention(focus_elements=[("关键指标", 5)])

    # 能力5: 设计评估
    design = skill.evaluate_design(has_title=True, color_strategic=False)

    # 能力6: 故事构建
    story = skill.build_story(protagonist="产品团队", imbalance="用户流失加剧")

    # 能力7: 综合诊断
    diag = skill.full_diagnosis(scores={"context": {"audience_clear": 4}})

    # 能力8: 图表改造
    makeover = skill.makeover(issues=["使用了饼图", "无标题"])
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from swd.context import ContextBuilder
from swd.chart_selector import ChartSelector, DataProfile
from swd.declutter import DeclutterAnalyzer
from swd.attention import AttentionAnalyzer
from swd.storyteller import StoryBuilder
from swd.diagnosis import DiagnosisEngine
from swd.makeover import MakeoverEngine
from swd.designer import DesignEvaluator

__version__ = "2.2.150"

__all__ = ["SWDSkill", "__version__"]


class SWDSkill:
    """Facade / 门面类 — 统一入口聚合 SWD 全部 8 项执行能力。

    Every method is a thin wrapper around the underlying module class,
    keeping the public API identical to what the README and examples expect.
    Extra **kwargs are silently ignored for forward compatibility.
    """

    def __init__(self, title: str) -> None:
        self.title = title

    # ── 能力 1: 上下文分析 / Context Analysis ──
    def build_context(
        self,
        audience: str = "",
        cta: str = "",
        big_idea: str = "",
        three_min_story: str = "",
        mechanism: str = "",
        supporting_data: Optional[List[str]] = None,
        risks: Optional[List[str]] = None,
        **_kwargs: Any,
    ) -> str:
        """构建故事上下文 (上下文分析)。"""
        ctx = ContextBuilder(self.title)
        if audience:
            ctx.set_audience(audience)
        if cta:
            ctx.set_call_to_action(cta)
        if big_idea:
            ctx.set_big_idea(big_idea, stakes=big_idea, full_sentence=big_idea)
        if three_min_story:
            ctx.set_three_min_story(three_min_story)
        if mechanism:
            ctx.set_mechanism(mechanism)
        if supporting_data:
            for d in supporting_data:
                ctx.add_supporting_data(d)
        if risks:
            for r in risks:
                ctx.add_risk(r)
        return ContextBuilder.render_markdown(ctx.build())

    # ── 能力 2: 图表选择 / Chart Selection ──
    def recommend_chart(
        self,
        data_type: str = "",
        has_time: bool = False,
        series_count: int = 0,
        category_count: int = 0,
        comparison_type: str = "",
        show_part_of_whole: bool = False,
        **_kwargs: Any,
    ) -> str:
        """推荐合适的图表类型。"""
        cs = ChartSelector()
        profile = DataProfile(
            data_type=data_type or "categorical",
            series_count=series_count,
            category_count=category_count,
            has_time_dimension=has_time,
            show_part_of_whole=show_part_of_whole,
        )
        if comparison_type:
            profile.comparison_type = comparison_type  # type: ignore[attr-defined]
        recs = cs.recommend(profile)
        if not recs:
            return "No recommendation available."
        lines = []
        for r in recs:
            label = "⭐" if r.priority == 1 else "  "
            lines.append(f"{label} **{r.chart_type}** ({r.label})")
            lines.append(f"   {r.reason}")
            for note in r.design_notes:
                lines.append(f"   - {note}")
            lines.append("")
        return "\n".join(lines)

    # ── 能力 3: 去杂乱诊断 / Declutter Diagnosis ──
    def diagnose_clutter(
        self,
        has_gridlines: bool = False,
        has_border: bool = False,
        has_separate_legend: bool = False,
        has_3d: bool = False,
        has_background: bool = False,
        **_kwargs: Any,
    ) -> str:
        """诊断图表中的视觉杂乱并给出清理建议。"""
        da = DeclutterAnalyzer()
        da.auto_detect(
            has_gridlines=has_gridlines,
            has_border=has_border,
            has_separate_legend=has_separate_legend,
            has_3d=has_3d,
            has_background_shading=has_background,
        )
        return DeclutterAnalyzer.render_markdown(da.build())

    # ── 能力 4: 注意力引导 / Attention Guidance ──
    def plan_attention(
        self,
        focus_elements: Optional[List[tuple]] = None,
        color_plan: str = "",
        preattentive: bool = True,
        **_kwargs: Any,
    ) -> str:
        """规划视觉层次和注意力引导。"""
        aa = AttentionAnalyzer()
        if focus_elements:
            for element, priority in focus_elements:
                aa.add_focus(str(element), priority)
        if preattentive:
            aa.auto_suggest()
        return AttentionAnalyzer.render_markdown(aa.build())

    # ── 能力 5: 设计评估 / Design Evaluation ──
    def evaluate_design(
        self,
        has_title: bool = False,
        color_strategic: bool = False,
        has_labels: bool = False,
        clutter_free: bool = False,
        narrative_flow: bool = False,
        **_kwargs: Any,
    ) -> str:
        """三维度设计评估（可供性 / 无障碍 / 美学）。"""
        de = DesignEvaluator()
        de.auto_evaluate(
            has_action_title=has_title,
            color_strategic=color_strategic,
            highlight_limited=narrative_flow,
            distractions_removed=clutter_free,
        )
        return DesignEvaluator.render_markdown(de.build())

    # ── 能力 6: 故事构建 / Story Building ──
    def build_story(
        self,
        protagonist: str = "",
        imbalance: str = "",
        evidence: Optional[List[str]] = None,
        cta: str = "",
        call_to_action: str = "",
        desired_balance: str = "",
        narrative_flow: str = "freight-train",
        comparison: Optional[Dict[str, Any]] = None,
        **_kwargs: Any,
    ) -> str:
        """构建三幕式数据故事。"""
        sb = StoryBuilder(self.title)
        effective_balance = desired_balance or cta or call_to_action
        if protagonist or imbalance:
            sb.set_setup(
                setting=self.title,
                protagonist=protagonist,
                imbalance=imbalance,
                desired_balance=effective_balance,
            )
        if effective_balance:
            sb.set_recommendation(effective_balance)
        if narrative_flow:
            sb.set_narrative_flow(narrative_flow)
        if evidence:
            for e in evidence:
                sb.add_evidence(e)
        if comparison:
            sb.add_comparison(
                comparison.get("title", ""),
                comparison.get("option_a", ""),
                comparison.get("option_b", ""),
            )
        return StoryBuilder.render_markdown(sb.build())

    # ── 能力 7: 综合诊断 / Full Diagnosis ──
    def full_diagnosis(
        self,
        scores: Optional[Dict[str, Dict[str, int]]] = None,
        **_kwargs: Any,
    ) -> str:
        """五维度 100 分制综合诊断。"""
        de = DiagnosisEngine()
        if scores:
            for dimension, items in scores.items():
                for item_key, score in items.items():
                    de.score(dimension, item_key, score)
            de.auto_improvements()
        return DiagnosisEngine.render_markdown(de.build())

    # ── 能力 8: 图表改造 / Chart Makeover ──
    def makeover(
        self,
        issues: Optional[List[str]] = None,
        design_spec: str = "",
        **_kwargs: Any,
    ) -> str:
        """基于问题列表生成图表改造步骤。"""
        me = MakeoverEngine()
        if issues:
            for issue in issues:
                me.add_issue(issue)
            me.auto_steps_from_issues()
        if design_spec:
            me.set_design_spec(design_spec)
        return MakeoverEngine.render_markdown(me.build())

    # ── 便捷组合方法 / Convenience ──
    def build_decision_comparison(
        self,
        title: str = "方案对比",
        option_a: str = "方案 A",
        option_b: str = "方案 B",
        criteria: Optional[List[str]] = None,
        **_kwargs: Any,
    ) -> str:
        """构建决策方案对比。"""
        sb = StoryBuilder(self.title)
        sb.add_comparison(f"{title}: {option_a} vs {option_b}")
        if criteria:
            for c in criteria:
                sb.add_comparison(c)
        return StoryBuilder.render_markdown(sb.build())
