# Installation Guide

## Quick Install (5 minutes)

### Option 1: Copy as AI Skill

```bash
# Copy to your AI Agent skills directory
cp -r skills/storytelling-with-data ~/.aoneclaw/skills/
```

### Option 2: Use as Python Package

No installation required! Just add the path in your code:

```python
import sys
sys.path.insert(0, "/path/to/storytelling-with-data")
from swd import SWDSkill

skill = SWDSkill("My Report")
```

### Option 3: Install via pip (Development)

```bash
# Clone the repository
git clone https://github.com/AliDujie/storytelling-with-data.git
cd storytelling-with-data

# Install in editable mode
pip install -e .
```

## System Requirements

- **Python**: >= 3.8
- **OS**: macOS / Linux / Windows
- **Dependencies**: None (pure Python standard library)

## Verify Installation

```python
from swd import SWDSkill

# Test initialization
skill = SWDSkill("Test Report")

# Test chart recommendation
rec = skill.recommend_chart(data_type="continuous", has_time=True)
print(f"✓ Installation successful! Chart recommendation: {rec}")
```

## Troubleshooting

### Issue: Module not found

**Solution**: Ensure the path is correct

```python
import sys
import os
sys.path.insert(0, os.path.abspath("/path/to/storytelling-with-data"))
```

### Issue: Import error

**Solution**: Check Python version

```bash
python --version  # Should be 3.8 or higher
```

## Next Steps

1. Read the [README.md](./README.md) for usage examples
2. Explore the [SKILL.md](./SKILL.md) for API documentation
3. Check the [knowledge base](./knowledge/) for storytelling principles

---

**Need help?** Open an issue on [GitHub](https://github.com/AliDujie/storytelling-with-data/issues)
