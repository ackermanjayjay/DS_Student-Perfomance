from pydantic import BaseModel
from load_model import prediction
import numpy as np
import logging

from preprocess import loadInputIterative


class InputData(BaseModel):
    StudyTimeWeekly: float
    Absences: int
    Tutoring: int
    ParentalSupport: int
    Sports: int
    Music: int
    Volunteering: int


def classification_student(data: InputData):
    try:
        input_array = np.array(
            [
                data.StudyTimeWeekly,
                data.Absences,
                data.Tutoring,
                data.ParentalSupport,
                data.Sports,
                data.Music,
                data.Volunteering,
            ]
        )
        result = prediction(input_array)
        return {
            "prediction": result[0],
            "Input": loadInputIterative(input_array),
        }
    except Exception as e:
        logging.error("status_code = ", 500, str(e))
