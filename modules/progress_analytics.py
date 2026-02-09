def analyze_progress(
    streak_days: int,
    avg_mood: int,
    avg_engagement: int
):
    """
    Analyzes behavioral progress trends.
    Returns a human-readable insight.
    """
    # Safety clamps
    streak_days = max(0, streak_days)
    avg_mood = min(max(avg_mood, 1), 5)
    avg_engagement = min(max(avg_engagement, 0), 10)

    if streak_days >= 7 and avg_mood >= 4 and avg_engagement >= 7:
        return "🚀 Strong positive progress. Current therapy approach is effective."

    if streak_days >= 3 and avg_engagement >= 5:
        return "📈 Moderate improvement observed. Consistency is helping."

    if avg_mood <= 2:
        return "💙 Emotional challenges detected. Consider lighter, play-based sessions."

    if streak_days == 0:
        return "⏳ No recent therapy data. Begin small daily routines."

    return "🔍 Progress is stable. Continue monitoring and adjusting gradually."