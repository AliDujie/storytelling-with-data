"""SWD Skill 工具模块 - 知识库加载与文本工具"""

from typing import Dict, List

from .config import KNOWLEDGE_BASE_DIR, KNOWLEDGE_FILES


def load_knowledge(topic: str) -> str:
    """加载指定主题的知识库文档。

    Args:
        topic: 主题名称，必须是 KNOWLEDGE_FILES 中定义的键。

    Returns:
        知识库文档的文本内容。

    Raises:
        ValueError: 当 topic 不在 KNOWLEDGE_FILES 中时抛出。
    """
    fname = KNOWLEDGE_FILES.get(topic)
    if not fname:
        raise ValueError(f"未知主题: {topic}，可选: {list(KNOWLEDGE_FILES.keys())}")
    path = KNOWLEDGE_BASE_DIR / fname
    if not path.exists():
        return f"[知识库文件 {fname} 不存在，请确认文件路径]"
    return path.read_text(encoding="utf-8")


def load_all_knowledge() -> Dict[str, str]:
    """加载全部知识库文档。

    Returns:
        以主题名为键、文档内容为值的字典。
    """
    return {topic: load_knowledge(topic) for topic in KNOWLEDGE_FILES}


def search_knowledge(keyword: str) -> Dict[str, List[str]]:
    """在知识库中搜索关键词，返回包含该关键词的段落。

    Args:
        keyword: 要搜索的关键词（大小写不敏感）。

    Returns:
        以主题名为键、匹配段落列表为值的字典。
    """
    results: Dict[str, List[str]] = {}
    for topic in KNOWLEDGE_FILES:
        try:
            content = load_knowledge(topic)
        except Exception:
            continue
        paragraphs = content.split("\n\n")
        matches = [p.strip() for p in paragraphs if keyword.lower() in p.lower()]
        if matches:
            results[topic] = matches
    return results


def intensity_bar(value: int, max_val: int = 5) -> str:
    """生成强度条可视化。

    Args:
        value: 当前值（0 ~ max_val）。
        max_val: 最大值，默认 5。

    Returns:
        形如 ``████░░ 4/5`` 的字符串。
    """
    filled = "█" * value
    empty = "░" * (max_val - value)
    return f"{filled}{empty} {value}/{max_val}"


def score_badge(score: int, total: int = 100) -> str:
    """生成分数徽章。

    Args:
        score: 得分。
        total: 满分，默认 100。

    Returns:
        带有颜色 emoji 和等级文字的徽章字符串。
    """
    pct = score / total * 100 if total > 0 else 0
    if pct >= 90:
        return f"🟢 {score}/{total} 卓越"
    if pct >= 70:
        return f"🟡 {score}/{total} 良好"
    if pct >= 50:
        return f"🟠 {score}/{total} 需改进"
    return f"🔴 {score}/{total} 需重做"


def render_checklist(items: List[tuple]) -> str:
    """渲染检查清单。

    Args:
        items: 检查项列表，每项为 ``(name, passed: bool, note)`` 三元组。

    Returns:
        Markdown 格式的检查清单文本。
    """
    lines = []
    for name, passed, note in items:
        icon = "✅" if passed else "❌"
        line = f"- {icon} **{name}**"
        if note:
            line += f" — {note}"
        lines.append(line)
    return "\n".join(lines)
