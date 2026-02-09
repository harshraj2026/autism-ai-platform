def explain_screening_score(score: int):
    """
    Converts screening score into clinician-friendly explanation.
    """

    if score >= 75:
        return (
            "🟢 Strong developmental indicators observed. "
            "Child shows consistent social engagement and coordination. "
            "Routine monitoring is recommended."
        )

    if score >= 50:
        return (
            "🟡 Moderate developmental variance detected. "
            "Some social-communication markers may need structured observation. "
            "Early intervention guidance could be beneficial."
        )

    return (
        "🔴 Developmental risk indicators detected. "
        "Multiple behavioral markers suggest further clinical evaluation. "
        "This is NOT a diagnosis."
    )
