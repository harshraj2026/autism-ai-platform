import streamlit as st
from utils.logger import save_log

def video_section():
    st.header("🎥 Child Play Observation")

    st.info("Upload short play-session videos (2–5 minutes)")

    video = st.file_uploader(
        "Upload video",
        type=["mp4", "mov", "avi"]
    )

    if video:
        st.video(video)
        save_log(
            "data/logs",
            "vodeo_upload.json",
            {"video_uploaded":True}
        )
        st.success("Video received for behavioral analysis")
       

       