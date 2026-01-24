from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    "codes": [
        "COIN1-AAA",
        "COIN1-BBB",
        "COIN2-CCC",
        "COIN5-DDD",
        "COIN10-EEE",
        "COIN20-FFF"
    ]
}

@app.route("/get", methods=["GET"])
def get_data():
    return jsonify(data)

@app.route("/remove", methods=["POST"])
def remove_item():
    item = request.json.get("item")
    if item in data["codes"]:
        data["codes"].remove(item)
    return jsonify(data)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
