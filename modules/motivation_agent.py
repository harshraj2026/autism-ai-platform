import streamlit as st
import random

def motivation_section():
    st.header("🌱 Daily Motivation & Encouragement")

    messages = [
        "Small steps today build big progress tomorrow 💙",
        "Consistency matters more than perfection 🌈",
        "Your effort is shaping your child’s future 🌱",
        "Every interaction counts — keep going 💪",
        "You’re doing better than you think ✨"
    ]

    if st.button("Get Today’s Motivation"):
        st.success(random.choice(messages))

    st.checkbox("I completed today’s therapy tasks")
    
import streamlit as st

def motivation_section():
    st.subheader("Motivation & Daily Adherence")

    checklist_completed = st.checkbox("Therapy completed today")
    mood_score = st.slider("Child mood today", 1, 5, 3)
    streak_days = st.number_input("Current therapy streak (days)", 0, 30, 2)

    if checklist_completed and mood_score >= 4:
        message = f"🌟 Excellent consistency! {streak_days} days in a row."
    elif checklist_completed:
        message = "👍 Therapy completed today. Small routines matter."
    elif mood_score <= 2:
        message = "💙 Tough day. One gentle activity is enough."
    else:
        message = "⏰ A quick check-in today helps track progress."

    st.info(message)

    # modules/motivation_agent.py
# 🔁 UPDATED FILE — refined motivation logic

def daily_motivation_message(
    checklist_completed: bool,
    mood_score: int,
    streak_days: int,
    user_type: str = "parent"
):
    """
    Generates motivation messages for parents or children.
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

