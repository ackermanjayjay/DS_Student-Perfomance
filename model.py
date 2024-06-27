from pydantic import BaseModel
from load_model import prediction
import numpy as np
import logging

from preprocess import load_input_iterative


class InputData(BaseModel):
    studyTimeWeekly: float
    absences: int
    tutoring: int
    parentalSupport: int
    sports: int
    music: int
    volunteering: int


def classification_student(data: InputData):
    try:
        input_array = np.array(
            [
                data.studyTimeWeekly,
                data.absences,
                data.tutoring,
                data.parentalSupport,
                data.sports,
                data.music,
                data.volunteering,
            ]
        )
        result = prediction(input_array)
        return {
            "prediction": result[0],
            "input": load_input_iterative(input_array),
        }
    except Exception as e:
        logging.error("error", str(e))
