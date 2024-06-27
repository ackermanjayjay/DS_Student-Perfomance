from typing import Union

from fastapi import FastAPI, HTTPException, status

from load_model import prediction
from pydantic import BaseModel
from model import InputData, classification_student
import numpy as np


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World dunia halo"}


@app.post("/prediction/", status_code=status.HTTP_200_OK)
def classification(data: InputData):
    try:
        result = classification_student(data)
        return {
            "data": result,
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
