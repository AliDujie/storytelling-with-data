"""SWD 故事构建器

基于三幕结构、Bing-Bang-Bongo、水平/垂直逻辑构建数据故事。
"""

from dataclasses import dataclass, field
from typing import List, Optional

from .config import STORY_ACTS, STORY_LABELS, NARRATIVE_FLOWS


@dataclass
class StorySetup:
    """第一幕：开始"""
    setting: str = ""
    protagonist: str = ""
    imbalance: str = ""
    desired_balance: str = ""
    solution_preview: str = ""


@dataclass
class StoryMiddle:
    """第二幕：中间"""
    evidence_points: List[str] = field(default_factory=list)
    comparison_points: List[str] = field(default_factory=list)
    consequences_if_no_action: str = ""
    options: List[str] = field(default_factory=list)
    recommended_solution: str = ""
    why_audience_unique: str = ""


@dataclass
class StoryEnd:
    """第三幕：结尾"""
    call_to_action: str = ""
    tie_back_to_beginning: str = ""
    urgency: str = ""


@dataclass
class SlideTitle:
    """幻灯片标题（水平逻辑）"""
    order: int
    title: str
    is_action_title: bool = True


@dataclass
class BingBangBongo:
    """Bing-Bang-Bongo 重复结构"""
    bing: str = ""   # 预告
    bang: str = ""   # 主体
    bongo: str = ""  # 回顾


@dataclass
class DataStory:
    """完整数据故事"""
    title: str = ""
    narrative_flow: str = "chronological"
    delivery_mode: str = "live_presentation"
    setup: StorySetup = field(default_factory=StorySetup)
    middle: StoryMiddle = field(default_factory=StoryMiddle)
    end: StoryEnd = field(default_factory=StoryEnd)
    bbb: BingBangBongo = field(default_factory=BingBangBongo)
    slide_titles: List[SlideTitle] = field(default_factory=list)

    def validate(self) -> List[str]:
        issues: List[str] = []
        if not self.setup.protagonist:
            issues.append("主角未定义——应以受众为框架")
        if not self.setup.imbalance:
            issues.append("缺少不平衡/冲突——没有冲突就没有故事")
        if not self.end.call_to_action:
            issues.append("缺少行动号召——受众不知道该做什么")
        if not self.middle.evidence_points:
            issues.append("缺少数据证据——需要数据支撑你的故事")
        # 水平逻辑检查
        non_action = [s for s in self.slide_titles if not s.is_action_title]
        if non_action:
            issues.append(f"{len(non_action)}个幻灯片使用描述标题而非行动标题")
        return issues


