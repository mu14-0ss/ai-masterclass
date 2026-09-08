from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

checkins = []

class CheckIn(BaseModel):
    name: str
    sleep: float
    water: int
    steps: int

@app.get("/")
def home():
    return {"message": "AI Fitness Backend running!"}

@app.get("/api/checkins")
def get_checkins():
    return checkins

@app.post("/api/checkins")
def add_checkin(item: CheckIn):
    checkins.append(item)
    # Your AI logic
    if item.sleep >= 7:
        result = f"YES {item.name}, 89% PR chance!"
    else:
        result = f"NO {item.name}, sleep more"
    return {"saved": True, "prediction": result, "total_checkins": len(checkins)}