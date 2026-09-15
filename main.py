from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="NHS Digital Hospital Agent")


class Appointment(BaseModel):
    patient_name: str
    date: str
    time: str
    department: str


appointments: List[Appointment] = []


@app.get("/")
def home():
    return {
        "message": "NHS Digital Hospital Agent is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/appointments")
def book_appointment(appointment: Appointment):
    appointments.append(appointment)

    return {
        "message": "Appointment booked successfully",
        "appointment": appointment
    }


@app.get("/appointments")
def get_appointments():
    return {
        "appointments": appointments
    }