class StoryBuilder:
    """故事构建器 — 构建完整的数据故事"""

    def __init__(self, title: str):
        self._story = DataStory(title=title)

    def set_narrative_flow(self, flow: str = "chronological",
                           mode: str = "live_presentation") -> "StoryBuilder":
        self._story.narrative_flow = flow
        self._story.delivery_mode = mode
        return self

    def set_setup(self, setting: str, protagonist: str,
                  imbalance: str, desired_balance: str,
                  solution_preview: str = "") -> "StoryBuilder":
        self._story.setup = StorySetup(
            setting=setting, protagonist=protagonist,
            imbalance=imbalance, desired_balance=desired_balance,
            solution_preview=solution_preview)
        return self

    def add_evidence(self, point: str) -> "StoryBuilder":
        self._story.middle.evidence_points.append(point)
        return self

    def add_comparison(self, point: str) -> "StoryBuilder":
        self._story.middle.comparison_points.append(point)
        return self

    def set_consequences(self, text: str) -> "StoryBuilder":
        self._story.middle.consequences_if_no_action = text
        return self

    def add_option(self, option: str) -> "StoryBuilder":
        self._story.middle.options.append(option)
        return self

    def set_recommendation(self, rec: str) -> "StoryBuilder":
        self._story.middle.recommended_solution = rec
        return self

    def set_end(self, call_to_action: str, tie_back: str = "",
                urgency: str = "") -> "StoryBuilder":
        self._story.end = StoryEnd(
            call_to_action=call_to_action,
            tie_back_to_beginning=tie_back, urgency=urgency)
        return self

    def set_bing_bang_bongo(self, bing: str, bang: str,
                            bongo: str) -> "StoryBuilder":
        self._story.bbb = BingBangBongo(bing=bing, bang=bang, bongo=bongo)
        return self

    def add_slide_title(self, title: str,
                        is_action: bool = True) -> "StoryBuilder":
        order = len(self._story.slide_titles) + 1
        self._story.slide_titles.append(
            SlideTitle(order=order, title=title, is_action_title=is_action))
        return self

    def check_horizontal_logic(self) -> List[str]:
        """检查水平逻辑——只读标题能否讲述完整故事"""
        issues: List[str] = []
        titles = [s.title for s in self._story.slide_titles]
        if not titles:
            issues.append("没有幻灯片标题——无法检查水平逻辑")
            return issues
        non_action = [s for s in self._story.slide_titles if not s.is_action_title]
        if non_action:
            for s in non_action:
                issues.append(f"幻灯片{s.order} '{s.title}' 是描述标题，建议改为行动标题")
        return issues

    def build(self) -> DataStory:
        return self._story

    @staticmethod
    def render_markdown(story: DataStory) -> str:
        issues = story.validate()
        warnings = ""
        if issues:
            items = "\n".join(f"- ⚠️ {i}" for i in issues)
            warnings = f"\n## ⚠️ 待完善项\n{items}\n"

        evidence = "\n".join(f"- 📊 {e}" for e in story.middle.evidence_points) or "- （未添加）"
        comparisons = "\n".join(f"- 🔄 {c}" for c in story.middle.comparison_points) or ""
        options = "\n".join(f"- 💡 {o}" for o in story.middle.options) or ""
        slides = ""
        if story.slide_titles:
            slides = "\n".join(
                f"{s.order}. {'✅' if s.is_action_title else '❌'} {s.title}"
                for s in story.slide_titles)

        return f"""# 📖 数据故事：{story.title}
{warnings}
## 故事结构

### 第一幕：开始 (Setup)
- **设定**: {story.setup.setting or '（未设定）'}
- **主角**: {story.setup.protagonist or '（未定义——应以受众为框架！）'}
- **不平衡/冲突**: {story.setup.imbalance or '（未定义——没有冲突就没有故事）'}
- **期望平衡**: {story.setup.desired_balance or '（未定义）'}

### 第二幕：中间 (Conflict & Evidence)
**数据证据**:
{evidence}
{f"**对比参考**:{chr(10)}{comparisons}" if comparisons else ""}
{f"**不行动的后果**: {story.middle.consequences_if_no_action}" if story.middle.consequences_if_no_action else ""}
{f"**方案选项**:{chr(10)}{options}" if options else ""}
{f"**推荐方案**: {story.middle.recommended_solution}" if story.middle.recommended_solution else ""}

### 第三幕：结尾 (Resolution)
- **行动号召**: {story.end.call_to_action or '（未定义）'}
- **回扣开头**: {story.end.tie_back_to_beginning or '（未设定）'}
{f"- **紧迫感**: {story.end.urgency}" if story.end.urgency else ""}

## 叙事设计
- **叙事顺序**: {story.narrative_flow}
- **沟通形式**: {story.delivery_mode}

{f'''## Bing, Bang, Bongo
- **Bing (预告)**: {story.bbb.bing}
- **Bang (主体)**: {story.bbb.bang}
- **Bongo (回顾)**: {story.bbb.bongo}
''' if story.bbb.bing else ''}
{f"## 幻灯片标题序列（水平逻辑）{chr(10)}{slides}" if slides else ""}
"""
