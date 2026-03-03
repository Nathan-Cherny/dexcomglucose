from flask import Flask, jsonify
import os
from pydexcom import Dexcom

app = Flask(__name__)

def get_glucose():
    # try:
    print(os.environ)
    print(os.environ.get("USERNAME"))
    
    dexcom = Dexcom(username=os.environ.get("USERNAME"), password=os.environ.get("PASSWORD"))
    reading = dexcom.get_current_glucose_reading()
    return reading.json
    # except Exception as e:
    #     print(e)
    #     return {"Error": f"Something went wrong: {e}"}

@app.route("/get_glucose")
def glucose():
    return jsonify(get_glucose())

@app.route("/")
def index():
    return "<h1>Dexcom api python call</h1><p>Do not use without permission. xSoTec</p>"
