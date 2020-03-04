import unittest
from pprint import pprint
from nose.tools import assert_true
from unittest import TestCase
import requests

import city_event
from city_event import get_events
from unittest.mock import patch, call


# Test event API


class TestEventAPI(TestCase):
    # got this idea from https://realpython.com/testing-third-party-apis-with-mocks/
    def test_request_response(self):
        response = requests.get('http://api.eventful.com/json/events/search?&app_key=bgw8NQ28vRcNxKHB')

        assert_true(response.ok)


if __name__ == '__main__':
    unittest.main()
