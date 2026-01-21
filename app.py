from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    "codes": ["A", "B", "C"]
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

if __name__ == "__main__":
    app.run()
