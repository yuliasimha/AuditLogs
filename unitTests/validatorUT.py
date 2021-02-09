import sys
sys.path.append('../')
import unittest
import json
import jsonschema 
from utils.validator import validator as validator


class TestValidator(unittest.TestCase):

    schema = { 
        "type" : "object",
        "properties" : {   
        "time":  {"type" : "number"},
        "username": {"type" : "string"},
        "message":  {"type" : "string"},
        "action":  {"type" : "string"}
        },
        "required": ["time", "username", "message"]
    }

    def test_valid_json(self):
        json_data = {
                        "time": 32345,
                        "username": "user5",
                        "message": "user5 connection succeeded",
                        "action": "connection"
                    }

        validator.validateInput(json_data, self.schema)

    def test_invalid_json_schema_missing_username(self):
        json_data = {
                        "time": 32345,
                        "message": "user5 connection succeeded",
                        "action": "connection"
                    }
        self.assertRaises(jsonschema.exceptions.ValidationError, validator.validateInput, json.dumps(json_data), self.schema)

    def test_invalid_json_schema_missing_time(self):
        json_data = {
                        "username": "user5",
                        "message": "user5 connection succeeded",
                        "action": "connection"
                    }
        self.assertRaises(jsonschema.exceptions.ValidationError, validator.validateInput, json.dumps(json_data), self.schema)

    def test_invalid_json_schema_missing_message(self):
        json_data = {
                        "time": 32345,
                        "username": "user5",
                        "action": "connection"
                    } 
        self.assertRaises(jsonschema.exceptions.ValidationError, validator.validateInput, json.dumps(json_data), self.schema)
    
    def test_invalid_json_time_string(self):
        json_data = {
                        "time": "32345",
                        "username": "user5",
                        "action": "connection"
                    } 
        self.assertRaises(jsonschema.exceptions.ValidationError, validator.validateInput, json.dumps(json_data), self.schema)

    def test_invalid_json_username_number(self):
        json_data = {
                        "time": "32345",
                        "username": 5,
                        "action": "connection"
                    } 
        self.assertRaises(jsonschema.exceptions.ValidationError, validator.validateInput, json.dumps(json_data), self.schema)

if __name__ == '__main__':
    unittest.main()
