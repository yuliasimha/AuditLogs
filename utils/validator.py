import json
import jsonschema 

class validator:

    @staticmethod
    def validateInput(json_data, schema):
        data = json.loads(json.dumps(json_data))
        jsonschema.validate(data, schema)