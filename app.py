from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    "codes": ["A", "B", "C"]
}

@app.route("/get", methods=["GET"])
def get_data():
    return ",".join(data["codes"])

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
