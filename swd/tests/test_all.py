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
        decision_maker="CTO",
        knowledge_level="general",
        relationship="established",
        mechanism="live_presentation",
        tone="serious",
        three_min_story="我们的用户增长在Q3放缓，需要投入新功能拉动增长。",
        big_idea="用户增长放缓的根本原因是新用户引导体验不佳，投入200万优化可在Q1恢复增长",
        big_idea_point="新用户引导体验是增长瓶颈",
        big_idea_stakes="不行动将导致Q1用户增长继续下滑15%",
        supporting_data=["新用户7日留存率从45%降至32%", "竞品首周体验NPS高出我们20分"],
        risks=["投入后效果可能需要2个季度才能显现"],
    )

    # 断言：返回字符串且包含关键内容
    assert isinstance(result, str), "build_context 应返回字符串"
    assert len(result) > 100, "报告内容不应为空"
    assert "产品VP" in result, "报告应包含受众信息"
    assert "批准200万" in result, "报告应包含行动号召"
    assert "CTO" in result, "报告应包含决策者"
    assert "上下文分析" in result, "报告应包含标题"
    assert "Big Idea" in result or "大创意" in result, "报告应包含Big Idea部分"
    assert "新用户7日留存率" in result, "报告应包含支撑数据"
    print("✅ test_build_context passed")


# ────────────────────────────────────────────
# 测试 2：图表选择推荐
# ────────────────────────────────────────────
def test_recommend_chart():
    skill = SWDSkill("销售分析")

    # 场景A：时间趋势数据（多系列多类别）→ 应推荐折线图
    result_line = skill.recommend_chart(
        data_type="continuous", has_time=True, series_count=2, category_count=12
    )
    assert isinstance(result_line, str), "recommend_chart 应返回字符串"
    assert "折线图" in result_line or "Line" in result_line, "时间趋势应推荐折线图"

    # 场景B：分类数据+长类别名 → 应推荐水平柱状图
    result_bar = skill.recommend_chart(
        data_type="categorical", category_count=8, category_names_long=True
    )
    assert "水平柱状图" in result_bar or "Horizontal" in result_bar, "长类别名应推荐水平柱状图"

    # 场景C：用户提出使用饼图 → 应给出避免警告
    result_pie = skill.recommend_chart(
        data_type="categorical", category_count=5, proposed_chart="pie"
    )
    assert "避免" in result_pie or "⛔" in result_pie or "⚠️" in result_pie, "饼图应触发避免警告"

    # 场景D：两个时间点比较（多系列）→ 应推荐坡度图
    result_slope = skill.recommend_chart(
        data_type="continuous", has_time=True, compare_two_points=True,
        series_count=3, category_count=2,
    )
    assert "坡度图" in result_slope or "Slopegraph" in result_slope, "两点比较应推荐坡度图"

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
        gestalt_issues=[
            ("proximity", "标签离数据太远", "缩小标签与数据的间距"),
        ],
        alignment_issues=["标题居中对齐，未与数据对齐"],
        whitespace_issues=["图表被拉伸填满整个页面"],
    )

    assert isinstance(result, str), "diagnose_clutter 应返回字符串"
    assert "去杂乱" in result or "诊断" in result, "报告应包含标题"
    # 检测到6个杂乱元素
    assert "3D" in result or "3d" in result, "应检测到3D效果"
    assert "对角" in result, "应检测到对角文本"
    assert "图例" in result or "legend" in result, "应检测到独立图例"
    # 格式塔建议
    assert "邻近性" in result or "proximity" in result, "应包含格式塔建议"
    # 六步骤
    assert "六步" in result or "步骤" in result, "应包含去杂乱步骤"
    # 对齐和白空间问题
    assert "居中" in result, "应包含对齐问题"
    assert "拉伸" in result, "应包含白空间问题"

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
            ("轴标签", 1),
        ],
        color_strategy="grey_plus_one",
        accent_color="蓝色 (#0070C0)",
        hierarchy=[
            (1, ["流失率趋势线", "关键数字"], "大号+粗体+蓝色"),
            (2, ["行业基准线"], "中号+深灰+虚线"),
            (3, ["轴标签", "数据来源"], "小号+浅灰"),
        ],
    )

    assert isinstance(result, str), "plan_attention 应返回字符串"
    assert "注意力" in result or "焦点" in result, "报告应包含标题"
    assert "流失率趋势线" in result, "应包含焦点元素"
    assert "灰色" in result or "grey" in result, "应包含颜色策略"
    assert "Level" in result or "层次" in result, "应包含视觉层次"
    # 眼睛诊断
    assert "眼睛" in result or "✅" in result, "应包含眼睛诊断结果"
    # 前注意属性建议
    assert "前注意" in result or "属性" in result, "应包含前注意属性建议"

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
    assert "卓越" in result_good or "🟢" in result_good, "全部通过应评为卓越"

    # 场景B：大部分未通过
    result_bad = skill.evaluate_design(
        has_title=False, has_axis_titles=False, has_action_title=False,
        color_strategic=False, alignment_clean=False,
    )
    assert "需重做" in result_bad or "🔴" in result_bad or "需改进" in result_bad or "🟠" in result_bad, \
        "多项未通过应评为需改进或需重做"
    assert "改进" in result_bad or "建议" in result_bad, "应包含改进建议"

    print("✅ test_evaluate_design passed")


