from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, render_template, request
import time
import random
from .scraping import scrape_sports_reference_stats, scrape_kenpom_ratings, scrape_net_rating #Relative Import
from . import models #Relative Import

app = Flask(__name__)
CORS(app)

# ---------------------------------------------------------------------------------------------
# Data Scraping and Processing (Place before your routes)
# ---------------------------------------------------------------------------------------------

team_urls = {
  "Alabama": "https://www.sports-reference.com/cbb/schools/alabama/2024.html",
    "Texas A&M-Corpus Christi": "https://www.sports-reference.com/cbb/schools/texas-am-corpus-christi/2024.html",
    "Maryland": "https://www.sports-reference.com/cbb/schools/maryland/2024.html",
    "West Virginia": "https://www.sports-reference.com/cbb/schools/west-virginia/2024.html",
    "San Diego State": "https://www.sports-reference.com/cbb/schools/san-diego-state/2024.html",
    "Charleston": "https://www.sports-reference.com/cbb/schools/college-of-charleston/2024.html",
    "Virginia": "https://www.sports-reference.com/cbb/schools/virginia/2024.html",
    "Furman": "https://www.sports-reference.com/cbb/schools/furman/2024.html",
    "Creighton": "https://www.sports-reference.com/cbb/schools/creighton/2024.html",
    "NC State": "https://www.sports-reference.com/cbb/schools/north-carolina-state/2024.html",
    "Baylor": "https://www.sports-reference.com/cbb/schools/baylor/2024.html",
    "UC Santa Barbara": "https://www.sports-reference.com/cbb/schools/california-santa-barbara/2024.html",
    "Missouri": "https://www.sports-reference.com/cbb/schools/missouri/2024.html",
    "Utah State": "https://www.sports-reference.com/cbb/schools/utah-state/2024.html",
    "Arizona": "https://www.sports-reference.com/cbb/schools/arizona/2024.html",
    "Princeton": "https://www.sports-reference.com/cbb/schools/princeton/2024.html",
    "Kansas": "https://www.sports-reference.com/cbb/schools/kansas/2024.html",
    "Howard": "https://www.sports-reference.com/cbb/schools/howard/2024.html",
    "Arkansas": "https://www.sports-reference.com/cbb/schools/arkansas/2024.html",
    "Illinois": "https://www.sports-reference.com/cbb/schools/illinois/2024.html",
    "Auburn": "https://www.sports-reference.com/cbb/schools/auburn/2024.html",
    "Iowa": "https://www.sports-reference.com/cbb/schools/iowa/2024.html",
    "Connecticut": "https://www.sports-reference.com/cbb/schools/connecticut/2024.html",
    "Iona": "https://www.sports-reference.com/cbb/schools/iona/2024.html",
    "Saint Mary's": "https://www.sports-reference.com/cbb/schools/saint-marys-ca/2024.html",
    "VCU": "https://www.sports-reference.com/cbb/schools/virginia-commonwealth/2024.html",
    "Michigan State": "https://www.sports-reference.com/cbb/schools/michigan-state/2024.html",
    "USC": "https://www.sports-reference.com/cbb/schools/southern-california/2024.html",
    "TCU": "https://www.sports-reference.com/cbb/schools/tcu/2024.html",
    "Arizona State": "https://www.sports-reference.com/cbb/schools/arizona-state/2024.html",
    "Gonzaga": "https://www.sports-reference.com/cbb/schools/gonzaga/2024.html",
    "Grand Canyon": "https://www.sports-reference.com/cbb/schools/grand-canyon/2024.html",
    "Houston": "https://www.sports-reference.com/cbb/schools/houston/2024.html",
    "Northern Kentucky": "https://www.sports-reference.com/cbb/schools/northern-kentucky/2024.html",
    "Duke": "https://www.sports-reference.com/cbb/schools/duke/2024.html",
    "Oral Roberts": "https://www.sports-reference.com/cbb/schools/oral-roberts/2024.html",
    "Tennessee": "https://www.sports-reference.com/cbb/schools/tennessee/2024.html",
    "Louisiana": "https://www.sports-reference.com/cbb/schools/louisiana-lafayette/2024.html",
    "Kentucky": "https://www.sports-reference.com/cbb/schools/kentucky/2024.html",
    "Providence": "https://www.sports-reference.com/cbb/schools/providence/2024.html",
    "Kansas State": "https://www.sports-reference.com/cbb/schools/kansas-state/2024.html",
    "Montana State": "https://www.sports-reference.com/cbb/schools/montana-state/2024.html",
    "Marquette": "https://www.sports-reference.com/cbb/schools/marquette/2024.html",
    "Vermont": "https://www.sports-reference.com/cbb/schools/vermont/2024.html",
    "Memphis": "https://www.sports-reference.com/cbb/schools/memphis/2024.html",
    "Florida Atlantic": "https://www.sports-reference.com/cbb/schools/florida-atlantic/2024.html",
    "Purdue": "https://www.sports-reference.com/cbb/schools/purdue/2024.html",
    "Texas Southern": "https://www.sports-reference.com/cbb/schools/texas-southern/2024.html",
    "Fairleigh Dickinson": "https://www.sports-reference.com/cbb/schools/fairleigh-dickinson/2024.html",
    "Miami FL": "https://www.sports-reference.com/cbb/schools/miami-fl/2024.html",
    "Drake": "https://www.sports-reference.com/cbb/schools/drake/2024.html",
    "Indiana": "https://www.sports-reference.com/cbb/schools/indiana/2024.html",
    "Kent State": "https://www.sports-reference.com/cbb/schools/kent-state/2024.html",
    "Xavier": "https://www.sports-reference.com/cbb/schools/xavier/2024.html",
    "Kennesaw State": "https://www.sports-reference.com/cbb/schools/kennesaw-state/2024.html",
    "Texas": "https://www.sports-reference.com/cbb/schools/texas/2024.html",
    "Colgate": "https://www.sports-reference.com/cbb/schools/colgate/2024.html",
    "Penn State": "https://www.sports-reference.com/cbb/schools/penn-state/2024.html",
    "Texas A&M": "https://www.sports-reference.com/cbb/schools/texas-am/2024.html",
    "Texas Tech": "https://www.sports-reference.com/cbb/schools/texas-tech/2024.html",
    "Northwestern": "https://www.sports-reference.com/cbb/schools/northwestern/men/2024.html"
}

