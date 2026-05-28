#!/usr/bin/env python3
"""Example: Chart Recommendation based on data characteristics."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from swd import SWDSkill

swd = SWDSkill("Quarterly Business Review")

# Scenario: Compare revenue across 5 business units
print("=" * 60)
print("Chart Recommendation: Compare 5 business units")
print("=" * 60)

recommendation = swd.recommend_chart(
    data_type="categorical",
    series_count=5,
    category_count=0
)
print(recommendation)

# Scenario: Show trend over 4 quarters
print("\n" + "=" * 60)
print("Chart Recommendation: Show quarterly trend")
print("=" * 60)

trend = swd.recommend_chart(
    data_type="continuous",
    series_count=1,
    has_time=True
)
print(trend)

# Scenario: Show part-to-whole distribution
print("\n" + "=" * 60)
print("Chart Recommendation: Part-to-whole breakdown")
print("=" * 60)

composition = swd.recommend_chart(
    data_type="categorical",
    series_count=4,
    show_part_of_whole=True
)
print(composition)
