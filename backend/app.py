from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
