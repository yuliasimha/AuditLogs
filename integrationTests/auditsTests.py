import os
import sys
sys.path.append('../')
import unittest
from app import app
import json
from flask import request
from flask import Response
import jsonschema

class auditsTests(unittest.TestCase):
   
  def setUp(self):
      app.testing = True
      self.test = app.test_client()     

  def test_valid_read_audits(self):
      params = "query=user8&from=1&to=12345678900000000"
      response = self.test.get('/api/audits/', query_string=params, content_type='application/json')
      self.assertEqual(response.status_code, 200)

  def test_valid_write_audit(self):
      params = {
                 "time": 123456,
                 "username": "test4",
                 "message": "test4 connection succeeded",
                 "action": "connection"
               }

      response = self.test.post('/api/audits/', data=json.dumps(params), content_type='application/json') 
      self.assertEqual(response.status_code, 201)

  def test_invalid_write_audit_bad_request(self):
      params = {
                 "time": "123456",
                 "username": "test4",
                 "message": "test4 connection succeeded",
               }

      response = self.test.post('/api/audits/', data=json.dumps(params), content_type='application/json') 
      self.assertEqual(response.status_code, 400)    

if __name__ == '__main__':
    unittest.main()
