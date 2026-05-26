#!/usr/bin/env python3
"""Example: Building a 3-Act Data Narrative."""
from swd import SWDSkill

swd = SWDSkill("Q4 Metrics Report")

print("=" * 60)
print("Data Story: Q4 Revenue Analysis")
print("=" * 60)

story = swd.build_story(
    audience="executives",
    core_message="Cloud services revenue grew 45% YoY but CAC doubled",
    evidence=[
        "Cloud revenue: $12.5M (↑45% YoY)",
        "Customer acquisition cost: $2,400 (↑100% from $1,200)",
        "Retention rate: 78% (target: 85%)"
    ]
)
print(story)

# Context analysis
print("\n" + "=" * 60)
print("Context Analysis")
print("=" * 60)

context = swd.analyze_context(
    "What is your audience's biggest concern about cloud revenue growth?"
)
print(context)
