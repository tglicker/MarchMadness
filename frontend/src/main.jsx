import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/index.jsx"; // ✅ Updated path
import Matchup from "./pages/matchup.js"; // ✅ Ensure correct extension

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