# ────────────────────────────────────────────
# 测试 6：数据故事构建
# ────────────────────────────────────────────
def test_build_story():
    skill = SWDSkill("用户增长策略汇报")
    result = skill.build_story(
        protagonist="产品委员会",
        imbalance="新用户增长率连续3个月下降，从月均15%降至8%",
        setting="2024年公司进入成熟期，获客成本持续上升",
        desired_balance="恢复月均15%的新用户增长率",
        evidence=[
            "新用户首周留存率从45%降至32%",
            "竞品A的首周引导体验NPS高出我们20分",
            "内部A/B测试显示优化引导流程可提升留存12%",
        ],
        call_to_action="批准200万预算用于Q1新用户引导体验优化",
        narrative_flow="lead_with_ending",
        bing="我们建议投入200万优化新用户引导，预计Q1恢复增长",
        bang="数据显示新用户留存是增长瓶颈，竞品已领先",
        bongo="投入200万优化引导体验，Q1恢复15%月均增长",
        slide_titles=[
            "新用户增长率连续3月下降至8%",
            "根因：首周留存率从45%骤降至32%",
            "竞品首周体验NPS高出我们20分",
            "A/B测试证明优化引导可提升留存12%",
            "建议：投入200万在Q1优化新用户引导体验",
        ],
    )

    assert isinstance(result, str), "build_story 应返回字符串"
    assert "数据故事" in result or "故事" in result, "报告应包含标题"
    assert "产品委员会" in result, "应包含主角"
    assert "下降" in result, "应包含冲突描述"
    assert "200万" in result, "应包含行动号召"
    assert "Bing" in result or "预告" in result, "应包含BBB结构"
    assert "幻灯片" in result or "标题" in result, "应包含幻灯片标题序列"

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
    # 检查总分（各项加起来 = 4+3+2+4+5+5+5+4+3+5+4+3+2+3+2+3+4+4+3+2 = 70）
    assert "70" in result, f"总分应为70，报告内容: {result[:200]}"
    # 检查评级（70/100 = 70% → 良好）
    assert "良好" in result or "🟡" in result, "70分应评为良好"
    # 检查改进建议（得分<=2的项应出现在建议中）
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
            "无标题",
            "彩虹色配色方案",
            "独立图例放在底部",
            "对角文本标签",
        ],
        chart_type="水平柱状图",
        title="客户满意度最高的三个功能贡献了75%的好评",
        color_accent="蓝色",
        narrative_slides=[
            ("整体满意度达到82%，高于行业均值", "先展示好消息建立信任"),
            ("但功能C和D的满意度显著低于平均", "用橙色强调问题区域"),
            ("建议优先优化功能C的用户体验", "给出明确行动号召"),
        ],
    )

    assert isinstance(result, str), "makeover 应返回字符串"
    assert "改造" in result, "报告应包含标题"
    # 检查问题识别
    assert "饼图" in result, "应识别饼图问题"
    assert "彩虹" in result, "应识别彩虹色问题"
    # 检查改造步骤
    assert "步骤" in result or "Step" in result, "应包含改造步骤"
    assert "水平柱状图" in result, "应包含替代方案"
    # 检查设计规范
    assert "设计规范" in result or "规范" in result, "应包含设计规范"
    # 检查叙事幻灯片
    assert "幻灯片" in result, "应包含叙事幻灯片序列"
    assert "82%" in result, "应包含幻灯片内容"

    print("✅ test_makeover passed")


