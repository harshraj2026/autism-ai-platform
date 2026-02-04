# modules/screening_logic.py
# 🆕 DAY 6 – Intelligence Layer (Explainable)

def calculate_screening_score(
    eye_contact: float,
    joint_attention: float,
    gesture_use: float,
    motor_coordination: float,
    parent_engagement: float
):
    """
    Returns a screening confidence score (0–100).
    This is NOT a diagnosis.
    """

    score = (
        eye_contact * 0.25 +
        joint_attention * 0.25 +
        gesture_use * 0.20 +
        motor_coordination * 0.15 +
        parent_engagement * 0.15
    )

    return round(score * 100, 2)
