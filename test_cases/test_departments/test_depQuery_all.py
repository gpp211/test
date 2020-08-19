import requests
from unittest import TestCase


class TestDepQueryAll(TestCase):
    def test_query_all(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        res = requests.get(url)
        self.assertEqual(200, res.status_code)

    def test_query_byWrongMethod(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        res = requests.post(url)
        self.assertEqual(200, res.status_code)

