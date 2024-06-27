from pydantic import BaseModel


class InputData(BaseModel):
    StudyTimeWeekly: float
    Absences: float
    Tutoring: float
    ParentalSupport: float
    Sports: float
    Music: float
    Volunteering: float
