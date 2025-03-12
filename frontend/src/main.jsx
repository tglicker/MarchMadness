import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  const [predictions, setPredictions] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://marchmadness-bxbx.onrender.com/predict')
      .then(response => response.json())
      .then(data => {
        setPredictions(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;
  if (!predictions) return <p>No predictions available.</p>;

  return (
    <div>
      <h1>March Madness Predictions</h1>
      {predictions && Object.entries(predictions).map(([team, data]) => (
        <div key={team}>
          <h2>{team}</h2>
          <p>Spread: {data.spread}</p>
          <p>Over/Under: {data.over_under}</p>
          <p>Win Probability: {data.win_probability}</p>
        </div>
      ))}
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
