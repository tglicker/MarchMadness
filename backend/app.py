from fastapi import FastAPI
from pydantic import BaseModel
import json
import random

app = FastAPI()

# Load team stats from a JSON file
with open("data/team_stats.json", "r") as file:
    team_stats = json.load(file)

# Request model
class MatchupRequest(BaseModel):
    team1: str
    team2: str

@app.get("/")
def home():
    return {"message": "March Madness Predictor API"}

@app.post("/predict")
def predict_outcome(matchup: MatchupRequest):
    team1_stats = next((t for t in team_stats if t["team"] == matchup.team1), None)
    team2_stats = next((t for t in team_stats if t["team"] == matchup.team2), None)

    if not team1_stats or not team2_stats:
        return {"error": "Team not found"}

    team1_advantage = team1_stats["offensive_efficiency"] - team2_stats["defensive_efficiency"]
    team2_advantage = team2_stats["offensive_efficiency"] - team1_stats["defensive_efficiency"]

    winner = matchup.team1 if team1_advantage > team2_advantage else matchup.team2
    return {"winner": winner, "confidence": round(random.uniform(50, 90), 2)}

