import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/index.jsx"; // ✅ Adjusted path
import Matchup from "./pages/matchup.jsx"; // ✅ Make sure this file exists

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
