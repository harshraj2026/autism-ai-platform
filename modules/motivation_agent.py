# import streamlit as st
# import random

# def motivation_section():
#     st.header("🌱 Daily Motivation & Encouragement")

#     messages = [
#         "Small steps today build big progress tomorrow 💙",
#         "Consistency matters more than perfection 🌈",
#         "Your effort is shaping your child’s future 🌱",
#         "Every interaction counts — keep going 💪",
#         "You’re doing better than you think ✨"
#     ]

#     if st.button("Get Today’s Motivation"):
#         st.success(random.choice(messages))

#     st.checkbox("I completed today’s therapy tasks")
# modules/motivation_agent.py
# 🔁 UPDATED — Day 6 intelligence-aware agent

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
