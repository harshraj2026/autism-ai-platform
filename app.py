import streamlit as st
from modules.video_input import video_section
from modules.parent_checklist import checklist_section
from modules.engagement import engagement_section
from modules.motivation_agent import motivation_section

st.set_page_config(page_title="Autism Care Platform", layout="wide")

st.title("🧠 AI-Enabled Autism Screening & Care Platform")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", [
    "Child Observation",
    "Parent Therapy Tracker",
    "Engagement Feedback",
    "Motivation & Adherence"
])

if page == "Child Observation":
    video_section()

elif page == "Therapy Tracker":
    checklist_section()

elif page == "Engagement Feedback":
    engagement_section()

elif page == "Motivation & Adherence":
    motivation_section()
