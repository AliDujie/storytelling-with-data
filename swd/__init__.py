"""Storytelling with Data (SWD) Python Toolkit

基于 Cole Nussbaumer Knaflic《Storytelling with Data》的完整数据可视化工具包。
覆盖 SWD 六课体系的 8 大执行能力。

快速开始::

    from swd import SWDSkill
    skill = SWDSkill("季度业绩汇报")

    # 能力1: 上下文分析
    ctx = skill.build_context(audience="产品VP", cta="批准新功能投入")

    # 能力2: 图表选择
    rec = skill.recommend_chart(data_type="continuous", has_time=True)

    # 能力3: 去杂乱诊断
    clutter = skill.diagnose_clutter(has_border=True, has_gridlines=True)

    # 能力4: 注意力引导
    attn = skill.plan_attention(focus_elements=[("关键指标", 5)])

    # 能力5: 设计评估
    design = skill.evaluate_design(has_title=True, color_strategic=False)

    # 能力6: 故事构建
    story = skill.build_story(protagonist="产品团队", imbalance="用户流失加剧")

    # 能力7: 综合诊断
    diag = skill.full_diagnosis(scores={"context": {"audience_clear": 4}})

    # 能力8: 图表改造
    makeover = skill.makeover(issues=["使用了饼图", "无标题"])
"""

__version__ = "2.2.141"
