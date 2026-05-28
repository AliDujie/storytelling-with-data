#!/usr/bin/env python3
"""Example: Declutter Diagnosis for a dashboard chart."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from swd import SWDSkill

swd = SWDSkill("Sales Dashboard")

print("=" * 60)
print("Declutter Diagnosis: Monthly Revenue Chart")
print("=" * 60)

diagnosis = swd.diagnose_clutter(
    has_gridlines=True,
    has_3d=True,
    has_separate_legend=True,
    has_data_markers=True,
    has_background_shading=True
)
print(diagnosis)

# Attention guidance
print("\n" + "=" * 60)
print("Attention Guidance")
print("=" * 60)

attention = swd.plan_attention(
    focus_elements=[("Cloud Services performance", 5)]
)
print(attention)
