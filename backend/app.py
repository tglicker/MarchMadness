from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['GET'])
def get_predictions():
    # Sample prediction data (replace with your model's output)
    predictions = {
        "team1": {
            "spread": -5.5,
            "over_under": 145.5,
            "win_probability": 0.6
        },
        "team2": {
            "spread": 5.5,
            "over_under": 145.5,
            "win_probability": 0.4
        }
    }
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
