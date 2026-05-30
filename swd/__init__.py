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

__version__ = "2.2.119"

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
                    include_ceo_analysis: bool = False,
                    decision_options: Optional[List[Dict]] = None,
                    ) -> str:
        """构建完整的数据故事（可选 CEO 视角扩展分析）
        
        Args:
            include_ceo_analysis: 是否包含 CEO 视角扩展分析（默认 False）
            decision_options: 决策选项列表（可选）
        """
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
        
        # 添加 CEO 视角扩展分析
        if include_ceo_analysis:
            decision_comp = self.build_decision_comparison(decision_options)
            risks = self.visualize_execution_risks()
            framework = self.generate_decision_framework()
            result += f"\n\n---\n\n## CEO 视角扩展分析\n\n{decision_comp}\n\n---\n\n{risks}\n\n---\n\n{framework}"
        
        return result

    def generate_story(self, protagonist: str, imbalance: str,
                      setting: str = "", desired_balance: str = "",
                      evidence: Optional[List[str]] = None,
                      call_to_action: str = "",
                      narrative_flow: str = "chronological",
                      delivery_mode: str = "live_presentation",
                      slide_titles: Optional[List[str]] = None,
                      bing: str = "", bang: str = "", bongo: str = "",
                      include_ceo_analysis: bool = True,
                      options: Optional[List[Dict]] = None,
                      ) -> str:
        """生成数据叙事报告（含 CEO 决策模块）
        
        Args:
            include_ceo_analysis: 是否包含 CEO 视角扩展分析（默认 True）
            options: 决策选项列表（可选）
        """
        # 原有数据叙事生成逻辑
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
        
        # 添加 CEO 视角扩展分析
        if include_ceo_analysis:
            decision_comp = self.build_decision_comparison(options)
            risks = self.visualize_execution_risks()
            framework = self.generate_decision_framework()
            result += f"\n\n---\n\n## CEO 视角扩展分析\n\n{decision_comp}\n\n---\n\n{risks}\n\n---\n\n{framework}"
        
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

    # ── CEO 视角扩展方法 ──

    def build_decision_comparison(self, options: Optional[List[Dict]] = None) -> str:
        """构建决策选项对比可视化（CEO 视角）
        
        为 CEO 提供多方案对比，支持快速决策。
        
        Args:
            options: 决策选项列表，每个选项应包含 name, 投入, 预期回报, ROI, 风险, 时间, 可逆性, 推荐度
        """
        if options is None:
            options = [
                {"name": "方案 A", "投入": "XXX 万", "预期回报": "XXX 万/年", "ROI": "XX%", "风险": "中", "时间": "X 个月", "可逆性": "可逆", "推荐度": "⭐⭐⭐⭐"},
                {"name": "方案 B", "投入": "XXX 万", "预期回报": "XXX 万/年", "ROI": "XX%", "风险": "低", "时间": "X 个月", "可逆性": "可逆", "推荐度": "⭐⭐⭐⭐⭐"},
                {"name": "方案 C", "投入": "XXX 万", "预期回报": "XXX 万/年", "ROI": "XX%", "风险": "高", "时间": "X 个月", "可逆性": "不可逆", "推荐度": "⭐⭐⭐"},
            ]
        
        # 生成对比表头
        header = "| 维度 | " + " | ".join([o["name"] for o in options]) + " |"
        divider = "|------|" + "|".join(["------"] * len(options)) + "|"
        
        # 生成对比表行
        rows = [
            ("投入成本", [o["投入"] for o in options]),
            ("预期回报", [o["预期回报"] for o in options]),
            ("ROI", [o["ROI"] for o in options]),
            ("风险等级", [o["风险"] for o in options]),
            ("时间周期", [o["时间"] for o in options]),
            ("可逆性", [o["可逆性"] for o in options]),
            ("推荐度", [o["推荐度"] for o in options]),
        ]
        
        table_rows = "\n".join([
            f"| {dim} | " + " | ".join(values) + " |"
            for dim, values in rows
        ])
        
        table = f"{header}\n{divider}\n{table_rows}"
        
        # 找出推荐方案
        recommended = max(options, key=lambda x: x["推荐度"].count("⭐"))
        
        # 生成各方案深度分析
        options_analysis = ""
        for i, opt in enumerate(options):
            options_analysis += f"""
#### {opt["name"]}
**核心思路**: XXX

**投入产出**:
- 投入：{opt["投入"]}
- 预期回报：{opt["预期回报"]}
- ROI: {opt["ROI"]}

**风险评估**:
- 风险等级：{opt["风险"]}
- 主要风险：XXX
- 缓解措施：XXX

**适用场景**:
- 场景 1: XXX
- 场景 2: XXX

---
"""
        
        return f"""
## 决策选项对比

---

### 方案对比表

{table}

---

### 推荐方案

**推荐**: {recommended["name"]}

**理由**:
1. ROI 最高（{recommended["ROI"]}）
2. 风险可控（{recommended["风险"]}）
3. 可逆性强（{recommended["可逆性"]}）

**关键优势**:
- 优势 1: {recommended.get("优势 1", "XXX")}
- 优势 2: {recommended.get("优势 2", "XXX")}
- 优势 3: {recommended.get("优势 3", "XXX")}

---

### 各方案深度分析
{options_analysis}
### 关键假设（需验证）

| 假设 | 影响方案 | 验证方法 | 验证时间 | 风险 |
|------|---------|---------|---------|------|
| 用户增长率 | 方案 A/B | A/B 测试 | X 周 | 高/中/低 |
| 获客成本 | 方案 A/C | 小范围测试 | X 周 | 高/中/低 |
| 技术可行性 | 方案 B/C | 技术验证 | X 周 | 高/中/低 |

---

### 决策建议

| 情景 | 推荐方案 | 理由 |
|------|---------|------|
| 资源充足 | {recommended["name"]} | ROI 最高，风险可控 |
| 资源有限 | 方案 B | 投入最低，回本最快 |
| 风险厌恶 | 方案 B | 风险最低，可逆性强 |
| 追求增长 | 方案 A | 增长潜力最大 |
"""

    def visualize_execution_risks(self) -> str:
        """可视化执行风险（CEO 视角）
        
        用可视化方式呈现各方案的风险分布和缓解措施。
        """
        return """
## 执行风险可视化

---

### 风险矩阵
```
                影响程度
                   ↑
             高    │  ② 方案 C    │  ① 方案 A
                   │  (高影响/中概率)│  (高影响/低概率)
                   │─────────────┼─────────────
             中    │  ④ 方案 B    │  ③ 方案 A
                   │  (中影响/低概率)│  (中影响/低概率)
                   │─────────────┼─────────────
             低    │            │
                   │            │
                   └────────────┴─────────────→
                        低        中        高
                              发生概率
```

**风险说明**:
1. **① XXX**（方案 A）- 概率低，但影响高
   - 描述：XXX
   - 应对：XXX

2. **② XXX**（方案 C）- 概率中，影响高
   - 描述：XXX
   - 应对：XXX

3. **③ XXX**（方案 A）- 概率低，影响中
   - 描述：XXX
   - 应对：XXX

4. **④ XXX**（方案 B）- 概率低，影响中
   - 描述：XXX
   - 应对：XXX

---

### 各方案风险对比

| 方案 | 高风险项 | 中风险项 | 低风险项 | 综合风险 |
|------|---------|---------|---------|---------|
| 方案 A | X 项 | X 项 | X 项 | 🟡 中 |
| 方案 B | X 项 | X 项 | X 项 | 🟢 低 |
| 方案 C | X 项 | X 项 | X 项 | 🔴 高 |

**综合风险评估标准**:
- 🟢 低：高风险项 = 0，中风险项 ≤ 2
- 🟡 中：高风险项 ≤ 1，中风险项 ≤ 3
- 🔴 高：高风险项 ≥ 2

---

### 风险缓解措施

#### 方案 A
| 风险 | 缓解措施 | 负责人 | 检查点 | 状态 |
|------|---------|--------|--------|------|
| 技术实现风险 | 提前技术验证 | XXX | T+X 周 | 未开始 |
| 资源不足风险 | 预留缓冲资源 | XXX | T+X 周 | 未开始 |
| 进度延期风险 | 关键路径监控 | XXX | 每周 | 未开始 |

#### 方案 B
| 风险 | 缓解措施 | 负责人 | 检查点 | 状态 |
|------|---------|--------|--------|------|
| 效果不达预期 | A/B 测试验证 | XXX | T+X 周 | 未开始 |
| 用户接受度低 | 早期用户反馈 | XXX | T+X 周 | 未开始 |

#### 方案 C
| 风险 | 缓解措施 | 负责人 | 检查点 | 状态 |
|------|---------|--------|--------|------|
| 高投入风险 | 分阶段投入 | XXX | T+X 周 | 未开始 |
| 不可逆风险 | 充分前期验证 | XXX | T+X 周 | 未开始 |
| 市场竞争风险 | 快速上市策略 | XXX | T+X 周 | 未开始 |

---

### 风险触发预警

| 风险 | 预警信号 | 触发条件 | 应急响应 | 负责人 |
|------|---------|---------|---------|--------|
| 进度延期 | 关键里程碑延迟 | 延迟 > X 周 | 启动赶工计划 | XXX |
| 预算超支 | 实际支出超预算 | 超支 > XX% | 冻结非必要支出 | XXX |
| 质量下降 | Bug 率上升 | Bug 率 > X% | 暂停发布，专注修复 | XXX |
| 团队流失 | 核心成员离职 | 离职 ≥ X 人 | 启动Backup 计划 | XXX |

---

### 风险管理建议

1. **每周风险审查**: 每周一上午审查风险状态
2. **风险升级机制**: 高风险项需上报 CEO
3. **风险应对预算**: 预留 XX% 预算作为风险缓冲
4. **风险沟通机制**: 重大风险 24 小时内通报相关方
"""

    def generate_decision_framework(self) -> str:
        """生成数据叙事决策框架（CEO 视角）
        
        将数据叙事与决策流程结合，形成完整的决策支持。
        """
        return """
## 数据叙事决策框架

---

### 决策流程图
```
                ┌─────────────┐
                │  问题定义   │
                └──────┬──────┘
                       ↓
                ┌─────────────┐
                │  数据收集   │
                └──────┬──────┘
                       ↓
                ┌─────────────┐
     ┌─────────│  数据分析   │─────────┐
     ↓         └──────┬──────┘         ↓
┌─────────┐          ↓          ┌─────────┐
│ 方案 A  │    ┌─────────────┐  │ 方案 B  │
│ 数据支撑│    │  方案对比   │  │ 数据支撑│
└────┬────┘    └──────┬──────┘  └────┬────┘
     ↓                ↓              ↓
     └───────────┬──────────────────┘
                 ↓
          ┌─────────────┐
          │  决策建议   │
          └──────┬──────┘
                 ↓
          ┌─────────────┐
          │  行动计划   │
          └─────────────┘
```

---

### 各阶段关键问题

#### 1. 问题定义
- [ ] 核心问题是什么？
- [ ] 谁受影响？
- [ ] 问题的商业影响是什么？
- [ ] 为什么现在需要解决？

#### 2. 数据收集
- [ ] 需要哪些数据？
- [ ] 数据来源是否可靠？
- [ ] 数据是否完整？
- [ ] 数据时效性如何？

#### 3. 数据分析
- [ ] 分析方法和假设是否合理？
- [ ] 是否存在偏差？
- [ ] 结论是否有数据支撑？
- [ ] 是否考虑了反例？

#### 4. 方案对比
- [ ] 是否穷尽了主要选项？
- [ ] 对比维度是否全面？
- [ ] 权重分配是否合理？
- [ ] 是否考虑了长期影响？

#### 5. 决策建议
- [ ] 推荐方案的理由是否充分？
- [ ] 风险是否充分披露？
- [ ] 是否有应急预案？
- [ ] 是否有明确的行动计划？

#### 6. 行动计划
- [ ] 行动步骤是否清晰？
- [ ] 责任人和时间是否明确？
- [ ] 成功标准是否可衡量？
- [ ] 是否有检查点？

---

### 决策质量检查清单

| 维度 | 检查项 | 标准 | 状态 |
|------|--------|------|------|
| **数据质量** | 数据来源可靠 | 来自权威渠道 | ✅/❌ |
| **数据质量** | 样本量充足 | 统计显著性 > 95% | ✅/❌ |
| **数据质量** | 分析方法正确 | 方法适用且无误 | ✅/❌ |
| **逻辑严密** | 因果关系清晰 | 有因果证据 | ✅/❌ |
| **逻辑严密** | 无逻辑跳跃 | 推理链条完整 | ✅/❌ |
| **逻辑严密** | 考虑反向因果 | 已排除反向因果 | ✅/❌ |
| **风险披露** | 主要风险已识别 | 高风险项全部列出 | ✅/❌ |
| **风险披露** | 缓解措施可行 | 措施具体可执行 | ✅/❌ |
| **风险披露** | 应急预案完备 | 有 Backup 计划 | ✅/❌ |
| **可执行性** | 资源可获取 | 资源已确认 | ✅/❌ |
| **可执行性** | 时间可实现 | 时间线合理 | ✅/❌ |
| **可执行性** | 团队有能力 | 团队技能匹配 | ✅/❌ |

**决策质量评分**: ⚪⚪⚪⚪⚪ (X/5)

**评分标准**:
- 5 分：所有检查项 ✅
- 4 分：≤ 2 个 ❌
- 3 分：≤ 4 个 ❌
- 2 分：≤ 6 个 ❌
- 1 分：> 6 个 ❌

---

### 决策后追踪

| 指标 | 基线值 | 目标值 | 检查时间 | 负责人 | 实际值 | 状态 |
|------|--------|--------|---------|--------|--------|------|
| XXX | XXX | XXX | T+X 周 | XXX | - | 待检查 |
| XXX | XXX | XXX | T+X 周 | XXX | - | 待检查 |
| XXX | XXX | XXX | T+X 周 | XXX | - | 待检查 |
| XXX | XXX | XXX | T+X 周 | XXX | - | 待检查 |

**检查频率**:
- Phase 1 (0-4 周): 每周检查
- Phase 2 (4-12 周): 每两周检查
- Phase 3 (12 周+): 每月检查

**复盘时间**: T+X 周

**复盘议程**:
1. 目标达成情况
2. 关键成功因素
3. 主要问题和教训
4. 下一步行动

---

### 决策文档归档

| 文档 | 位置 | 负责人 | 状态 |
|------|------|--------|------|
| 问题定义文档 | XXX | XXX | 已完成 |
| 数据分析报告 | XXX | XXX | 已完成 |
| 方案对比表 | XXX | XXX | 已完成 |
| 决策会议记录 | XXX | XXX | 待完成 |
| 行动计划 | XXX | XXX | 待完成 |
| 复盘报告 | XXX | XXX | 待完成 |
"""	


__all__ = [
    "__version__",
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
