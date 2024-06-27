from pydantic import BaseModel
import logging


def preprocess_feature_data(data):
    tutoring = {"Yes": 1.0, "No": 0.0}
    ParentalSupport = {}


def load_input_iterative(data):
    simpan = []
    result = {}
    for value in data:
        simpan.append(value)
    result = {
        "studyTimeWeekly": simpan[0],
        "absences": simpan[1],
        "parentalSupport": simpan[2],
        "tutoring": simpan[3],
        "sports": simpan[4],
        "music": simpan[5],
        "volunteering": simpan[6],
    }
    return result
