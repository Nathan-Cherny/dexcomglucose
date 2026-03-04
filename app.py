from flask import Flask, jsonify, request
import os
from pydexcom import Dexcom

app = Flask(__name__)
API_KEY = os.environ.get("API_KEY")

def get_glucose():
    try:
        dexcom = Dexcom(username=os.environ.get("USERNAME"), password=os.environ.get("PASSWORD"))
        reading = dexcom.get_current_glucose_reading()
        return reading.json
    except Exception as e:
        print(e)
        return {"Error": f"Something went wrong: {e}"}

@app.route("/get_glucose")
def glucose():
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != f"Bearer {API_KEY}":
        print(f"auth_header = {auth_header}")
        return jsonify({
            "status": 401,
            "Error": "Unauthorized. Authorization Token is invalid."
        })
        
    return jsonify(get_glucose())

@app.route("/")
def index():
    return "<h1>Dexcom api python call</h1><p>Do not use without permission. xSoTec</p>"
