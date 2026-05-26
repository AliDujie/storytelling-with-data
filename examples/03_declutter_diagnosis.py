#!/usr/bin/env python3
"""Example: Declutter Diagnosis for a dashboard chart."""
from swd import SWDSkill

swd = SWDSkill("Sales Dashboard")

print("=" * 60)
print("Declutter Diagnosis: Monthly Revenue Chart")
print("=" * 60)

diagnosis = swd.declutter_diagnosis(
    chart_type="line",
    description="""
    Multi-line chart showing monthly revenue for 5 product lines.
    Has: gridlines on both axes, 3D effects on bars, legend on right,
    data labels on every point, shadow effects, gradient fill.
    """
)
print(diagnosis)

# Attention guidance
print("\n" + "=" * 60)
print("Attention Guidance")
print("=" * 60)

attention = swd.guide_attention(
    "Highlight that Cloud Services exceeded target while Enterprise declined",
    pre_attentive=["color", "size", "position"]
)
print(attention)
