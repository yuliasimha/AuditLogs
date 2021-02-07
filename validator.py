import json
import jsonschema 

class validator:

    @staticmethod
    def validateInput(json_data, schema):
        try:
            data = json.loads(json.dumps(json_data))
            jsonschema.validate(data, schema)
        except jsonschema.exceptions.ValidationError as e:
            print("well-formed but invalid JSON:", e)
        except json.decoder.JSONDecodeError as e:
            print("poorly-formed text, not JSON:", e) 