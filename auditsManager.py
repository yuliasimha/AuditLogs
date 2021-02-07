import json
import fileUtils
import boto3
import jsonschema
import requestHandler
from validator import validator 
from decouple import config
 
class auditsManager:

    bucketName = config('BUCKET_NAME')
    key = config('FILE_NAME')

    s3Resorce = boto3.resource('s3')
    s3Client = boto3.client('s3')
    fileHelper = fileUtils.fileUtils(s3Resorce)
    requestHelper = requestHandler.requestHandler(s3Client)
    
    auditSchema = { 
        "type" : "object",
        "properties" : {   
        "time":  {"type" : "number"},
        "username": {"type" : "string"},
        "message":  {"type" : "string"},
        "action":  {"type" : "string"}
        },
        "required": ["time", "username", "message"]
    }

    def writeAudit(self, newAuditLine):
        listObj = []

        validator.validateInput(newAuditLine, self.auditSchema)

        if self.fileHelper.isFileExist(self.bucketName, self.key):
            auditObj = self.s3Resorce.Object(self.bucketName, self.key)
            jsonData = json.load(auditObj.get()['Body'])
            listObj = jsonData

        listObj.append(newAuditLine)
        self.s3Resorce.Bucket(self.bucketName).put_object(Key=self.key, Body=bytes(json.dumps(listObj).encode('UTF-8')))

    def readAudit(self, value, timeStart, timeEnd): 
        expression = self.buildSearchQuery(value, timeStart, timeEnd)
        responseData = self.requestHelper.sendSQLRequest(self.bucketName, self.key, expression)
        return responseData

    def buildSearchQuery(self, value, timeStart, timeEnd):
        query = f"SELECT * FROM S3Object[*][*] s WHERE s.\"username\" = '{value}' OR s.\"action\" = '{value}' OR s.\"message\" LIKE '%{value}%' AND s.\"time\" BETWEEN {timeStart} AND {timeEnd}"
        return query





