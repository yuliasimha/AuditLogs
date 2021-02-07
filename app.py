from flask import Flask
import auditsManager
from flask import request
from flask import Response
from flask import jsonify
import json
 
app = Flask(__name__)
 
app.debug = True

@app.route("/api/audits/")
def search():
    user = request.args.get('query')
    timeStart =  request.args.get('from')
    timeEnd =  request.args.get('to')
    
    auditsMgr = auditsManager.auditsManager()
    response = auditsMgr.readAudit(user, timeStart, timeEnd)
    return json.dumps(response)

@app.route('/api/audits/', methods=["POST"])
def addAudit():
    content = request.json
    auditsMgr = auditsManager.auditsManager()
    auditsMgr.writeAudit(content)
    #statusCode = Response(status = 201)
    return "", 201
