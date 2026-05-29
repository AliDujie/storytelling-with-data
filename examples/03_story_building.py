#!/usr/bin/env python3
"""SWD Example 02: Story Building / 故事构建

Build a three-act data narrative with clear call-to-action.
构建三幕数据叙事并明确行动号召。

Run: python 02_story_building.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from swd import SWDSkill

print("=" * 60)
print("SWD Example 02: Story Building")
print("示例 02：故事构建")
print("=" * 60)

skill = SWDSkill("Q4 Retention Report")

# ── Scenario: Churn analysis story ──
print("\n📖 Scenario: Build a story about rising churn")
print("📖 场景：构建关于流失率上升的叙事")
print("-" * 50)
story = skill.build_story(
    protagonist="产品团队",
    imbalance="Q4 用户流失率上升了 15%",
    desired_balance="将流失率恢复到 Q3 水平（< 5%）",
    call_to_action="推出新用户引导流程 + 预警系统"
)
print(story[:600])
print("...\n")

# ── Context analysis for the story ──
print("\n🔍 Context Analysis / 上下文分析")
print("-" * 50)
ctx = skill.build_context(
    audience="产品副总裁",
    cta="批准新用户引导优化项目预算",
    decision_maker="产品副总裁",
    knowledge_level="general",
    mechanism="live_presentation"
)
print(ctx[:400])
print("...\n")

print("✅ Tip: Every data story needs a clear protagonist and call-to-action.")
print("✅ 提示：每个数据故事都需要清晰的主角和行动号召。")
