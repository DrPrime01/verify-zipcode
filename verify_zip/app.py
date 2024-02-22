import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from helpers import call_zipcodes

load_dotenv()

app = Flask(__name__)
username = os.getenv('PASSKEY')


@app.route("/")
def main():
    """Hello"""
    return "Hello from Flask!"


@app.route("/postcodes", methods=["POST"])
def get_zipcodes():
    """Route to get zipcodes based on placename"""
    if request.is_json:
        payload = request.json
        if "placename" not in payload:
            return jsonify({'error': 'placename is required'}), 400
        placename = payload["placename"]
    else:
        placename = request.form.get("placename")
        if placename is None:
            return jsonify({'error': 'placename is required'}), 400

    data = call_zipcodes(placename, username)
    return jsonify(data), 200


@app.route("/verify_zipcode", methods=["POST"])
def verify_zipcode():
    """Route to verify zipcode based on placename and zipcode"""
    if request.is_json:
        payload = request.json
        placename = payload.get("placename")
        postal_code = payload.get("postal_code")
        if not placename or not postal_code:
            return jsonify({'error': 'placename/postal code is required'}), 400
    else:
        placename = request.form.get("placename")
        postal_code = request.form.get("postal_code")
        if not placename or not postal_code:
            return jsonify({'error': 'placename/postal code is required'}), 400

    data = call_zipcodes(placename, username, postal_code)
    postal_codes = data.get("postalCodes", [])
    if postal_codes:
        return jsonify({"message": True, "data": postal_codes[0]}), 200

    return jsonify({"message": False}), 200


if __name__ == "__main__":
    app.run(debug=True)
