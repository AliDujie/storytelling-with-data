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

__version__ = "1.0.0"

from .config import AnalysisConfig, CHART_TYPES, CHART_LABELS, KNOWLEDGE_FILES
from .utils import load_knowledge, load_all_knowledge, search_knowledge
from .context import ContextBuilder, ContextAnalysis, AudienceProfile, BigIdea
from .chart_selector import ChartSelector, DataProfile, ChartRecommendation
from .declutter import DeclutterAnalyzer, DeclutterReport, ClutterItem, GestaltApplication
from .attention import AttentionAnalyzer, AttentionPlan, FocusPoint, ColorPlan
from .designer import DesignEvaluator, DesignAssessment
from .storyteller import StoryBuilder, DataStory, BingBangBongo, SlideTitle
from .diagnosis import DiagnosisEngine, DiagnosisResult
from .makeover import MakeoverEngine, MakeoverPlan, MakeoverStep, DesignSpec

from typing import Dict, List, Optional, Tuple


class SWDSkill:
    """SWD 统一入口类 — 封装全部 8 大执行能力

    用法::

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

    def __init__(self, project_name: str, config: Optional[AnalysisConfig] = None):
        self.project = project_name
        self.config = config or AnalysisConfig()

    # ── 能力1: 上下文分析 ──

    def build_context(self, audience: str, cta: str,
                      decision_maker: str = "",
                      knowledge_level: str = "general",
                      relationship: str = "first_contact",
                      mechanism: str = "live_presentation",
                      tone: str = "neutral",
                      three_min_story: str = "",
                      big_idea: str = "",
                      big_idea_point: str = "",
                      big_idea_stakes: str = "",
                      supporting_data: Optional[List[str]] = None,
                      risks: Optional[List[str]] = None) -> str:
        """构建上下文分析报告"""
        builder = ContextBuilder(self.project)
        builder.set_audience(audience, decision_maker, knowledge_level, relationship)
        builder.set_mechanism(mechanism, tone)
        if three_min_story:
            builder.set_three_min_story(three_min_story)
        if big_idea:
            builder.set_big_idea(big_idea_point or "", big_idea_stakes or "", big_idea)
        builder.set_call_to_action(cta)
        for d in (supporting_data or []):
            builder.add_supporting_data(d)
        for r in (risks or []):
            builder.add_risk(r)
        return ContextBuilder.render_markdown(builder.build())

    # ── 能力2: 图表选择 ──

    def recommend_chart(self, data_type: str = "categorical",
                        series_count: int = 1, category_count: int = 0,
                        has_time: bool = False, has_negative: bool = False,
                        show_part_of_whole: bool = False,
                        category_names_long: bool = False,
                        compare_two_points: bool = False,
                        show_start_end_changes: bool = False,
                        proposed_chart: str = "") -> str:
        """推荐最佳图表类型"""
        selector = ChartSelector()
        selector.set_profile(
            data_type=data_type, series_count=series_count,
            category_count=category_count, has_time_dimension=has_time,
            has_negative_values=has_negative, show_part_of_whole=show_part_of_whole,
            category_names_long=category_names_long,
            compare_two_points=compare_two_points,
            show_start_end_changes=show_start_end_changes)
        recs = selector.recommend()
        avoid = selector.check_avoid(proposed_chart) if proposed_chart else None
        return ChartSelector.render_markdown(recs, avoid)

    # ── 能力3: 去杂乱诊断 ──

    def diagnose_clutter(self, has_border: bool = False,
                         has_gridlines: bool = False,
                         has_data_markers: bool = False,
                         has_trailing_zeros: bool = False,
                         has_diagonal_text: bool = False,
                         has_separate_legend: bool = False,
                         has_3d: bool = False,
                         has_background_shading: bool = False,
                         gestalt_issues: Optional[List[Tuple[str, str, str]]] = None,
                         alignment_issues: Optional[List[str]] = None,
                         whitespace_issues: Optional[List[str]] = None,
                         ) -> str:
        """诊断可视化中的杂乱元素"""
        analyzer = DeclutterAnalyzer()
        analyzer.auto_detect(
            has_border=has_border, has_gridlines=has_gridlines,
            has_data_markers=has_data_markers, has_trailing_zeros=has_trailing_zeros,
            has_diagonal_text=has_diagonal_text, has_separate_legend=has_separate_legend,
            has_3d=has_3d, has_background_shading=has_background_shading)
        for principle, issue, suggestion in (gestalt_issues or []):
            analyzer.add_gestalt(principle, issue, suggestion)
        for a in (alignment_issues or []):
            analyzer.add_alignment_issue(a)
        for w in (whitespace_issues or []):
            analyzer.add_whitespace_issue(w)
        return DeclutterAnalyzer.render_markdown(analyzer.build())

    # ── 能力4: 注意力引导 ──

    def plan_attention(self, focus_elements: Optional[List[Tuple[str, int]]] = None,
                       color_strategy: str = "grey_plus_one",
                       accent_color: str = "蓝色 (#4472C4)",
                       hierarchy: Optional[List[Tuple[int, List[str], str]]] = None,
                       ) -> str:
        """规划注意力引导方案"""
        analyzer = AttentionAnalyzer()
        for name, importance in (focus_elements or []):
            analyzer.add_focus(name, importance=importance)
        analyzer.set_color_plan(strategy=color_strategy, accent=accent_color)
        for level, elements, treatment in (hierarchy or []):
            analyzer.add_hierarchy_level(level, elements, treatment)
        analyzer.auto_suggest()
        plan = analyzer.build()
        result = AttentionAnalyzer.render_markdown(plan)
        eyes = analyzer.diagnose_eyes_drawn()
        if eyes:
            result += "\n\n## '眼睛首先看向哪里'诊断\n"
            result += "\n".join(f"- {e}" for e in eyes)
        return result

    # ── 能力5: 设计评估 ──

    def evaluate_design(self, has_title: bool = False,
                        has_axis_titles: bool = False,
                        has_action_title: bool = False,
                        has_annotations: bool = False,
                        color_strategic: bool = False,
                        alignment_clean: bool = False,
                        whitespace_ok: bool = False,
                        hierarchy_clear: bool = False,
                        highlight_limited: bool = False,
                        distractions_removed: bool = False,
                        ) -> str:
        """评估数据可视化设计质量"""
        evaluator = DesignEvaluator()
        evaluator.auto_evaluate(
            has_title=has_title, has_axis_titles=has_axis_titles,
            has_action_title=has_action_title, has_annotations=has_annotations,
            color_strategic=color_strategic, alignment_clean=alignment_clean,
            whitespace_ok=whitespace_ok, hierarchy_clear=hierarchy_clear,
            highlight_limited=highlight_limited,
            distractions_removed=distractions_removed)
        evaluator.auto_improvements()
        return DesignEvaluator.render_markdown(evaluator.build())

    # ── 能力6: 故事构建 ──

    def build_story(self, protagonist: str, imbalance: str,
                    setting: str = "", desired_balance: str = "",
                    evidence: Optional[List[str]] = None,
                    call_to_action: str = "",
                    narrative_flow: str = "chronological",
                    delivery_mode: str = "live_presentation",
                    slide_titles: Optional[List[str]] = None,
                    bing: str = "", bang: str = "", bongo: str = "",
                    ) -> str:
        """构建完整的数据故事"""
        builder = StoryBuilder(self.project)
        builder.set_narrative_flow(narrative_flow, delivery_mode)
        builder.set_setup(setting or f"{self.project}项目背景",
                          protagonist, imbalance, desired_balance)
        for e in (evidence or []):
            builder.add_evidence(e)
        if call_to_action:
            builder.set_end(call_to_action)
        if bing or bang or bongo:
            builder.set_bing_bang_bongo(bing, bang, bongo)
        for t in (slide_titles or []):
            builder.add_slide_title(t)
        story = builder.build()
        result = StoryBuilder.render_markdown(story)
        h_issues = builder.check_horizontal_logic()
        if h_issues:
            result += "\n\n## 水平逻辑检查\n"
            result += "\n".join(f"- ⚠️ {i}" for i in h_issues)
        return result

    # ── 能力7: 综合诊断 ──

    def full_diagnosis(self, scores: Optional[Dict[str, Dict[str, int]]] = None,
                       ) -> str:
        """五维度100分制综合诊断"""
        engine = DiagnosisEngine(self.project)
        if scores:
            engine.auto_score(scores)
        engine.auto_improvements()
        return DiagnosisEngine.render_markdown(engine.build())

    # ── 能力8: 图表改造 ──

    def makeover(self, issues: Optional[List[str]] = None,
                 chart_type: str = "", title: str = "",
                 color_accent: str = "蓝色",
                 narrative_slides: Optional[List[Tuple[str, str]]] = None,
                 ) -> str:
        """从原始图表到数据故事的完整改造"""
        engine = MakeoverEngine(self.project)
        for issue in (issues or []):
            engine.add_issue(issue)
        engine.auto_steps_from_issues()
        if chart_type or title:
            engine.set_design_spec(chart_type=chart_type, title=title,
                                   color_accent=color_accent)
        for headline, voiceover in (narrative_slides or []):
            engine.add_narrative_slide(headline, voiceover=voiceover)
        return MakeoverEngine.render_markdown(engine.build())

    # ── 知识库搜索 ──

    def search_knowledge(self, keyword: str) -> Dict[str, List[str]]:
        """在知识库中搜索关键词"""
        return search_knowledge(keyword)


__all__ = [
    "SWDSkill",
    "AnalysisConfig", "CHART_TYPES", "CHART_LABELS", "KNOWLEDGE_FILES",
    "load_knowledge", "load_all_knowledge", "search_knowledge",
    "ContextBuilder", "ContextAnalysis", "AudienceProfile", "BigIdea",
    "ChartSelector", "DataProfile", "ChartRecommendation",
    "DeclutterAnalyzer", "DeclutterReport", "ClutterItem", "GestaltApplication",
    "AttentionAnalyzer", "AttentionPlan", "FocusPoint", "ColorPlan",
    "DesignEvaluator", "DesignAssessment",
    "StoryBuilder", "DataStory", "BingBangBongo", "SlideTitle",
    "DiagnosisEngine", "DiagnosisResult",
    "MakeoverEngine", "MakeoverPlan", "MakeoverStep", "DesignSpec",
]
