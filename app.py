from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Checkin(BaseModel):
    sleep_hours: float
    stress_level: int
    caffeine_mg: int
    soreness_level: int

checkins = []

@app.post("/api/checkins")
def create_checkin(data: Checkin):
    score = data.sleep_hours*10 - data.stress_level*5 - data.soreness_level*3
    pr = max(10, min(95, int(score+30)))
    return {"predicted_pr_percent": pr, "risk_flag": "LOW" if pr>70 else "HIGH", "message": f"Model says {pr}% chance of PR"}