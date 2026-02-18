import streamlit as st
from modules.video_input import video_section
from modules.parent_checklist import checklist_section
from modules.engagement import engagement_section
from modules.motivation_agent import motivation_section, daily_motivation_message
from modules.screening_logic import calculate_screening_score
from modules.progress_analytics import analyze_progress

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus import ListFlowable
from reportlab.platypus import ListItem
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

def generate_pdf(screening_score, risk_level, therapy_days, mood_score, recommendations):

    file_name = "Autism_Risk_Report.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    
    elements.append(Paragraph("<b>Autism AI Risk Assessment Report</b>", styles["Title"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"Screening Score: {screening_score}", styles["Normal"]))
    elements.append(Paragraph(f"Risk Level: {risk_level}", styles["Normal"]))
    elements.append(Paragraph(f"Therapy Days This Week: {therapy_days}", styles["Normal"]))
    elements.append(Paragraph(f"Mood Score: {mood_score}", styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("<b>AI Recommendations:</b>", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    rec_list = [ListItem(Paragraph(rec, styles["Normal"])) for rec in recommendations]
    elements.append(ListFlowable(rec_list, bulletType='bullet'))

    doc.build(elements)

    return file_name



st.set_page_config(page_title="Autism Care Platform", layout="wide")

st.title("🧠 AI-Enabled Autism Screening & Care Platform")
#  ---- Recommendation Function ------
def generate_recommendations(risk_score, mood_score, therapy_days):

    recommendations = []

    if risk_score >= 6:
        recommendations.append("Increase therapy sessions frequency.")
        recommendations.append("Consult developmental pediatrician.")
        recommendations.append("Initiate structured behavioral intervention.")

    elif risk_score >= 4:
        recommendations.append("Maintain consistent therapy routine.")
        recommendations.append("Monitor behavioral changes weekly.")
    
    else:
        recommendations.append("Continue current therapy plan.")
        recommendations.append("Encourage social interaction activities.")

    if mood_score <= 2:
        recommendations.append("Introduce emotional regulation exercises.")

    if therapy_days < 3:
        recommendations.append("Improve therapy adherence this week.")

    return recommendations


# Risk Calculation Functions
def calculate_risk(score, therapy_days, mood_score):
    risk = 0
    
    # Screening score weight
    if score > 15:
        risk += 3
    elif score > 8:
        risk += 2
    else:
        risk += 1

    # Therapy consistency
    if therapy_days < 3:
        risk += 2
    elif therapy_days < 7:
        risk += 1

    # Mood impact
    if mood_score <= 2:
        risk += 2
    elif mood_score == 3:
        risk += 1

    return risk


def classify_risk(risk_score):
    if risk_score >= 6:
        return "🔴 High Risk"
    elif risk_score >= 4:
        return "🟡 Moderate Risk"
    else:
        return "🟢 Low Risk"


# -------------------------
# Streamlit UI Starts Here
# -------------------------

# ---OLD SIDEBAR-----
# page = st.sidebar.radio("Navigate", [
#     "Child Observation",
#     "Parent Therapy Tracker",
#     "Engagement Feedback",
#     "Motivation & Adherence",
#     "Ai Screening Insight",
#     "Progress Insights"
# ])
# ----NEW SIDEBAR-----
page = st.sidebar.selectbox(
    "Navigate",
    ["Home", "AI Screening Insight", "Therapy Tracker", "Predictive Risk Layer"]
)
if "risk_history" not in st.session_state:
 st.session_state.risk_history = []
history = st.session_state.risk_history
if page == "Predictive Risk Layer":

    st.header("📊 Predictive Autism Risk Assessment")

    screening_score = st.slider("Screening Score", 0, 20, 10)
    therapy_days = st.number_input("Therapy Days This Week", 0, 7, 3)
    mood_score = st.slider("Child Mood Score", 1, 5, 3)

    risk_score = calculate_risk(screening_score, therapy_days, mood_score)
    if st.button("Save Risk Snapshot",key="risk_snapshot"):
     st.session_state.risk_history.append(risk_score)
     st.success("Risk data saved!")

       #------Show Risk Trend Graph----
 
    # if len(st.session_state.risk_history) > 0:
    #  st.subheader("📈 Risk Trend Over Time")
    #  st.line_chart(st.session_state.risk_history)
    if len(history) > 0:
     st.subheader("📈 Risk Trend Over Time")
     st.line_chart(history)


     # ----Add Smart Trend Alert-----

    # if len(st.session_state.risk_history) >= 2:
    #  if st.session_state.risk_history[-1] > st.session_state.risk_history[-2]:
    #     st.warning("⚠️ Risk is increasing. Early intervention recommended.")
    # elif st.session_state.risk_history[-1] < st.session_state.risk_history[-2]:
    #     st.success("✅ Risk is decreasing. Good progress!")
    # elif st.session_state.risk_history[-1] == st.session_state.risk_history[-2]:
    #     st.info("ℹ️ Risk level unchanged.")
    if len(history) >= 2:
      last = history[-1]
      previous = history[-2]
    
      if last > previous:
        st.warning("⚠️ Risk is increasing. Early intervention recommended.")

      elif last < previous:
        st.success("✅ Risk is decreasing. Good progress!")

      else:
        st.info("ℹ️ Risk level unchanged.")


    # ------Add a reset button----
    if st.button("Reset Risk History",key="reset_history"):
       st.session_state.risk_history = []
       st.success("History cleared.")

    risk_level = classify_risk(risk_score)

    st.subheader("Predicted Risk Level:")
    st.markdown(f"## {risk_level}")
    st.progress(risk_score / 8)
    
    # ------Display Recommendations in UI------
    
    st.subheader("🧠 AI-Generated Recommendations")

    recommendations = generate_recommendations(
    risk_score,
    mood_score,
    therapy_days
    )

    for rec in recommendations:
       st.write("•", rec)
    #  -----Make It Look Professional----
    st.info("Recommendations are generated using AI-based risk logic.")

    if st.button("Generate Clinical Report (PDF)",key="pdf_button"):

       file = generate_pdf(
        screening_score,
        risk_level,
        therapy_days,
        mood_score,
        recommendations
       )

       with open(file, "rb") as f:
        st.download_button(
            "Download Report",
             f,
             file_name="Autism_Risk_Report.pdf",
             key="download_pdf_risk"
            )




#-------CHILD OBSERVATION-------
elif page == "Child Observation":
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

    from modules.data_engine import (
        calculate_therapy_streak,
        calculate_avg_mood,
        calculate_avg_engagement
    )

    streak_days = calculate_therapy_streak()
    avg_mood = calculate_avg_mood()
    avg_engagement = calculate_avg_engagement()

    st.metric("Therapy Sessions Logged", streak_days)
    st.metric("Average Mood", avg_mood)
    st.metric("Average Engagement", avg_engagement)

    insight = analyze_progress(
        streak_days=streak_days,
        avg_mood=avg_mood,
        avg_engagement=avg_engagement
    )

    st.success(insight)
    st.caption("Insight is generated from real stored behavioral data.")

 
#-----------AI SCREENING---------
elif page == "AI Screening Insight":
 
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

