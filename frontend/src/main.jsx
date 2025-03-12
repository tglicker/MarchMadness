import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/index.jsx"; // ✅ Adjusted path
import Matchup from "./pages/matchup.jsx"; // ✅ Ensure this exists

console.log("React app is starting..."); // ✅ Add this for debugging

ReactDOM.createRoot(document.getElementById("app")).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/matchup" element={<Matchup />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
