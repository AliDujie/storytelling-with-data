# SWD 跨技能呈现指南

> 如何将其他技能的研究成果转化为高管可读的数据叙事

---

## SWD 在生态系统中的位置

SWD 是 7 技能工作流的 **数据呈现层**，是所有研究的最终出口：

```
Persona → JTBD → UDM → QuantUX → VPD → SWD (你在这里)
```

## 各技能 → SWD 的输入映射

| 来源技能 | 典型输入 | SWD 呈现方式 | 推荐图表 |
|---------|---------|-------------|---------|
| UDM | 研究发现、SUS/NPS、痛点列表 | 痛点优先级矩阵、旅程图 | 散点图、热力图 |
| QuantUX | A/B 测试结果、HEART 指标 | 趋势图、对比图 | 折线图、柱状图 |
| JTBD | 机会评分、四力分析 | 机会地图、竞争定位 | 气泡图、象限图 |
| VPD | 契合度评分、实验结果 | 画布概览、ROI 对比 | 雷达图、瀑布图 |
| Persona | 用户角色、行为数据 | 角色画像、行为对比 | 分组柱状图 |

## SWD 与 UDM：研究发现的叙事化

UDM 输出结构化的研究发现，SWD 将其转化为三幕叙事：

```
UDM 输出                    SWD 呈现
─────────                   ────────
3 个核心痛点      ──►       第一幕: 问题 (痛点严重性数据)
方法推荐          ──►       第二幕: 证据 (研究方法与样本)
SUS/NPS 评分     ──►       第三幕: 方案 (改善预期与ROI)
```

### 示例：UDM → SWD

```python
from udm import UDMSkill
from swd import SWDSkill

# UDM: 研究执行
udm = UDMSkill("旅行平台")
sus = udm.calculate_sus([3, 2, 4, 2, 3, 2, 4, 2, 3, 2])
nps = udm.calculate_nps([6, 5, 7, 4, 6, 5, 8, 3, 6, 7])

# SWD: 叙事构建
swd = SWDSkill("用户体验改进汇报")
swd.build_context(audience="产品 VP", cta="批准 Q3 优化预算")
swd.full_diagnosis({
    "clarity": 70, "attention": 65, "design": 60,
    "story": 75, "actionability": 80
})
# → 去杂乱 + 注意力引导 + 三幕叙事建议
```

## SWD 与 QuantUX：统计结果的可视化

QuantUX 输出统计检验结果，SWD 将其转化为直观的图表：

```
QuantUX 输出                SWD 呈现
────────────                ────────
A/B 测试: +12.3%, p<0.001  ──►  柱状图 (Before/After)
HEART 指标趋势              ──►  折线图 (4 季度趋势)
MaxDiff 偏好份额            ──►  水平条形图 (排名)
```

### 示例：QuantUX → SWD

```python
from quantux import QuantUXSkill
from swd import SWDSkill

# QuantUX: 统计分析
quantux = QuantUXSkill("旅行平台")
sample = quantux.calculate_ab_sample_size(baseline=0.08, mde=0.015)

# SWD: 结果呈现
swd = SWDSkill("A/B 测试汇报")
chart = swd.recommend_chart(
    data_type="comparison",
    category_count=2,
    has_time=True
)
# → 推荐: 分组柱状图 (含时间趋势)
```

## SWD 与 JTBD：机会洞察的故事化

JTBD 输出结构化的机会分析，SWD 将其转化为商业故事：

```
JTBD 输出                   SWD 呈现
─────────                   ────────
Opportunity Score: 8.2     ──►  气泡图 (重要性 vs 满意度)
四力分析结果                ──►  力场图 (推动力 vs 阻力)
Workaround 描述            ──►  流程图 (现有替代方案)
```

## SWD 与 VPD：价值主张的商业化呈现

VPD 输出价值主张实验结果，SWD 将其转化为投资叙事：

```
VPD 输出                    SWD 呈现
────────                    ────────
契合度评分: 0.78           ──►  仪表盘 (0-1 标度)
竞争战略画布                ──►  雷达图 (竞争维度对比)
商业化路径                  ──►  路线图 (3 阶段里程碑)
```

## SWD 与 Persona：角色数据的可视化

Persona 输出用户角色描述，SWD 将其转化为团队对齐材料：

```
Persona 输出                SWD 呈现
────────────                ────────
3 个角色 + 行为特征         ──►  角色卡片 (分组柱状图对比)
行为数据                    ──►  热力图 (行为 × 角色)
优先级 (Primary/Secondary)  ──►  堆叠图 (用户占比)
```

## SWD 叙事质量检查清单

在汇报前，用 SWD 自我诊断：

| 检查项 | 标准 | 如何验证 |
|--------|------|---------|
| 受众明确 | 知道给谁看 | `build_context(audience=...)` |
| 信息单一 | 一张图一个信息 | `diagnose_clutter()` |
| 重点突出 | 关键信息 3 秒可见 | `attention_guide()` |
| 故事完整 | 有起承转合 | `build_story(...)` 三幕结构 |
| 行动明确 | 看完知道要做什么 | CTA 清晰可执行 |

---

*本文档是 AliDujie Storytelling with Data 技能生态系统的补充参考。*
