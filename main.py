import auditsManager
import json
import time
import requests

auditData = {
  "time": 32345,
  "username": "user5",
  "message": "user5 connection succeeded",
  "action": "connection"
}

#auditsMgr = auditsManager.auditsManager()
#auditsMgr.writeAudit(auditData)


#auditsMgr.readAudit("yulia", 6, 123456128)

def send():
  url = "https://i5o7w3hula.execute-api.eu-west-3.amazonaws.com/dev/api/audits/"
  data = {"time": 712, "username": "user8", "message": "user8 connection succeeded","action": "connection"}
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  response = requests.post(url, data=json.dumps(data), headers=headers)
  print(response)

send() 

v= 12   