#!/usr/bin/env python3
"""SWD Example 01: Chart Selection / 图表选择

Demonstrates chart type recommendation based on data characteristics.
根据数据特征推荐图表类型。

Run: python 01_chart_selection.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from swd import SWDSkill

print("=" * 60)
print("SWD Example 01: Chart Selection")
print("示例 01：图表选择")
print("=" * 60)

skill = SWDSkill("Q4 Metrics Dashboard")

# ── Scenario 1: Time series data ──
print("\n📊 Scenario: Monthly revenue over 12 months (continuous + time)")
print("📊 场景：12 个月月收入数据（连续+时间）")
print("-" * 50)
rec = skill.recommend_chart(data_type='continuous', has_time=True)
print(rec[:500])
print("...\n")

# ── Scenario 2: Category comparison ──
print("\n📊 Scenario: Sales by region (categorical comparison)")
print("📊 场景：各地区销售额对比（分类对比）")
print("-" * 50)
rec2 = skill.recommend_chart(data_type='categorical', has_time=False)
print(rec2[:500])
print("...\n")

# ── Scenario 3: Part-to-whole ──
print("\n📊 Scenario: Market share breakdown (part-to-whole)")
print("📊 场景：市场份额占比（部分与整体）")
print("-" * 50)
rec3 = skill.recommend_chart(data_type='part_to_whole')
print(rec3[:500])
print("...\n")

print("✅ Tip: Choose charts based on data type, not aesthetics.")
print("✅ 提示：根据数据类型选择图表，而非外观。")
