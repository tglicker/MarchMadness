import { Link } from "react-router-dom";

export default function Home() {
  console.log("Home component is rendering..."); // ✅ Debugging
  return (
    <div>
      <h1>March Madness Predictor</h1>
      <Link to="/matchup">Go to Matchup Predictor</Link>
    </div>
  );
}

