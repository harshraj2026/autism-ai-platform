# modules/data_engine.py
# 🔁 NEW FILE — Day 11 Data Intelligence Engine

import os
import json
from statistics import mean


LOG_FOLDER = "data/logs"


def load_logs(filename):
    """
    Loads all JSON logs of a specific type.
    """
    logs = []

    if not os.path.exists(LOG_FOLDER):
        return logs

    for file in os.listdir(LOG_FOLDER):
        if filename in file:
            filepath = os.path.join(LOG_FOLDER, file)
            with open(filepath, "r") as f:
                logs.append(json.load(f))

    return logs


def calculate_therapy_streak():
    """
    Calculates number of therapy sessions logged.
    (Simple version: total logs count)
    """
    therapy_logs = load_logs("therapy_checklist")
    return len(therapy_logs)


def calculate_avg_mood():
    """
    Calculates average mood from engagement logs.
    """
    engagement_logs = load_logs("engagement")

    mood_mapping = {
        "Happy": 5,
        "Neutral": 3,
        "Frustrated": 2,
        "Withdrawn": 1
    }

    mood_scores = [
        mood_mapping.get(log.get("mood"), 3)
        for log in engagement_logs
    ]

    return round(mean(mood_scores), 2) if mood_scores else 0


def calculate_avg_engagement():
    """
    Calculates average engagement score.
    """
    engagement_logs = load_logs("engagement")

    scores = [
        log.get("engagement_score", 0)
        for log in engagement_logs
    ]

    return round(mean(scores), 2) if scores else 0
