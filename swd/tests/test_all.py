"""SWD Skill 完整测试套件

8 个独立测试用例，覆盖 SWDSkill 统一入口类的全部 8 大执行能力。
每个测试用例独立运行，包含明确断言，输出通过状态。

运行方式::

    cd storytelling-with-data-skill
    python -m pytest swd/tests/test_all.py -v
    # 或直接运行
    python swd/tests/test_all.py
"""

import sys
from pathlib import Path

# 确保项目根目录在 sys.path 中
_root = str(Path(__file__).resolve().parent.parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

from swd import SWDSkill


# ────────────────────────────────────────────
# 测试 1：上下文分析
# ────────────────────────────────────────────
def test_build_context():
    skill = SWDSkill("Q4业绩汇报")
    result = skill.build_context(
        audience="产品VP",
        cta="批准200万预算继续项目",
        big_idea="用户增长放缓的根本原因是新用户引导体验不佳，投入200万优化可在Q1恢复增长",
        three_min_story="我们的用户增长在Q3放缓，需要投入新功能拉动增长。",
        supporting_data=["新用户7日留存率从45%降至32%", "竞品首周体验NPS高出我们20分"],
        risks=["投入后效果可能需要2个季度才能显现"],
    )

    assert isinstance(result, str), "build_context 应返回字符串"
    assert len(result) > 100, "报告内容不应为空"
    assert "产品VP" in result, "报告应包含受众信息"
    assert "200万" in result or "批准" in result, "报告应包含行动号召相关信息"
    assert "上下文分析" in result or "Context" in result, "报告应包含标题"
    print("✅ test_build_context passed")


# ────────────────────────────────────────────
# 测试 2：图表选择推荐
# ────────────────────────────────────────────
def test_recommend_chart():
    skill = SWDSkill("销售分析")

    # 场景A：时间趋势数据 → 应推荐折线图
    result_line = skill.recommend_chart(
        data_type="continuous", has_time=True, series_count=2, category_count=12
    )
    assert isinstance(result_line, str), "recommend_chart 应返回字符串"
    assert len(result_line) > 20, "报告内容不应为空"
    assert "折线图" in result_line or "Line" in result_line, "时间趋势应推荐折线图"

    # 场景B：分类数据+长类别名 → 应推荐水平柱状图
    result_bar = skill.recommend_chart(
        data_type="categorical", category_count=8, category_names_long=True
    )
    assert "水平柱状图" in result_bar or "Horizontal" in result_bar, "长类别名应推荐水平柱状图"

    print("✅ test_recommend_chart passed")


# ────────────────────────────────────────────
# 测试 3：去杂乱诊断
# ────────────────────────────────────────────
def test_diagnose_clutter():
    skill = SWDSkill("月度报告")
    result = skill.diagnose_clutter(
        has_border=True,
        has_gridlines=True,
        has_3d=True,
        has_diagonal_text=True,
        has_separate_legend=True,
        has_trailing_zeros=True,
    )

    assert isinstance(result, str), "diagnose_clutter 应返回字符串"
    assert len(result) > 100, "报告内容不应为空"
    assert "3D" in result.lower() or "3d" in result, "应检测到3D效果"
    assert "图例" in result or "legend" in result.lower(), "应检测到图例问题"

    print("✅ test_diagnose_clutter passed")


# ────────────────────────────────────────────
# 测试 4：注意力引导规划
# ────────────────────────────────────────────
def test_plan_attention():
    skill = SWDSkill("用户流失分析")
    result = skill.plan_attention(
        focus_elements=[
            ("流失率趋势线", 5),
            ("行业基准线", 2),
        ],
        hierarchy=[
            (1, ["流失率趋势线"], "大号+粗体+蓝色"),
            (2, ["行业基准线"], "中号+深灰"),
        ],
    )

    assert isinstance(result, str), "plan_attention 应返回字符串"
    assert len(result) > 50, "报告内容不应为空"
    assert "流失率" in result, "应包含焦点元素"

    print("✅ test_plan_attention passed")


# ────────────────────────────────────────────
# 测试 5：设计评估
# ────────────────────────────────────────────
def test_evaluate_design():
    skill = SWDSkill("产品仪表盘")

    # 场景A：大部分通过
    result_good = skill.evaluate_design(
        has_title=True, has_axis_titles=True, has_action_title=True,
        has_annotations=True, color_strategic=True, alignment_clean=True,
        whitespace_ok=True, hierarchy_clear=True,
        highlight_limited=True, distractions_removed=True,
    )
    assert isinstance(result_good, str), "evaluate_design 应返回字符串"
    assert len(result_good) > 50, "报告内容不应为空"

    # 场景B：多项未通过
    result_bad = skill.evaluate_design(
        has_title=False, has_axis_titles=False, has_action_title=False,
        color_strategic=False, alignment_clean=False,
    )
    assert "建议" in result_bad or "改进" in result_bad or "需" in result_bad or "❌" in result_bad, \
        "多项未通过应包含改进建议或警告"

    print("✅ test_evaluate_design passed")


# ────────────────────────────────────────────
# 测试 6：数据故事构建
# ────────────────────────────────────────────
def test_build_story():
    skill = SWDSkill("用户增长策略汇报")
    result = skill.build_story(
        protagonist="产品委员会",
        imbalance="新用户增长率连续3个月下降，从月均15%降至8%",
        evidence=[
            "新用户首周留存率从45%降至32%",
            "竞品A的首周引导体验NPS高出我们20分",
        ],
        call_to_action="批准200万预算用于Q1新用户引导体验优化",
    )

    assert isinstance(result, str), "build_story 应返回字符串"
    assert len(result) > 100, "报告内容不应为空"
    assert "产品委员会" in result, "应包含主角"
    assert "下降" in result or "减少" in result, "应包含冲突描述"
    assert "批准" in result or "200万" in result, "应包含行动号召相关内容"

    print("✅ test_build_story passed")


# ────────────────────────────────────────────
# 测试 7：可视化综合诊断
# ────────────────────────────────────────────
def test_full_diagnosis():
    skill = SWDSkill("季度销售图表")
    result = skill.full_diagnosis(scores={
        "context": {
            "audience_clear": 4,
            "cta_clear": 3,
            "big_idea_visible": 2,
            "data_supports_story": 4,
        },
        "visual_choice": {
            "chart_type_fit": 5,
            "avoid_bad_charts": 5,
            "zero_baseline": 5,
            "logical_order": 4,
        },
        "clutter": {
            "no_unnecessary_elements": 3,
            "no_diagonal_text": 5,
            "whitespace_ok": 4,
            "no_redundancy": 3,
        },
        "attention": {
            "preattentive_used": 2,
            "color_sparse": 3,
            "visual_hierarchy": 2,
            "eyes_drawn_test": 3,
        },
        "design_narrative": {
            "text_sufficient": 4,
            "alignment_aesthetic": 4,
            "narrative_structure": 3,
            "action_titles": 2,
        },
    })

    assert isinstance(result, str), "full_diagnosis 应返回字符串"
    assert "诊断" in result, "报告应包含标题"
    assert "改进" in result or "建议" in result, "应包含改进建议"

    print("✅ test_full_diagnosis passed")


# ────────────────────────────────────────────
# 测试 8：图表改造
# ────────────────────────────────────────────
def test_makeover():
    skill = SWDSkill("客户满意度报告")
    result = skill.makeover(
        issues=[
            "使用了饼图展示5个类别的满意度分布",
            "彩虹色配色方案",
            "独立图例放在底部",
        ],
    )

    assert isinstance(result, str), "makeover 应返回字符串"
    assert len(result) > 50, "报告内容不应为空"

    print("✅ test_makeover passed")


# ────────────────────────────────────────────
# 测试 9：决策对比 (便捷方法)
# ────────────────────────────────────────────
def test_build_decision_comparison():
    skill = SWDSkill("战略决策分析")

    # 测试默认选项
    result_default = skill.build_decision_comparison()
    assert isinstance(result_default, str), "build_decision_comparison 应返回字符串"
    assert len(result_default) > 50, "报告内容不应为空"

    # 测试自定义选项
    result_custom = skill.build_decision_comparison(
        title="方案评估",
        option_a="自建团队",
        option_b="外包合作",
        criteria=["成本", "速度", "质量"],
    )
    assert isinstance(result_custom, str), "build_decision_comparison 应返回字符串"
    assert "自建团队" in result_custom, "应包含自定义方案A"
    assert "外包合作" in result_custom, "应包含自定义方案B"

    print("✅ test_build_decision_comparison passed")


# ────────────────────────────────────────────
# 主入口
# ────────────────────────────────────────────
if __name__ == "__main__":
    tests = [
        test_build_context,
        test_recommend_chart,
        test_diagnose_clutter,
        test_plan_attention,
        test_evaluate_design,
        test_build_story,
        test_full_diagnosis,
        test_makeover,
        test_build_decision_comparison,
    ]

    passed = 0
    failed = 0
    for test_fn in tests:
        try:
            test_fn()
            passed += 1
        except Exception as e:
            failed += 1
            print(f"❌ {test_fn.__name__} FAILED: {e}")

    print(f"\n{'='*50}")
    print(f"测试结果: {passed} passed, {failed} failed, {len(tests)} total")
    if failed == 0:
        print("🎉 全部 9 个测试用例通过!")
    else:
        print(f"⚠️ 有 {failed} 个测试未通过")
        sys.exit(1)
