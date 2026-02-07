
import streamlit as st
from utils.logger import save_log

def engagement_section():
    st.header("😊 Engagement & Mood Feedback")

    mood = st.selectbox(
        "Child’s mood today",
        ["Happy", "Neutral", "Frustrated", "Withdrawn"]
    )

    engagement = st.slider(
        "Engagement level",
        0, 10, 5
    )

    notes = st.text_area("Additional observations")

    if st.button("Submit Feedback"):
        save_log(
            "data/logs",
            "engagement.json",
            {
                "agent":"engagement_monitor",
                "mood": mood,
                "engagement_score": engagement,
                "engagement_normalized":engagement/10,
                "notes": notes
            }
        )
        st.success("Engagement data saved")

