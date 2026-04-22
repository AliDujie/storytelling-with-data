"""SWD 图表改造引擎

提供从原始图表到最终故事的完整改造流程，包含六步法实战指导。
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class MakeoverStep:
    """单个改造步骤"""
    order: int
    lesson: str          # 对应SWD六课中的哪一课
    action: str
    before_desc: str = ""
    after_desc: str = ""
    rationale: str = ""


@dataclass
class DesignSpec:
    """改造后设计规范"""
    chart_type: str = ""
    title: str = ""
    title_type: str = "action"   # action / descriptive
    color_base: str = "灰色"
    color_accent: str = "蓝色"
    alignment: str = "左上对齐"
    font: str = "Arial / 无衬线字体"
    data_labels: str = "直接标注"
    axis_treatment: str = "灰色，简洁"
    annotations: List[str] = field(default_factory=list)
    data_source: str = ""


@dataclass
class NarrativeSlide:
    """叙事幻灯片（渐进式揭示）"""
    order: int
    headline: str
    emphasis: str = ""
    voiceover: str = ""


@dataclass
class MakeoverPlan:
    """完整改造方案"""
    title: str = ""
    original_issues: List[str] = field(default_factory=list)
    steps: List[MakeoverStep] = field(default_factory=list)
    design_spec: DesignSpec = field(default_factory=DesignSpec)
    narrative_slides: List[NarrativeSlide] = field(default_factory=list)


class MakeoverEngine:
    """图表改造引擎 — 六步法从原始图表到数据故事"""

    SIX_LESSONS = [
        ("context", "理解上下文", "明确受众、目的、Big Idea"),
        ("visual", "选择合适展示", "根据数据特征选择最佳图表类型"),
        ("clutter", "消除杂乱", "去除边框/网格线/标记/尾部零等"),
        ("attention", "聚焦注意力", "用颜色/大小/位置引导焦点"),
        ("design", "像设计师思考", "添加文本、对齐、美学优化"),
        ("story", "讲述故事", "构建叙事、渐进式揭示、行动号召"),
    ]

    def __init__(self, title: str = ""):
        self._plan = MakeoverPlan(title=title)

    def add_issue(self, issue: str) -> "MakeoverEngine":
        self._plan.original_issues.append(issue)
        return self

    def add_step(self, lesson: str, action: str,
                 before: str = "", after: str = "",
                 rationale: str = "") -> "MakeoverEngine":
        order = len(self._plan.steps) + 1
        self._plan.steps.append(MakeoverStep(
            order=order, lesson=lesson, action=action,
            before_desc=before, after_desc=after, rationale=rationale))
        return self

    def set_design_spec(self, chart_type: str = "", title: str = "",
                        color_accent: str = "蓝色",
                        annotations: Optional[List[str]] = None,
                        data_source: str = "") -> "MakeoverEngine":
        self._plan.design_spec = DesignSpec(
            chart_type=chart_type, title=title,
            color_accent=color_accent,
            annotations=annotations or [],
            data_source=data_source)
        return self

    def add_narrative_slide(self, headline: str, emphasis: str = "",
                            voiceover: str = "") -> "MakeoverEngine":
        order = len(self._plan.narrative_slides) + 1
        self._plan.narrative_slides.append(NarrativeSlide(
            order=order, headline=headline,
            emphasis=emphasis, voiceover=voiceover))
        return self

    def auto_steps_from_issues(self) -> "MakeoverEngine":
        """基于检测到的问题自动生成改造步骤"""
        issue_map = {
            "饼图": ("visual", "将饼图替换为水平柱状图", "人眼难以比较角度和面积"),
            "3D": ("visual", "移除3D效果，使用2D版本", "3D扭曲数值，造成误导"),
            "双Y轴": ("visual", "拆分为两个图或直接标注数据", "受众难以判断数据对应哪个轴"),
            "无标题": ("design", "添加行动标题", "受众需要知道看什么"),
            "无轴标题": ("design", "添加轴标题", "受众需要理解坐标含义"),
            "图例": ("clutter", "直接标注数据系列，移除图例", "减少来回查看的认知负荷"),
            "网格线": ("clutter", "移除或弱化网格线", "减少视觉噪音"),
            "边框": ("clutter", "移除图表边框", "利用闭合性原则"),
            "彩虹色": ("attention", "改为灰色基底+单一强调色", "太多颜色失去前注意价值"),
            "对角文本": ("clutter", "缩写标签消除对角文本", "对角文本阅读速度慢52%"),
            "居中对齐": ("design", "改为左对齐", "居中对齐不产生干净的线条"),
            "无行动号召": ("story", "添加明确的行动号召", "受众不知道该做什么"),
        }
        for issue in self._plan.original_issues:
            for keyword, (lesson, action, rationale) in issue_map.items():
                if keyword in issue:
                    self.add_step(lesson, action, before=issue, rationale=rationale)
                    break
        return self

    def build(self) -> MakeoverPlan:
        return self._plan

    @staticmethod
    def render_markdown(plan: MakeoverPlan) -> str:
        lines = [f"# ✨ 图表改造方案：{plan.title}\n"]

        if plan.original_issues:
            lines.append("## 原始问题诊断\n")
            for i, issue in enumerate(plan.original_issues, 1):
                lines.append(f"{i}. ❌ {issue}")

        if plan.steps:
            lines.append("\n## 改造步骤\n")
            for step in plan.steps:
                lesson_label = next(
                    (label for key, label, _ in MakeoverEngine.SIX_LESSONS
                     if key == step.lesson), step.lesson)
                lines.append(f"### 步骤 {step.order}: [{lesson_label}] {step.action}")
                if step.before_desc:
                    lines.append(f"- **改造前**: {step.before_desc}")
                if step.after_desc:
                    lines.append(f"- **改造后**: {step.after_desc}")
                if step.rationale:
                    lines.append(f"- **原理**: {step.rationale}")
                lines.append("")

        ds = plan.design_spec
        if ds.chart_type or ds.title:
            lines.append("## 改造后设计规范\n")
            lines.append("| 维度 | 规范 |")
            lines.append("|------|------|")
            if ds.chart_type:
                lines.append(f"| 图表类型 | {ds.chart_type} |")
            if ds.title:
                lines.append(f"| 标题 | {ds.title} ({ds.title_type}) |")
            lines.append(f"| 基色 | {ds.color_base} |")
            lines.append(f"| 强调色 | {ds.color_accent} |")
            lines.append(f"| 对齐 | {ds.alignment} |")
            lines.append(f"| 字体 | {ds.font} |")
            lines.append(f"| 数据标注 | {ds.data_labels} |")
            lines.append(f"| 轴处理 | {ds.axis_treatment} |")
            if ds.data_source:
                lines.append(f"| 数据来源 | {ds.data_source} |")
            if ds.annotations:
                lines.append("\n**注释**:")
                for a in ds.annotations:
                    lines.append(f"- {a}")

        if plan.narrative_slides:
            lines.append("\n## 叙事幻灯片序列（渐进式揭示）\n")
            for slide in plan.narrative_slides:
                lines.append(f"### 幻灯片 {slide.order}")
                lines.append(f"**标题**: {slide.headline}")
                if slide.emphasis:
                    lines.append(f"**强调**: {slide.emphasis}")
                if slide.voiceover:
                    lines.append(f"**口头叙述**: {slide.voiceover}")
                lines.append("")

        return "\n".join(lines)
