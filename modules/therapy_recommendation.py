def recommend_therapy(
    screening_score: int,
    avg_mood: int,
    avg_engagement: int,
    streak_days: int
):
    """
    Generates personalized therapy guidance.
    This is NOT a treatment plan or diagnosis.
    """

    recommendations = []

    # 🔴 Higher Support Needed
    if screening_score < 50:
        recommendations.append(
            "🧩 Focus on short, structured interaction sessions (5–10 minutes)."
        )
        recommendations.append(
            "👀 Encourage eye contact through play-based activities."
        )

    # 🟡 Moderate Support
    if 50 <= screening_score < 75:
        recommendations.append(
            "🤝 Introduce turn-taking games to strengthen joint attention."
        )

    # 🟢 Strong Indicators
    if screening_score >= 75:
        recommendations.append(
            "🌱 Maintain current therapy routines with gradual complexity increase."
        )

    # 💙 Emotional State
    if avg_mood <= 2:
        recommendations.append(
            "💙 Prioritize emotionally safe, child-led activities today."
        )

    # ⚡ Engagement
    if avg_engagement < 5:
        recommendations.append(
            "🎲 Use sensory or movement-based play to boost engagement."
        )

    # 🔁 Consistency
    if streak_days >= 5:
        recommendations.append(
            "🏆 Strong consistency observed — consider introducing one new skill goal."
        )

    if not recommendations:
        recommendations.append(
            "📋 Continue observing and maintaining gentle daily routines."
        )

    return recommendations
