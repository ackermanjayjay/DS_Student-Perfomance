from typing import Union

from fastapi import FastAPI, HTTPException

from load_model import prediction
from pydantic import BaseModel
from model import InputData
import numpy as np

from preprocess import loadInputIterative

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World dunia halo"}


@app.post("/prediction/")

def classification(data: InputData):
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
            "Statuscode": 200,
            "prediction": result[0],
            "Input": loadInputIterative(input_array),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
