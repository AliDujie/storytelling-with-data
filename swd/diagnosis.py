"""SWD 可视化综合诊断引擎

基于SWD六课体系的五维度100分制综合诊断。
"""

from dataclasses import dataclass, field
from typing import List, Dict

from .config import DIAGNOSIS_DIMENSIONS, DIAGNOSIS_LABELS


@dataclass
class DimensionScore:
    """单维度评分"""
    dimension: str
    items: List[tuple] = field(default_factory=list)  # (name, score, max, note)

    @property
    def score(self) -> int:
        return sum(s for _, s, _, _ in self.items)

    @property
    def max_score(self) -> int:
        return sum(m for _, _, m, _ in self.items)

    @property
    def label(self) -> str:
        return DIAGNOSIS_LABELS.get(self.dimension, self.dimension)


@dataclass
class DiagnosisResult:
    """综合诊断结果"""
    title: str = ""
    dimensions: Dict[str, DimensionScore] = field(default_factory=dict)
    top_improvements: List[str] = field(default_factory=list)
    makeover_suggestions: List[str] = field(default_factory=list)

    @property
    def total_score(self) -> int:
        return sum(d.score for d in self.dimensions.values())

    @property
    def total_max(self) -> int:
        return sum(d.max_score for d in self.dimensions.values())

    @property
    def badge(self) -> str:
        s = self.total_score
        t = self.total_max
        pct = s / t * 100 if t else 0
        if pct >= 90: return f"🟢 {s}/{t} 卓越"
        if pct >= 70: return f"🟡 {s}/{t} 良好"
        if pct >= 50: return f"🟠 {s}/{t} 需改进"
        return f"🔴 {s}/{t} 需重做"


# ── 每个维度的评分项 ──
CONTEXT_ITEMS = [
    ("audience_clear", "受众是否明确？信息是否针对特定受众？"),
    ("cta_clear", "行动号召是否清晰？受众知道该做什么吗？"),
    ("big_idea_visible", "大创意是否可在5秒内识别？"),
    ("data_supports_story", "数据是否支撑故事（而非仅展示数据）？"),
]

VISUAL_ITEMS = [
    ("chart_type_fit", "图表类型是否适合数据类型和目的？"),
    ("avoid_bad_charts", "是否避免了饼图/3D/双Y轴等问题图表？"),
    ("zero_baseline", "柱状图是否有零基线？时间轴是否一致？"),
    ("logical_order", "数据排序是否有逻辑？"),
]

CLUTTER_ITEMS = [
    ("no_unnecessary_elements", "是否有不必要的边框/网格线/数据标记？"),
    ("no_diagonal_text", "是否有对角文本或居中对齐问题？"),
    ("whitespace_ok", "白色空间使用是否恰当？"),
    ("no_redundancy", "是否有冗余信息（如图例+直接标注）？"),
]

ATTENTION_ITEMS = [
    ("preattentive_used", "是否使用了前注意属性引导焦点？"),
    ("color_sparse", "颜色使用是否稀疏且有策略？"),
    ("visual_hierarchy", "是否创建了清晰的视觉层次？"),
    ("eyes_drawn_test", "'眼睛首先看向哪里'测试是否通过？"),
]

DESIGN_ITEMS = [
    ("text_sufficient", "文本是否充分（标题/轴标题/注释/数据来源）？"),
    ("alignment_aesthetic", "对齐和美学是否专业？"),
    ("narrative_structure", "是否有清晰的叙事结构（开始-中间-结尾）？"),
    ("action_titles", "是否使用了行动标题而非描述标题？"),
]

ALL_DIMENSION_ITEMS = {
    "context": CONTEXT_ITEMS,
    "visual_choice": VISUAL_ITEMS,
    "clutter": CLUTTER_ITEMS,
    "attention": ATTENTION_ITEMS,
    "design_narrative": DESIGN_ITEMS,
}


class DiagnosisEngine:
    """综合诊断引擎 — 五维度100分制评估"""

    def __init__(self, title: str = ""):
        self._result = DiagnosisResult(title=title)
        for dim in DIAGNOSIS_DIMENSIONS:
            self._result.dimensions[dim] = DimensionScore(dimension=dim)

    def score(self, dimension: str, item_key: str, score: int,
              note: str = "") -> "DiagnosisEngine":
        if dimension not in self._result.dimensions:
            raise ValueError(f"未知维度: {dimension}")
        items = ALL_DIMENSION_ITEMS.get(dimension, [])
        name = next((desc for k, desc in items if k == item_key), item_key)
        self._result.dimensions[dimension].items.append((name, score, 5, note))
        return self

    def auto_score(self, scores: Dict[str, Dict[str, int]]) -> "DiagnosisEngine":
        """批量评分 scores = {"context": {"audience_clear": 4, ...}, ...}"""
        for dim, items in scores.items():
            for item_key, sc in items.items():
                self.score(dim, item_key, sc)
        return self

    def add_improvement(self, suggestion: str) -> "DiagnosisEngine":
        self._result.top_improvements.append(suggestion)
        return self

    def add_makeover(self, suggestion: str) -> "DiagnosisEngine":
        self._result.makeover_suggestions.append(suggestion)
        return self

    def auto_improvements(self) -> "DiagnosisEngine":
        """基于低分项自动生成改进建议"""
        low_items = []
        for dim, ds in self._result.dimensions.items():
            for name, sc, mx, note in ds.items:
                if sc <= 2:
                    low_items.append((sc, dim, name, note))
        low_items.sort(key=lambda x: x[0])
        for sc, dim, name, note in low_items[:5]:
            label = DIAGNOSIS_LABELS.get(dim, dim)
            self._result.top_improvements.append(f"[{label}] {name}" + (f" — {note}" if note else ""))
        return self

    def build(self) -> DiagnosisResult:
        return self._result

    @staticmethod
    def render_markdown(result: DiagnosisResult) -> str:
        lines = [f"# 🔍 SWD 综合诊断报告：{result.title}\n"]
        lines.append(f"## 总分: {result.badge}\n")

        for dim in DIAGNOSIS_DIMENSIONS:
            ds = result.dimensions.get(dim)
            if not ds or not ds.items:
                continue
            lines.append(f"### {ds.label} ({ds.score}/{ds.max_score})\n")
            lines.append("| 评分项 | 得分 | 备注 |")
            lines.append("|--------|------|------|")
            for name, sc, mx, note in ds.items:
                bar = "█" * sc + "░" * (mx - sc)
                lines.append(f"| {name} | {bar} {sc}/{mx} | {note} |")
            lines.append("")

        if result.top_improvements:
            lines.append("## 优先改进建议\n")
            for i, imp in enumerate(result.top_improvements, 1):
                lines.append(f"{i}. {imp}")

        if result.makeover_suggestions:
            lines.append("\n## 改造建议\n")
            for s in result.makeover_suggestions:
                lines.append(f"- {s}")

        return "\n".join(lines)
