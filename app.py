import streamlit as st
from modules.video_input import video_section
from modules.parent_checklist import checklist_section
from modules.engagement import engagement_section
from modules.motivation_agent import motivation_section, daily_motivation_message
from modules.screening_logic import calculate_screening_score
from modules.progress_analytics import analyze_progress

st.set_page_config(page_title="Autism Care Platform", layout="wide")

st.title("🧠 AI-Enabled Autism Screening & Care Platform")

page = st.sidebar.radio("Navigate", [
    "Child Observation",
    "Parent Therapy Tracker",
    "Engagement Feedback",
    "Motivation & Adherence",
    "Ai Screening Insight",
    "Progress Insights"
])
#-------CHILD OBSERVATION-------
if page == "Child Observation":
    video_section()
#-------THERAPY TRACKER---------
elif page == "Parent Therapy Tracker":
    checklist_section()
#--------ENGAGEMENT-------------
elif page == "Engagement Feedback":
    engagement_section()
#---------MOTIVATION-------------
elif page == "Motivation & Adherence":
    motivation_section()
    #-----PROGRESS INSIGHTS--------
elif page == "Progress Insights":
 st.subheader("📊 Behavioral Progress Insights")

streak_days = st.number_input("Therapy streak (days)", 0, 30, 5)
avg_mood = st.slider("Average mood (last few days)", 1, 5, 3)
avg_engagement = st.slider("Average engagement", 0, 10, 6)

insight = analyze_progress(
        streak_days=streak_days,
        avg_mood=avg_mood,
        avg_engagement=avg_engagement
    )

st.success(insight)
from modules.therapy_recommendation import recommend_therapy

st.divider()
st.subheader("🧩 Personalized Therapy Guidance")

therapy_plan = recommend_therapy(
    screening_score=70,  # placeholder until automated link
    avg_mood=avg_mood,
    avg_engagement=avg_engagement,
    streak_days=streak_days
    )

for item in therapy_plan:
     st.write("•", item)

st.caption("Insight is generated from observed behavioral trends, not diagnosis.")
from modules.longitudinal_analysis import analyze_longitudinal_trends

st.divider()
st.subheader("📈 Longitudinal Progress Trends")

 # 🔽 Mock historical data (Day 10 placeholder)
past_streaks = [1, 2, 3, 5, streak_days]
past_moods = [2, 3, 3, 4, avg_mood]
past_engagements = [4, 5, 6, 7, avg_engagement]

trend_insights = analyze_longitudinal_trends(
    past_streaks=past_streaks,
    past_moods=past_moods,
    past_engagements=past_engagements
    )

for insight in trend_insights:
     st.write("•", insight)

st.caption(
    "Trend analysis is observational and supports long-term care planning."
)

 
#-----------AI SCREENING---------
if page == "AI Screening Insight":
 st.subheader("🧠 AI-Assisted Screening Insight")
 st.caption("This score assists clinicians. It is NOT a diagnosis.")
    
    #---BEHAVIOURAL MARKERS------
eye_contact = st.slider("Eye Contact", 0.0, 1.0, 0.6)
joint_attention = st.slider("Joint Attention", 0.0, 1.0, 0.5)
gesture_use = st.slider("Gesture Use", 0.0, 1.0, 0.4)
motor_coordination = st.slider("Motor Coordination", 0.0, 1.0, 0.5)
parent_engagement = st.slider("Parent Engagement", 0.0, 1.0, 0.7)

score,explanation = calculate_screening_score(
        eye_contact,
        joint_attention,
        gesture_use,
        motor_coordination,
        parent_engagement
    )

st.metric("Screening Confidence Score", f"{score} / 100")
st.info(explanation)
    #----CONTEXT AWARE MOTIVATION---
st.divider()
st.subheader("Daily Motivation Insight")

streak_days = st.number_input("Therapy streak (days)", 0, 30, 3)
user_type = st.selectbox("Message audience", ["parent", "child"], key="screening_user_type")
    
message = daily_motivation_message(
    checklist_completed=True,
    mood_score=4,
    streak_days=streak_days,
    user_type=user_type
    
    )

st.info(message)
