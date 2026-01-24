from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    "codes": [
        "5839201746",
        "7406182953",
        "9265017840",
        "3184769205",
        "8642059317",
        "1590378462",
        "4029581763",
        "7716243908",
        "2957830461",
        "6801942573",
        "9375204681",
        "2148693057",
        "5067381294",
        "8902615743",
        "1639578024",
        "7243059681",
        "4518926703",
        "3086719524",
        "9724601385",
        "8472039516"
    ]
}
@app.get("/get")
def get_codes():
    return "VERSION-NEW\n" + "\n".join(data["codes"])

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
