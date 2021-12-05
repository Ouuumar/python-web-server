import warnings
warnings.filterwarnings("ignore")

import unittest
import requests
import grequests
import logging
import time
import numpy as np

# use log instead of print
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class TestApi(unittest.TestCase):

    URL = "http://host.docker.internal:8080" # const url
    
    def test_website_is_up(self):
        r = requests.get(TestApi.URL)
        self.assertTrue(r.status_code == 200)

    def test_response(self):
        numbers = [0] 
        r = requests.get(f"{TestApi.URL}/average?list={','.join(map(str, numbers))}")
        try:
            mean = np.mean(numbers)
        except:
            mean = 0
        self.assertTrue(float(r.text) == np.mean(numbers))


    def test_mass_request(self):
        n_requests = 10
        max_ms_per_request = 100

        start_time = time.time()

        logging.info(f"Sending {n_requests} requests...") 

        urls = [TestApi.URL]*n_requests
        responses = grequests.map(grequests.head(u) for u in urls)

        end_time = time.time()
        mean_ms_per_request = (end_time-start_time)*1000/n_requests

        logging.info(f"Mean time per request: {mean_ms_per_request}ms")

        self.assertTrue(mean_ms_per_request< max_ms_per_request)
        self.assertTrue(all(r.status_code == 200 for r in responses))


if __name__ == '__main__':
    unittest.main()