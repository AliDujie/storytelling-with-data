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
