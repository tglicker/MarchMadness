import { useState, useEffect } from "react";

export default function Matchup() {
  const [teams, setTeams] = useState([]);
  const [team1, setTeam1] = useState("");
  const [team2, setTeam2] = useState("");
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    fetch("https://marchmadness-bxbx.onrender.com/teams")
      .then((res) => res.json())
      .then((data) => setTeams(data.teams))
      .catch((err) => console.error("Error fetching teams:", err));
  }, []);

  const handlePredict = async () => {
    try {
      const response = await fetch("https://marchmadness-bxbx.onrender.com/predict", {
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
      <h1>MARCH MADNESS JAM</h1>

      <div className="select-container">
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
      </div>

      <button onClick={handlePredict} disabled={!team1 || !team2}>
        Predict!
      </button>

      {prediction && (
        <div className="scoreboard">
          <h3 className="winner">Winner: {prediction.winner}</h3>
          <p className="confidence">
            Confidence: {prediction.confidence}%
          </p>
          {prediction.confidence > 80 && <p className="flames">🔥 HE’S ON FIRE! 🔥</p>}
        </div>
      )}
    </div>
  );
}



