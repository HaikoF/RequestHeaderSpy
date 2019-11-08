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
        result = request.headers['Client-Ip'].split(':')[0]
    except:
        result = request.remote_addr
    return result

@app.route("/useragent")
def getUserAgent():
    return request.headers['User-Agent']

@app.route("/get/<name>")
def getAny(name = None):
    try:
        result = {name: request.headers[name]}
    except:
        return "%s not found - may be misspelled?" % name, 404
    return jsonify(result)