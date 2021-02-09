import json
import botocore
from botocore.exceptions import ClientError

class fileUtils:

    def __init__(self, resource):
        self.resource = resource

    def isFileExist(self, bucketName, key):
        isExists = True
        try:
            self.resource.Object(bucketName, key).load()
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
               isExists = False
        return isExists 
