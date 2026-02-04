import streamlit as st
from modules.video_input import video_section
from modules.parent_checklist import checklist_section
from modules.engagement import engagement_section
from modules.motivation_agent import motivation_section
from modules.screening_logic import calculate_screening_score


st.set_page_config(page_title="Autism Care Platform", layout="wide")

st.title("🧠 AI-Enabled Autism Screening & Care Platform")
page = st.sidebar.radio(
    "Navigate",
    [
        "Child Observation",
        "Therapy Tracker",
        "Engagement Feedback",
        "Motivation & Adherence",
        "AI Screening Insight" 
    ]
)
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
    
elif page == "AI Screening Insight":
    st.subheader("AI-Assisted Screening Insight")

    eye_contact = st.slider("Eye Contact", 0.0, 1.0, 0.6)
    joint_attention = st.slider("Joint Attention", 0.0, 1.0, 0.5)
    gesture_use = st.slider("Gesture Use", 0.0, 1.0, 0.4)
    motor_coordination = st.slider("Motor Coordination", 0.0, 1.0, 0.5)
    parent_engagement = st.slider("Parent Engagement", 0.0, 1.0, 0.7)

    score = calculate_screening_score(
        eye_contact,
        joint_attention,
        gesture_use,
        motor_coordination,
        parent_engagement
    )

    st.metric("Screening Confidence Score", f"{score} / 100")
    st.caption("This score supports clinical evaluation. It is not a diagnosis.")

