from flask import Flask
import auditsManager
from flask import request
from flask import Response
from flask import jsonify
from flask import abort
import json
import jsonschema
import re
 
app = Flask(__name__)
 
app.debug = True

@app.route("/api/audits/")
def search():
   
    try:
        timeStart =  int(request.args.get('from'))
        timeEnd =  int(request.args.get('to'))
        searchValue = request.args.get('query')
        if timeStart > timeEnd:
            raise Exception("Time start value must be larget than time end")

        if len(searchValue) == 0 or "'" in searchValue or searchValue == "%":
            raise Exception("Search value empty or contains illegal character")

    except Exception as e:
        print("Invalid query string parameter", e)
        return jsonify({'error': 'Bad Request'}), 400 

    auditsMgr = auditsManager.auditsManager()
    response = auditsMgr.readAudit(searchValue, timeStart, timeEnd)
    return json.dumps(response)
    

@app.route('/api/audits/', methods=["POST"])
def addAudit():
    content = request.json
    auditsMgr = auditsManager.auditsManager()

    try:
        auditsMgr.writeAudit(content)
    except jsonschema.exceptions.ValidationError as e:
        print("well-formed but invalid JSON:", e)
        return jsonify({'error': 'Bad Request'}), 400 
    except json.decoder.JSONDecodeError as e:
        print("poorly-formed text, not JSON:", e)
        return jsonify({'error': 'Bad Request'}), 400 
    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server Error'}), 500
    return "", 201
