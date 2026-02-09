import streamlit as st


def motivation_reason(
    checklist_completed: bool,
    mood_score: int,
    streak_days: int
):
    if checklist_completed and mood_score >= 4:
        return "High adherence and positive emotional state detected."

    if checklist_completed:
        return "Routine adherence detected despite emotional variability."

    if mood_score <= 2:
        return "Emotional fatigue detected. Supportive messaging applied."

    if streak_days >= 3:
        return "Consistency pattern identified."

    return "Low engagement data — neutral encouragement applied."

#------LOGIC SECTION-------

def daily_motivation_message(
    checklist_completed: bool,
    mood_score: int,
    streak_days: int,
    user_type: str = "parent"
):
    """
    Generates adaptive motivation messages.
    This supports long-term adherence and emotional well-being.
    """

    # 🌱 CHILD-FACING MESSAGES
    if user_type == "child":
        if checklist_completed:
            return "🎉 Awesome job today! Want to play again tomorrow?"
        return "🧸 Let’s try one fun activity today!"

    # 🧠 PARENT-FACING MESSAGES
    if checklist_completed and mood_score >= 4:
        return f"🌟 Great consistency! {streak_days} days in a row — this matters."

    if checklist_completed:
        return "👍 Therapy completed today. Even small routines create change."

    if mood_score <= 2:
        return "💙 Tough days happen. One small step today is enough."

    if streak_days >= 3:
        return f"⏰ You’re on a {streak_days}-day streak. Let’s keep it going!"

    return "📋 A quick check-in today helps us track meaningful progress."

#-------UI SECTION---------
def motivation_section():
    st.header("🌱 Daily Motivation & Encouragement")
    

checklist_completed = st.checkbox("Therapy completed today")
mood_score = st.slider("Child mood today", 1, 5, 3)
streak_days = st.number_input("Current therapy streak (days)", 0, 30, 2)

user_type = st.selectbox(
        "Message audience",
        ["parent", "child"]
    )

message = daily_motivation_message(
        checklist_completed=checklist_completed,
        mood_score=mood_score,
        streak_days=streak_days,
        user_type=user_type
    )

st.info(message)

 
