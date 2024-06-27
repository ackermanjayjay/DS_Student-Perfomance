from pydantic import BaseModel
import logging


def preprocess_feature_data(data):
    tutoring = {"Yes": 1.0, "No": 0.0}
    ParentalSupport = {}


def loadInputIterative(data):
    simpan = []
    result = {}
    for value in data:
        simpan.append(value)
    result = {
        "StudyTimeWeekly": simpan[0],
        "Absences": simpan[1],
        "ParentalSupport": simpan[2],
        "Tutoring": simpan[3],
        "Sports": simpan[4],
        "Music": simpan[5],
        "Volunteering": simpan[6],
    }
    return result
