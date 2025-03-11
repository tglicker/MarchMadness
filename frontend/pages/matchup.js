import { useState } from "react";

export default function Matchup() {
  const [team1, setTeam1] = useState("");
  const [team2, setTeam2] = useState("");
  const [prediction, setPrediction] = useState(null);

  const handlePredict = async () => {
    try {
      const response = await fetch("https://your-render-backend-url/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ team1, team2 })
      });
      const data = await response.json();
      setPrediction(data);
    } catch (error) {
      console.error("Error making prediction:", error);
    }
  };

  return (
    <div>
      <h1>Predict Matchup</h1>
      <input type="text" placeholder="Team 1" value={team1} onChange={(e) => setTeam1(e.target.value)} />
      <input type="text" placeholder="Team 2" value={team2} onChange={(e) => setTeam2(e.target.value)} />
      <button onClick={handlePredict}>Predict</button>
      {prediction && (
        <div>
          <h3>Winner: {prediction.winner}</h3>
          <p>Confidence: {prediction.confidence}%</p>
        </div>
      )}
    </div>
  );
}

