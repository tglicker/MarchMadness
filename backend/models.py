import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def create_features(team1_data, team2_data):
    # Your create_features function here
    features = {
        'team1_ppg': float(team1_data['PTS']),
        'team1_oppg': float(team1_data['Opp PTS']),
        'team1_fg_pct': float(team1_data['FG%']),
        'team1_opp_fg_pct': float(team1_data['Opp FG%']),
        'team1_adj_o': float(team1_data['AdjO']),
        'team1_adj_d': float(team1_data['AdjD']),
        'team1_net': int(team1_data['NET']),
        'team2_ppg': float(team2_data['PTS']),
        'team2_oppg': float(team2_data['Opp PTS']),
        'team2_fg_pct': float(team2_data['FG%']),
        'team2_opp_fg_pct': float(team2_data['Opp FG%']),
        'team2_adj_o': float(team2_data['AdjO']),
        'team2_adj_d': float(team2_data['AdjD']),
        'team2_net': int(team2_data['NET']),
        'team1_adj_t': float(team1_data['AdjT']),
        'team2_adj_t': float(team2_data['AdjT']),
    }
    return pd.Series(features)

def create_training_data(bracket_data, team_data):
    # Your create_training_data function here
    game_results = {
        ("Alabama", "Texas A&M-Corpus Christi"): {"margin": 21, "total_score": 143, "first_15": "Alabama"},
        ("Maryland", "West Virginia"): {"margin": 7, "total_score": 134, "first_15": "Maryland"},
        # ... (Add results for all matchups)
    }
    training_data = []
    for team1, team2 in bracket_data:
        if team1 in team_data and team2 in team_data:
            team1_stats = team_data[team1]
            team2_stats = team_data[team2]
            features = create_features(team1_stats, team2_stats)
            results = game_results.get((team1, team2), {})
            if results:
                training_data.append({**features, **results})
    return pd.DataFrame(training_data)

def train_margin_model(data):
    # Train linear regression
    model = make_pipeline(StandardScaler(), LinearRegression())
    model.fit(data[['team1_ppg', 'team1_oppg', 'team1_fg_pct', 'team1_opp_fg_pct', 'team1_adj_o', 'team1_adj_d', 'team1_net', 'team2_ppg', 'team2_oppg', 'team2_fg_pct', 'team2_opp_fg_pct', 'team2_adj_o', 'team2_adj_d', 'team2_net']], data['margin'])
    return model

def predict_margin(model, team1_data, team2_data):
    features = create_features(team1_data, team2_data)
    prediction = model.predict(features.to_frame().T)[0]
    return prediction

# Add similar training and prediction functions for Total Score and First to 15.
