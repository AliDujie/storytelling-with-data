#!/usr/bin/env python3
"""Example: Chart Recommendation based on data characteristics."""
from swd import SWDSkill

swd = SWDSkill("Quarterly Business Review")

# Scenario: Compare revenue across 5 business units
print("=" * 60)
print("Chart Recommendation: Compare 5 business units")
print("=" * 60)

recommendation = swd.recommend_chart(
    "compare",
    ["Cloud Services", "Enterprise Software", "Consumer Apps",
     "Advertising", "Hardware"],
    [12.5, 8.3, 5.1, 3.2, 2.8]
)
print(recommendation)

# Scenario: Show trend over 4 quarters
print("\n" + "=" * 60)
print("Chart Recommendation: Show quarterly trend")
print("=" * 60)

trend = swd.recommend_chart(
    "trend",
    ["Q1", "Q2", "Q3", "Q4"],
    [45, 52, 48, 61]
)
print(trend)

# Scenario: Show part-to-whole distribution
print("\n" + "=" * 60)
print("Chart Recommendation: Part-to-whole breakdown")
print("=" * 60)

composition = swd.recommend_chart(
    "proportion",
    ["Product A", "Product B", "Product C", "Other"],
    [35, 28, 22, 15]
)
print(composition)
