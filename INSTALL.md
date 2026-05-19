# Installation Guide / 安装指南

## Quick Install (5 minutes) / 快速安装（5 分钟）

### Option 1: Copy as AI Skill / 方式一：作为 AI 技能安装

```bash
# Copy to your AI Agent skills directory / 复制到你的 AI Agent 技能目录
cp -r storytelling-with-data ~/.openclaw/skills/
```

### Option 2: Use as Python Package / 方式二：作为 Python 包使用

No installation required! Just add the path in your code:
无需安装！只需在代码中添加路径：

```python
import sys
sys.path.insert(0, "/path/to/storytelling-with-data")
from swd import SWDSkill

skill = SWDSkill("My Report")
```

### Option 3: Install via pip (Development) / 方式三：通过 pip 安装（开发模式）

```bash
# Clone the repository / 克隆仓库
git clone https://github.com/AliDujie/storytelling-with-data.git
cd storytelling-with-data

# Install in editable mode / 以可编辑模式安装
pip install -e .
```

## System Requirements / 系统要求

- **Python**: >= 3.8
- **OS**: macOS / Linux / Windows
- **Dependencies**: None (pure Python standard library) / 无外部依赖（纯 Python 标准库）

## Verify Installation / 验证安装

```python
from swd import SWDSkill

# Test initialization / 测试初始化
skill = SWDSkill("Test Report")

# Test chart recommendation / 测试图表推荐
rec = skill.recommend_chart(data_type="continuous", has_time=True)
print(f"✓ Installation successful! Chart recommendation: {rec}")
# ✓ 安装成功！图表推荐：{rec}
```

## Troubleshooting / 故障排查

### Issue: Module not found / 问题：找不到模块

**Solution**: Ensure the path is correct / **解决方案**：确保路径正确

```python
import sys
import os
sys.path.insert(0, os.path.abspath("/path/to/storytelling-with-data"))
```

### Issue: Import error / 问题：导入错误

**Solution**: Check Python version / **解决方案**：检查 Python 版本

```bash
python --version  # Should be 3.8 or higher / 应为 3.8 或更高版本
```

## Related Skills / 相关技能

This skill is part of the AliDujie UX Research ecosystem:
本技能是 AliDujie UX 研究生态系统的一部分：

- [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — UDM 研究结果可交给 SWD 进行数据叙事
- [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — QuantUX 分析结果可用 SWD 可视化
- [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — JTBD 分析结果可用 SWD 呈现
- [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — VPD 实验结果可用 SWD 数据叙事
- [Web Persona](https://github.com/AliDujie/web-persona-skill) — Persona 数据可用 SWD 可视化呈现

## Next Steps / 下一步

1. Read the [README.md](./README.md) for usage examples / 阅读 README.md 了解使用示例
2. Explore the [SKILL.md](./SKILL.md) for API documentation / 查看 SKILL.md 了解 API 文档
3. Check the [USAGE.md](./USAGE.md) for detailed workflows / 查看 USAGE.md 了解详细工作流
4. Check the [references/](./references/) directory for methodology guides / 查看 references/ 目录了解方法论指南
5. Run the tests: `python swd/tests/test_all.py` / 运行测试

## 🔗 Related Skills / 相关技能

This skill is part of the AliDujie UX Research ecosystem:
本技能是 AliDujie UX 研究生态系统的一部分：

| Skill | Role | Collaboration |
|-------|------|---------------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | Research methods | UDM findings → SWD storytelling |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | Statistical validation | A/B results → SWD makeover + narrative |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Needs discovery | JTBD scores → SWD context + report |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | User personas | Persona data → SWD chart selection |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | Value validation | VPD canvas → SWD visualization |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Strategy framework | SWD output → STM analysis |
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | Board presentations | SWD story → CEO board deck |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | Product strategy | SWD data → CPO portfolio strategy |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | Growth strategy | SWD metrics → CMO campaigns |
