import sys
sys.path.append('../')
import unittest
import auditsManager
from unittest.mock import patch
import requests
import json


class TestUtils(unittest.TestCase):

    auditsManager = auditsManager.auditsManager()  

    def test_valid_build_query(self):
        self.assertEqual(self.auditsManager.buildSearchQuery("value", "timeStart", "timeEnd"),"SELECT * FROM S3Object[*][*] s WHERE s.\"username\" = 'value' OR s.\"action\" = 'value' OR s.\"message\" LIKE '%value%' AND s.\"time\" BETWEEN timeStart AND timeEnd")

if __name__ == '__main__':
    unittest.main()