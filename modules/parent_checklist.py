
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

    completed_count = sum(activities.values())

    if st.button("Save Therapy Progress"):
        save_log(
            "data/logs",
            "therapy_checklist.json",
            {
                "agent": "parent_therapy",
                "completed": completed_count,  
                "total": len(activities),
                "activities": activities
            }
        )
        st.success
        (
             f"Therapy progress logged ({completed_count}/{len(activities)} completed)"
        )

