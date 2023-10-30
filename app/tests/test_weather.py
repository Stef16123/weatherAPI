import asyncio
import sys
sys.path.append('/app')

import unittest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


class WeatherTest(unittest.TestCase):
    

    def test_current(self):
        response = client.get("/weather/current")
        assert response.status_code == 200 or response.status_code == 404
    
    def test_last_hour(self):
        response = client.get("/weather/last-hour")
        assert response.status_code == 200 or response.status_code == 404
    
    def test_historical(self):
        response = client.get("/weather/historical")
        assert response.status_code == 200 or response.status_code == 404

    def test_historical_max(self):
        response = client.get("/weather/historical/max")
        assert response.status_code == 200 or response.status_code == 404

    def test_historical_min(self):
        response = client.get("/weather/historical/max")
        assert response.status_code == 200 or response.status_code == 404


if __name__ == '__main__':
    unittest.main()
