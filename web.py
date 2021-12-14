from flask import Flask
from flask import request
from flask import jsonify
from flask import escape


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
    return escape(result)

@app.route("/useragent")
def getUserAgent():
    return escape(request.headers['User-Agent'])

@app.route("/get/<name>")
def getAny(name = None):
    try:
        result = {name: request.headers[name]}
    except:
        return "%s not found - may be misspelled?" % escape(name), 404
    return jsonify(result)