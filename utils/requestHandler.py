import boto3
import json

class requestHandler:

    def __init__(self, client):
        self.client = client

    def sendSQLRequest(self, bucketName, key, expression):
        responselist = []
        response = self.client.select_object_content(
            Bucket=bucketName,
            Key=key,
            ExpressionType='SQL',
            Expression=expression,
            InputSerialization={'JSON': {"Type": "DOCUMENT"}},
            OutputSerialization={'JSON': {"RecordDelimiter": ","}}
        )
        for event in response['Payload']:
            if 'Records' in event:
                records = event['Records']['Payload'].decode('utf-8')
                records = records.rstrip(',')
                jsonResult = json.loads("[" +records + "]")
                responselist = responselist + jsonResult

        return responselist
