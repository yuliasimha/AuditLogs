import auditsManager
import json
import time
import requests

auditData = {
  "time": 3,
  "username": "arnold",
  "message": "yulia connection succeeded",
  "action": "connection"
}

auditsMgr = auditsManager.auditsManager()
#auditsMgr.writeAudit(auditData)

#auditsMgr.readAudit("yulia", 6, 123456128)

def send():
  url = "http://127.0.0.1:5000/api/audits/"
  data = {"time": 712, "username": "arnold3", "message": "yulia connection succeeded","action": "connection"}
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  requests.post(url, data=json.dumps(data), headers=headers)
  
send()    