from typing import Union

from fastapi import FastAPI, HTTPException

from load_model import prediction
from pydantic import BaseModel
from model import InputData
import numpy as np

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World dunia halo"}


@app.post("/prediction/")
def classification(data: InputData):
    try:
        input_array = np.array(
            [
                data.feature1,
                data.feature2,
                data.feature3,
                data.feature4,
                data.feature5,
                data.feature6,
                data.feature7,
            ]
        )
        result = prediction(input_array)
        return {"Statuscode": 200, "prediction": result[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
