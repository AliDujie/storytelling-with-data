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

__version__ = "2.0.0"

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

    # ── CEO 视角方法 (3 个) ──

    def build_decision_comparison(self, options: Optional[List[Dict]] = None) -> str:
        """
        CEO 决策方法 1: 构建决策选项对比

        基于数据故事，为 CEO 提供清晰的决策选项对比，包括投入、风险、回报维度。

        Args:
            options: 决策选项列表，每项包含 name, investment, timeline, risk, return, confidence 等。
                     若不传入则使用通用默认值作为参考基线。

        Returns:
            Markdown 格式的决策对比报告

        Example::

            skill = SWDSkill("季度业绩汇报")
            options = [
                {"name": "方案 A: 快速上线", "investment": "低", "timeline": "2 周", "risk": "中", "return": "中"},
                {"name": "方案 B: 全面优化", "investment": "高", "timeline": "8 周", "risk": "低", "return": "高"},
            ]
            comparison = skill.build_decision_comparison(options)
        """
        default_options = [
            {"name": "方案 A: 保守策略", "investment": "低投入", "timeline": "短期见效", "risk": "低风险", "return": "中等回报", "confidence": "高"},
            {"name": "方案 B: 平衡策略", "investment": "中投入", "timeline": "中期见效", "risk": "中风险", "return": "中高回报", "confidence": "中"},
            {"name": "方案 C: 激进策略", "investment": "高投入", "timeline": "长期见效", "risk": "高风险", "return": "高回报", "confidence": "低"},
        ]
        opts = options if options else default_options

        lines = [
            "## 📊 CEO 决策选项对比",
            "",
            "基于数据分析，提供以下决策选项供选择：",
            "",
            "### 决策矩阵",
            "",
            "| 维度 | " + " | ".join(opt.get("name", f"方案{i+1}") for i, opt in enumerate(opts)) + " |",
            "|------|" + "|".join(["------"] * len(opts)) + "|",
        ]

        dimensions = [
            ("💰 投入成本", "investment"),
            ("⏱️ 时间周期", "timeline"),
            ("⚠️ 风险等级", "risk"),
            ("📈 预期回报", "return"),
            ("🎯 成功把握", "confidence"),
        ]

        for dim_label, dim_key in dimensions:
            row = f"| {dim_label} | " + " | ".join(opt.get(dim_key, "-") for opt in opts) + " |"
            lines.append(row)

        lines.extend([
            "",
            "### 推荐方案",
            "",
            f"**推荐**: {opts[1].get('name', '方案 B')}（平衡风险与回报）",
            "",
            "**理由**:",
            f"- 投入可控：{opts[1].get('investment', '中等')}，不会造成资源过度占用",
            f"- 风险适中：{opts[1].get('risk', '中等')}，在可接受范围内",
            f"- 回报合理：{opts[1].get('return', '中高')}，能实现业务目标",
            "",
            "### 关键决策点",
            "",
            "| 决策点 | 建议 | 截止 |",
            "|--------|------|------|",
            "| 资源投入 | 批准预算 | T+3 天 |",
            "| 时间窗口 | 确认上线时间 | T+5 天 |",
            "| 风险预案 | 制定 B 计划 | T+7 天 |",
            "",
        ])

        return "\n".join(lines)

    def visualize_execution_risks(self, context: Optional[Dict] = None) -> str:
        """
        CEO 决策方法 2: 执行风险可视化

        识别并可视化执行过程中的关键风险，帮助 CEO 做出风险知情决策。

        Args:
            context: 执行上下文，包含 timeline, team_size, dependencies 等

        Returns:
            Markdown 格式的风险可视化报告

        Example::

            skill = SWDSkill("季度业绩汇报")
            risks = skill.visualize_execution_risks({
                "timeline": "8 周",
                "team_size": 5,
                "dependencies": ["技术团队", "设计团队"]
            })
        """
        ctx = context or {}
        timeline = ctx.get("timeline", "8 周")
        team_size = ctx.get("team_size", 5)
        dependencies = ctx.get("dependencies", ["跨部门协作"])

        default_risks = [
            {"category": "进度风险", "risk": "需求变更导致延期", "probability": "中", "impact": "高", "mitigation": "冻结需求范围，变更需 CEO 审批"},
            {"category": "资源风险", "risk": f"{team_size}人团队可能不足", "probability": "中", "impact": "中", "mitigation": "预留 20% 缓冲人力"},
            {"category": "技术风险", "risk": "技术债务累积", "probability": "低", "impact": "高", "mitigation": "每迭代安排 20% 重构时间"},
            {"category": "协作风险", "risk": f"{', '.join(dependencies[:2])} 协调困难", "probability": "高", "impact": "中", "mitigation": "设立跨部门联络人，周同步"},
            {"category": "市场风险", "risk": "竞品抢先发布", "probability": "中", "impact": "高", "mitigation": "MVP 快速上线，后续迭代优化"},
        ]

        lines = [
            "## ⚠️ 执行风险可视化",
            "",
            f"**执行周期**: {timeline} | **团队规模**: {team_size}人 | **关键依赖**: {', '.join(dependencies)}",
            "",
            "### 风险矩阵",
            "",
            "| 概率\\影响 | 低 | 中 | 高 |",
            "|----------|-----|-----|-----|",
            "| **高**   | 🟢  | 🟡 低 | 🟠 中 |",
            "| **中**   | 🟢 低 | 🟡 中 | 🟠 高 |",
            "| **低**   | 🟢 低 | 🟢 低 | 🟡 中 |",
            "",
            "### 关键风险清单 (Top 5)",
            "",
        ]

        for i, r in enumerate(default_risks, 1):
            risk_level = "🟠" if r["impact"] == "高" and r["probability"] in ["高", "中"] else "🟡" if r["impact"] == "中" else "🟢"
            lines.append(f"{risk_level} **风险{i}**: {r['risk']}")
            lines.append(f"   - 类别：{r['category']}")
            lines.append(f"   - 概率：{r['probability']} | 影响：{r['impact']}")
            lines.append(f"   - 缓解措施：{r['mitigation']}")
            lines.append("")

        lines.extend([
            "### 风险应对策略",
            "",
            "| 策略类型 | 适用风险 | 行动方案 |",
            "|----------|----------|----------|",
            "| 🛡️ 规避 | 高概率高影响 | 调整方案，消除风险源 |",
            "| 📉 降低 | 中概率高影响 | 增加资源，加强监控 |",
            "| 🤝 转移 | 低概率高影响 | 外包/保险/合作伙伴 |",
            "| ✅ 接受 | 低概率低影响 | 建立应急预算，监控触发 |",
            "",
            "### CEO 决策建议",
            "",
            "1. **立即行动**: 审批风险缓解预算（建议总预算的 15-20%）",
            "2. **关键监控**: 每周审查 Top 3 风险状态",
            "3. **触发机制**: 任一🟠风险升级为红色，立即上报 CEO",
            "",
        ])

        return "\n".join(lines)

    def generate_decision_framework(self, decision_type: str = "go_no_go") -> str:
        """
        CEO 决策方法 3: 生成决策框架

        为 CEO 提供结构化的决策框架，确保决策过程系统化、可追溯。

        Args:
            decision_type: 决策类型，支持 "go_no_go", "priority", "resource_allocation", "risk_acceptance"

        Returns:
            Markdown 格式的决策框架

        Example::

            skill = SWDSkill("季度业绩汇报")
            framework = skill.generate_decision_framework("go_no_go")
        """
        frameworks = {
            "go_no_go": {
                "title": "🎯 Go/No-Go 决策框架",
                "criteria": [
                    ("战略一致性", "项目是否与公司年度战略目标一致？", "是/否"),
                    ("市场窗口", "是否处于最佳市场进入时机？", "是/否"),
                    ("资源可行", "现有资源是否足以支撑执行？", "是/否"),
                    ("风险可控", "主要风险是否有明确缓解方案？", "是/否"),
                    ("回报明确", "ROI 是否清晰且可接受？", "是/否"),
                ],
                "threshold": "5 项中至少 4 项为'是' → Go；否则 → No-Go",
                "next_steps": ["Go: 批准立项，分配资源", "No-Go: 记录原因，归档备查"],
            },
            "priority": {
                "title": "📋 优先级决策框架",
                "criteria": [
                    ("影响力", "对业务目标的影响程度 (1-10)", "分数"),
                    ("紧急性", "时间敏感度 (1-10)", "分数"),
                    ("可行性", "执行难度反向评分 (1-10)", "分数"),
                    ("战略匹配", "与战略方向契合度 (1-10)", "分数"),
                ],
                "threshold": "总分 = 影响力×30% + 紧急性×30% + 可行性×20% + 战略匹配×20%",
                "next_steps": ["≥8 分：P0 优先级，立即执行", "6-7 分：P1 优先级，排队执行", "<6 分：P2 优先级，暂缓或放弃"],
            },
            "resource_allocation": {
                "title": "💰 资源分配决策框架",
                "criteria": [
                    ("当前投入", "已投入资源（人/钱/时间）", "数值"),
                    ("追加需求", "还需投入资源", "数值"),
                    ("机会成本", "若投入此项目，放弃的其他机会", "描述"),
                    ("预期回报", "项目成功后的收益", "数值/描述"),
                    ("失败损失", "项目失败的最大损失", "数值/描述"),
                ],
                "threshold": "预期回报 > (追加需求 + 机会成本) × 1.5 → 批准；否则 → 重新评估",
                "next_steps": ["批准：签署资源分配协议", "拒绝：释放资源给其他项目", "重评：要求补充商业论证"],
            },
            "risk_acceptance": {
                "title": "⚠️ 风险接受决策框架",
                "criteria": [
                    ("风险描述", "具体风险是什么？", "描述"),
                    ("发生概率", "风险发生的可能性", "高/中/低"),
                    ("影响程度", "风险发生后的影响", "高/中/低"),
                    ("缓解成本", "完全缓解此风险的成本", "数值"),
                    ("接受阈值", "公司可接受的最大损失", "数值"),
                ],
                "threshold": "缓解成本 > 预期损失 (概率×影响) → 接受风险；否则 → 投入缓解",
                "next_steps": ["接受：记录风险，建立监控", "缓解：批准缓解预算，执行措施"],
            },
        }

        fw = frameworks.get(decision_type, frameworks["go_no_go"])

        lines = [
            f"## {fw['title']}",
            "",
            f"**决策类型**: `{decision_type}` | **项目**: {self.project}",
            "",
            "### 决策标准",
            "",
            "| 标准 | 问题 | 评估 |",
            "|------|------|------|",
        ]

        for name, question, eval_type in fw["criteria"]:
            lines.append(f"| {name} | {question} | {eval_type} |")

        lines.extend([
            "",
            "### 决策阈值",
            "",
            fw["threshold"],
            "",
            "### 决策结果与下一步",
            "",
            "| 结果 | 行动 |",
            "|------|------|",
        ])

        for step in fw["next_steps"]:
            parts = step.split(": ", 1)
            if len(parts) == 2:
                lines.append(f"| {parts[0]} | {parts[1]} |")
            else:
                lines.append(f"| - | {step} |")

        lines.extend([
            "",
            "### 决策记录模板",
            "",
            "```",
            f"决策类型：{decision_type}",
            f"项目名称：{self.project}",
            f"决策日期：YYYY-MM-DD",
            f"决策人：[CEO 姓名]",
            f"决策结果：[Go/No-Go/P0/P1/P2/批准/拒绝/接受/缓解]",
            f"关键依据：[列出 Top 3 决策依据]",
            f"后续行动：[具体行动项 + 负责人 + 截止日]",
            "```",
            "",
        ])

        return "\n".join(lines)



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
