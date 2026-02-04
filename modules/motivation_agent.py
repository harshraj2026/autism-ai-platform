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
