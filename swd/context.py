"""SWD 上下文分析引擎

提供受众分析、核心信息提炼、3分钟故事、Big Idea 构建等能力。
"""

from dataclasses import dataclass, field
from typing import List, Optional


KNOWLEDGE_LEVELS = ("expert", "general", "novice")
RELATIONSHIPS = ("first_contact", "established", "need_credibility")
MECHANISMS = ("live_presentation", "written_report", "email", "mixed")
TONES = ("serious", "urgent", "celebratory", "lighthearted", "neutral")
MOTIVATIONS = (
    "save_money", "grow_revenue", "beat_competition", "gain_market_share",
    "reduce_risk", "innovate", "improve_efficiency", "learn_skill",
)


@dataclass
class AudienceProfile:
    """受众画像"""
    primary_audience: str = ""
    decision_maker: str = ""
    knowledge_level: str = "general"
    relationship: str = "first_contact"
    biases: str = ""
    motivation: str = ""

    def validate(self) -> List[str]:
        issues: List[str] = []
        if not self.primary_audience:
            issues.append("必须指定主要受众（具体职位/角色，避免笼统描述）")
        if self.knowledge_level not in KNOWLEDGE_LEVELS:
            issues.append(f"了解程度 '{self.knowledge_level}' 不在可选值中: {KNOWLEDGE_LEVELS}")
        if self.relationship not in RELATIONSHIPS:
            issues.append(f"关系状态 '{self.relationship}' 不在可选值中: {RELATIONSHIPS}")
        return issues


@dataclass
class BigIdea:
    """大创意 — 必须满足三个条件"""
    unique_point_of_view: str = ""
    stakes: str = ""
    full_sentence: str = ""

    def validate(self) -> List[str]:
        issues: List[str] = []
        if not self.unique_point_of_view:
            issues.append("Big Idea 必须阐述你的独特观点")
        if not self.stakes:
            issues.append("Big Idea 必须传达利害关系")
        if not self.full_sentence:
            issues.append("Big Idea 必须是一个完整的句子")
        if self.full_sentence and len(self.full_sentence) < 10:
            issues.append("Big Idea 句子过短，建议更具体")
        return issues

    def render(self) -> str:
        return self.full_sentence


@dataclass
class ContextAnalysis:
    """完整的上下文分析"""
    title: str = ""
    audience: AudienceProfile = field(default_factory=AudienceProfile)
    mechanism: str = "live_presentation"
    tone: str = "neutral"
    three_min_story: str = ""
    big_idea: BigIdea = field(default_factory=BigIdea)
    supporting_data: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    call_to_action: str = ""

    def validate(self) -> List[str]:
        issues: List[str] = []
        if not self.title:
            issues.append("请为分析任务设置标题")
        issues.extend(self.audience.validate())
        issues.extend(self.big_idea.validate())
        if self.mechanism not in MECHANISMS:
            issues.append(f"沟通机制 '{self.mechanism}' 不在可选值中: {MECHANISMS}")
        if not self.three_min_story:
            issues.append("请撰写3分钟故事：如果只有3分钟，你会告诉受众什么？")
        if not self.call_to_action:
            issues.append("请明确行动号召：受众需要知道或做什么？")
        if not self.supporting_data:
            issues.append("请识别支撑数据：什么数据可以证明你的观点？")
        return issues


class ContextBuilder:
    """上下文分析构建器"""

    def __init__(self, title: str):
        self._analysis = ContextAnalysis(title=title)

    def set_audience(self, primary: str, decision_maker: str = "",
                     knowledge_level: str = "general",
                     relationship: str = "first_contact",
                     biases: str = "", motivation: str = "") -> "ContextBuilder":
        self._analysis.audience = AudienceProfile(
            primary_audience=primary, decision_maker=decision_maker,
            knowledge_level=knowledge_level, relationship=relationship,
            biases=biases, motivation=motivation,
        )
        return self

    def set_mechanism(self, mechanism: str, tone: str = "neutral") -> "ContextBuilder":
        self._analysis.mechanism = mechanism
        self._analysis.tone = tone
        return self

    def set_three_min_story(self, story: str) -> "ContextBuilder":
        self._analysis.three_min_story = story
        return self

    def set_big_idea(self, unique_point: str, stakes: str,
                     full_sentence: str) -> "ContextBuilder":
        self._analysis.big_idea = BigIdea(
            unique_point_of_view=unique_point, stakes=stakes,
            full_sentence=full_sentence,
        )
        return self

    def add_supporting_data(self, data: str) -> "ContextBuilder":
        self._analysis.supporting_data.append(data)
        return self

    def add_risk(self, risk: str) -> "ContextBuilder":
        self._analysis.risks.append(risk)
        return self

    def set_call_to_action(self, cta: str) -> "ContextBuilder":
        self._analysis.call_to_action = cta
        return self

    def build(self) -> ContextAnalysis:
        return self._analysis

    @staticmethod
    def render_markdown(ctx: ContextAnalysis) -> str:
        issues = ctx.validate()
        warnings = ""
        if issues:
            items = "\n".join(f"- ⚠️ {i}" for i in issues)
            warnings = f"\n## ⚠️ 待完善项\n{items}\n"

        data_list = "\n".join(f"- {d}" for d in ctx.supporting_data) if ctx.supporting_data else "- （未指定）"
        risk_list = "\n".join(f"- {r}" for r in ctx.risks) if ctx.risks else "- （未指定）"

        return f"""# 📋 上下文分析报告：{ctx.title}
{warnings}
## 受众画像
| 维度 | 内容 |
|------|------|
| 主要受众 | {ctx.audience.primary_audience or '（未指定）'} |
| 决策者 | {ctx.audience.decision_maker or '（未指定）'} |
| 了解程度 | {ctx.audience.knowledge_level} |
| 关系状态 | {ctx.audience.relationship} |
| 偏见/倾向 | {ctx.audience.biases or '（未指定）'} |
| 动机 | {ctx.audience.motivation or '（未指定）'} |

## 沟通机制
- **形式**: {ctx.mechanism}
- **语气**: {ctx.tone}

## 核心信息

### 3分钟故事
{ctx.three_min_story or '（未撰写）'}

### 大创意 (Big Idea)
> {ctx.big_idea.render() or '（未提炼）'}

- **独特观点**: {ctx.big_idea.unique_point_of_view or '（未指定）'}
- **利害关系**: {ctx.big_idea.stakes or '（未指定）'}

### 支撑数据
{data_list}

### 风险与反面证据
{risk_list}

## 行动号召
{ctx.call_to_action or '（未指定）'}
"""
