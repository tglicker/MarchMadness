import { useState, useEffect } from "react";

export default function Matchup() {
  const [teams, setTeams] = useState([]);
  const [team1, setTeam1] = useState("");
  const [team2, setTeam2] = useState("");
  const [prediction, setPrediction] = useState(null);

  // Fetch teams from the backend
  useEffect(() => {
    fetch("https://your-render-backend-url/teams")
      .then((res) => res.json())
      .then((data) => setTeams(data.teams))
      .catch((err) => console.error("Error fetching teams:", err));
  }, []);

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
      <select onChange={(e) => setTeam1(e.target.value)}>
        <option value="">Select Team 1</option>
        {teams.map((team) => (
          <option key={team} value={team}>{team}</option>
        ))}
      </select>
      <select onChange={(e) => setTeam2(e.target.value)}>
        <option value="">Select Team 2</option>
        {teams.map((team) => (
          <option key={team} value={team}>{team}</option>
        ))}
      </select>
      <button onClick={handlePredict} disabled={!team1 || !team2}>Predict</button>

      {prediction && (
        <div>
          <h3>Winner: {prediction.winner}</h3>
          <p>Confidence: {prediction.confidence}%</p>
        </div>
      )}
    </div>
  );
}