# ────────────────────────────────────────────
# 测试 9：CEO 决策方法 1 - 决策选项对比
# ────────────────────────────────────────────
def test_build_decision_comparison():
    skill = SWDSkill("季度业绩汇报")

    # 场景 A：使用默认选项
    result_default = skill.build_decision_comparison()
    assert isinstance(result_default, str), "build_decision_comparison 应返回字符串"
    assert "CEO 决策选项对比" in result_default or "决策" in result_default, "应包含决策对比标题"
    assert "方案" in result_default, "应包含方案选项"
    assert "投入" in result_default or "成本" in result_default, "应包含投入维度"
    assert "风险" in result_default, "应包含风险维度"
    assert "回报" in result_default, "应包含回报维度"
    assert "推荐" in result_default, "应包含推荐方案"

    # 场景 B：自定义选项
    result_custom = skill.build_decision_comparison(options=[
        {"name": "方案 A: 快速上线", "investment": "50 万", "timeline": "4 周", "risk": "高", "return": "中", "confidence": "高"},
        {"name": "方案 B: 稳健推进", "investment": "100 万", "timeline": "8 周", "risk": "中", "return": "高", "confidence": "中"},
    ])
    assert "快速上线" in result_custom, "应包含自定义方案名"
    assert "50 万" in result_custom, "应包含自定义投入"
    assert "决策矩阵" in result_custom, "应包含决策矩阵"

    print("✅ test_build_decision_comparison passed")


# ────────────────────────────────────────────
# 测试 10：CEO 决策方法 2 - 执行风险可视化
# ────────────────────────────────────────────
def test_visualize_execution_risks():
    skill = SWDSkill("产品上线计划")

    # 场景 A：使用默认上下文
    result_default = skill.visualize_execution_risks()
    assert isinstance(result_default, str), "visualize_execution_risks 应返回字符串"
    assert "执行风险" in result_default or "风险" in result_default, "应包含风险标题"
    assert "风险矩阵" in result_default or "矩阵" in result_default, "应包含风险矩阵"
    assert "概率" in result_default, "应包含概率维度"
    assert "影响" in result_default, "应包含影响维度"
    assert "缓解" in result_default or "措施" in result_default, "应包含缓解措施"

    # 场景 B：自定义上下文
    result_custom = skill.visualize_execution_risks(context={
        "timeline": "12 周",
        "team_size": 8,
        "dependencies": ["技术团队", "设计团队", "市场团队"],
    })
    assert "12 周" in result_custom, "应包含自定义时间"
    assert "8 人" in result_custom or "8 人" in result_custom or "团队规模" in result_custom, "应包含自定义团队规模"
    assert "市场团队" in result_custom, "应包含自定义依赖"

    print("✅ test_visualize_execution_risks passed")


# ────────────────────────────────────────────
# 测试 11：CEO 决策方法 3 - 决策框架生成
# ────────────────────────────────────────────
def test_generate_decision_framework():
    skill = SWDSkill("战略投资决策")

    # 场景 A：Go/No-Go 决策框架
    result_gono = skill.generate_decision_framework("go_no_go")
    assert isinstance(result_gono, str), "generate_decision_framework 应返回字符串"
    assert "Go/No-Go" in result_gono or "决策框架" in result_gono, "应包含 Go/No-Go 框架标题"
    assert "战略一致性" in result_gono or "标准" in result_gono, "应包含决策标准"
    assert "阈值" in result_gono or "Threshold" in result_gono, "应包含决策阈值"
    assert "决策记录" in result_gono or "模板" in result_gono, "应包含决策记录模板"

    # 场景 B：优先级决策框架
    result_priority = skill.generate_decision_framework("priority")
    assert "优先级" in result_priority or "Priority" in result_priority, "应包含优先级框架"
    assert "影响力" in result_priority, "应包含影响力标准"
    assert "紧急性" in result_priority, "应包含紧急性标准"

    # 场景 C：资源分配决策框架
    result_resource = skill.generate_decision_framework("resource_allocation")
    assert "资源分配" in result_resource, "应包含资源分配框架"
    assert "机会成本" in result_resource, "应包含机会成本标准"
    assert "预期回报" in result_resource, "应包含预期回报标准"

    # 场景 D：风险接受决策框架
    result_risk = skill.generate_decision_framework("risk_acceptance")
    assert "风险接受" in result_risk or "风险" in result_risk, "应包含风险接受框架"
    assert "发生概率" in result_risk, "应包含概率标准"
    assert "缓解成本" in result_risk, "应包含缓解成本标准"

    print("✅ test_generate_decision_framework passed")


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
        # CEO 视角方法测试
        test_build_decision_comparison,
        test_visualize_execution_risks,
        test_generate_decision_framework,
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
        print("🎉 全部 {len(tests)} 个测试用例通过!")
    else:
        print(f"⚠️ 有 {failed} 个测试未通过")
        sys.exit(1)
