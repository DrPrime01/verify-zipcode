import requests
from flask import jsonify


def call_zipcodes(placename, username, postal_code=None):
    """function to get the zipcodes"""
    if postal_code:
        endpoint_url = f"http://api.geonames.org/postalCodeSearchJSON?placename={placename}&postalcode={postal_code}&username={username}"
    else:
        endpoint_url = f"http://api.geonames.org/postalCodeSearchJSON?placename={placename}&username={username}"
    response = requests.get(endpoint_url)
    return response.json()
