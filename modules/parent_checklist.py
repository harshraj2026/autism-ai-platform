
import streamlit as st
from utils.logger import save_log

def checklist_section():
    st.header("📋 Daily Therapy Checklist")

    activities = {
        "Eye contact exercise": False,
        "Name response practice": False,
        "Imitation activity": False,
        "Gesture prompting": False,
        "Social play": False
    }

    for activity in activities:
        activities[activity] = st.checkbox(activity)

    if st.button("Save Therapy Progress"):
        save_log(
            "data/logs",
            "therapy_checklist.json",
            activities
        )
        st.success("Therapy progress logged successfully")

