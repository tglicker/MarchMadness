from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import random

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with specific frontend URLs for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load team stats from a JSON file
try:
    with open("data/team_stats.json", "r") as file:
        team_stats = json.load(file)
except Exception as e:
    team_stats = []
    print(f"Error loading team stats: {e}")

# Request model
class MatchupRequest(BaseModel):
    team1: str
    team2: str

@app.get("/")
def home():
    return {"message": "March Madness Predictor API"}

@app.get("/teams")
def get_teams():
    return {"teams": sorted([team["team"] for team in team_stats])}

@app.post("/predict")
def predict_outcome(matchup: MatchupRequest):
    team1_stats = next((t for t in team_stats if t["team"] == matchup.team1), None)
    team2_stats = next((t for t in team_stats if t["team"] == matchup.team2), None)

    if not team1_stats or not team2_stats:
        return {"error": "Team not found"}

    # Calculate point differential
    team1_advantage = (team1_stats["offensive_efficiency"] - team2_stats["defensive_efficiency"]) + team1_stats["point_differential"]
    team2_advantage = (team2_stats["offensive_efficiency"] - team1_stats["defensive_efficiency"]) + team2_stats["point_differential"]

    winner = matchup.team1 if team1_advantage > team2_advantage else matchup.team2
    confidence = round(abs(team1_advantage - team2_advantage) * 2, 2)  # Scale confidence based on difference

    return {"winner": winner, "confidence": min(confidence, 90)}  # Cap confidence at 90%
