
from modules.explainability import explain_screening_score

def calculate_screening_score(
    eye_contact,
    joint_attention,
    gesture_use,
    motor_coordination,
    parent_engagement
):
    """
    Returns a screening confidence score (0–100).
    This is NOT a diagnosis.
    """
    weights = [0.25, 0.25, 0.2, 0.15, 0.15]
    features = [
        eye_contact,
        joint_attention,
        gesture_use,
        motor_coordination,
        parent_engagement,
    ]
    score = int(sum(f * w for f, w in zip(features, weights)) * 100)

    explanation = explain_screening_score(score)

    return score, explanation
