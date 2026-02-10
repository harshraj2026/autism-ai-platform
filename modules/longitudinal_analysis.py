def analyze_longitudinal_trends(
    past_streaks: list,
    past_moods: list,
    past_engagements: list
):
    """
    Detects behavioral trends over time.
    This is NOT a diagnostic evaluation.
    """

    insights = []

    if len(past_streaks) < 3:
        return ["📊 Not enough historical data yet to detect trends."]

    # 🔁 Consistency Trend
    if past_streaks[-1] > past_streaks[0]:
        insights.append("📈 Therapy consistency is improving over time.")
    elif past_streaks[-1] < past_streaks[0]:
        insights.append("📉 Therapy consistency has declined recently.")

    # 😊 Mood Trend
    if sum(past_moods[-3:]) / 3 > sum(past_moods[:3]) / 3:
        insights.append("🙂 Emotional regulation shows gradual improvement.")
    elif sum(past_moods[-3:]) / 3 < sum(past_moods[:3]) / 3:
        insights.append("💙 Emotional challenges increased in recent days.")

    # ⚡ Engagement Trend
    if sum(past_engagements[-3:]) / 3 > sum(past_engagements[:3]) / 3:
        insights.append("🎯 Engagement levels are trending upward.")
    elif sum(past_engagements[-3:]) / 3 < sum(past_engagements[:3]) / 3:
        insights.append("🛑 Engagement has reduced — consider adjusting activities.")

    if not insights:
        insights.append("📋 No significant behavioral trend detected yet.")

    return insights
