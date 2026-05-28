#!/usr/bin/env python3
"""Example: Building a 3-Act Data Narrative."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from swd import SWDSkill

swd = SWDSkill("Q4 Metrics Report")

print("=" * 60)
print("Data Story: Q4 Revenue Analysis")
print("=" * 60)

story = swd.build_story(
    protagonist="Leadership Team",
    imbalance="Cloud services revenue grew 45% YoY but CAC doubled",
    evidence=[
        "Cloud revenue: $12.5M (↑45% YoY)",
        "Customer acquisition cost: $2,400 (↑100% from $1,200)",
        "Retention rate: 78% (target: 85%)"
    ],
    call_to_action="Reinvest $2M from acquisition to retention programs"
)
print(story)

# Context analysis
print("\n" + "=" * 60)
print("Context Analysis")
print("=" * 60)

context = swd.build_context(
    audience="executives",
    cta="Approve retention investment plan",
    knowledge_level="executive"
)
print(context)
