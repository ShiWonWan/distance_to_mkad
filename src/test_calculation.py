import unittest
import requests
from flask.typing import StatusCode

class FlaskTest(unittest.TestCase):

    API_URL = 'http://127.0.0.1:5000/calculation/getdistance'

    # Chech for reponse 200
    def test_getDistance(self):
        body = {
            "address": "Ulitsa Tsentral'naya, 38а, Pirogovo, Moscow Oblast, Rusia, 141033"
        }
        reponse = requests.post(self.API_URL, json=body)
        self.assertEqual(reponse.status_code, 200)
    
    # Check for JSON reponse
    def test_getDistance_content(self):
        body = {
            "address": "Ulitsa Tsentral'naya, 38а, Pirogovo, Moscow Oblast, Rusia, 141033"
        }
        reponse = requests.post(self.API_URL, json=body)
        self.assertEqual(reponse.headers['Content-Type'], 'application/json')
    
    # Check invalid input data
    def test_getDistance_invalid_input(self):
        body = """{"address" : "Ulitsa Tsentral'naya, 38а, Pirogovo, Moscow Oblast, Rusia, 141033"}"""
        reponse = requests.post(self.API_URL, json=body)
        self.assertEqual(reponse.status_code, 200)


if __name__ == '__main__':
    unittest.main()