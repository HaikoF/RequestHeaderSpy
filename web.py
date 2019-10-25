from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def getHeader():
    headers = dict(request.headers)    
    result = jsonify(headers)
    return result

@app.route("/ip")
def getIp():
    try:
        result = request.headers['Client-Ip']
    except:
        result = request.remote_addr
    return result
