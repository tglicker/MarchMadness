fetch('https://marchmadness-zzm4.onrender.com/predict')
    .then(response => response.json())
    .then(data => {
        const predictionsDiv = document.getElementById('predictions');
        for (const team in data) {
            const teamData = data[team];
            const teamDiv = document.createElement('div');
            teamDiv.classList.add('team-prediction');
            teamDiv.innerHTML = `
                <img src="assets/${team.toLowerCase()}_logo.png" alt="${team} Logo">
                <h2>${team}</h2>
                <p>Spread: ${teamData.spread}</p>
                <p>Over/Under: ${teamData.over_under}</p>
                <p>Win Probability: ${teamData.win_probability}</p>
            `;
            predictionsDiv.appendChild(teamDiv);
        }
    });