bracket_2023 = [
    ("Alabama", "Texas A&M-Corpus Christi"),
    ("Maryland", "West Virginia"),
    ("San Diego State", "Charleston"),
    ("Virginia", "Furman"),
    ("Creighton", "NC State"),
    ("Baylor", "UC Santa Barbara"),
    ("Missouri", "Utah State"),
    ("Arizona", "Princeton"),
    ("Kansas", "Howard"),
    ("Arkansas", "Illinois"),
    ("Auburn", "Iowa"),
    ("Connecticut", "Iona"),
    ("Saint Mary's", "VCU"),
    ("Michigan State", "USC"),
    ("TCU", "Arizona State"),
    ("Gonzaga", "Grand Canyon"),
    ("Houston", "Northern Kentucky"),
    ("Duke", "Oral Roberts"),
    ("Tennessee", "Louisiana"),
    ("Kentucky", "Providence"),
    ("Kansas State", "Montana State"),
    ("Marquette", "Vermont"),
    ("Michigan State", "USC"),
    ("Memphis", "Florida Atlantic"),
    ("Purdue", "Texas Southern"),
    ("Fairleigh Dickinson", "Purdue"),
    ("Miami FL", "Drake"),
    ("Indiana", "Kent State"),
    ("Xavier", "Kennesaw State"),
    ("Texas", "Colgate"),
    ("Penn State", "Texas A&M"),
    ("Texas Tech", "NC State"),
    ("Northwestern", "Boise State")
]

all_team_data = {}

for team1, team2 in bracket_2023:
    if team1 not in all_team_data:
        team1_url = team_urls[team1]
        team1_stats = scrape_sports_reference_stats(team1_url)
        team1_kenpom = scrape_kenpom_ratings(team1)
        team1_net = scrape_net_rating(team1)
        if team1_stats and team1_kenpom and team1_net:
            all_team_data[team1] = {**team1_stats, **team1_kenpom, **team1_net}
            print(f"Scraped data for {team1}")
        else:
            print(f"Could not scrape data for {team1}")

    if team2 not in all_team_data:
        team2_url = team_urls[team2]
        team2_stats = scrape_sports_reference_stats(team2_url)
        team2_kenpom = scrape_kenpom_ratings(team2)
        team2_net = scrape_net_rating(team2)
        if team2_stats and team2_kenpom and team2_net:
            all_team_data[team2] = {**team2_stats, **team2_kenpom, **team2_net}
            print(f"Scraped data for {team2}")
        else:
            print(f"Could not scrape data for {team2}")

    time.sleep(random.randint(3, 6))

print("Scraping complete!")

training_df = models.create_training_data(bracket_2023, all_team_data)
print(training_df) #Verify that the dataframe was created.

# ---------------------------------------------------------------------------------------------
# Flask Routes (Your existing routes)
# ---------------------------------------------------------------------------------------------

@app.route('/predict', methods=['GET'])
def get_predictions():
    # Replace with your actual prediction logic
    predictions = {
        "TeamA": {
            "spread": -3.5,
            "over_under": 150.5,
            "win_probability": 0.65,
        },
        "TeamB": {
            "spread": 3.5,
            "over_under": 150.5,
            "win_probability": 0.35,
        },
    }
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
