import unittest
from unittest import TestCase
from unittest.mock import patch, call
import requests

import weather

class TestWeather(TestCase):

        @patch('weather.process_current_weather_json')
        def test_process_current_weather_json(self, mock_temp):
                mock_temp = 25.16
                weather_api_response = {'main': {'feels_like': 12.96,
                                'humidity': 29,
                                'pressure': 1021,
                                'temp': mock_temp,
                                'temp_max': 28,
                                'temp_min': 21.2},
                        'weather': [{'description': 'clear sky',
                                        'icon': '01d',
                                        'id': 800,
                                        'main': 'Clear'}],
                        'wind': {'deg': 350, 'gust': 17.22, 'speed': 10.29}}
                mock_temp.side_effect = [ weather_api_response ]
                result = weather.process_current_weather_json('minneapolis')
                temp = result.temp
                self.assertEqual(25.16, temp)

if __name__== '__main__':
        unittest.main()
                

#     """Mock input() to force it to return 'clear sky' and 25.16"""
#     @patch(weather.current_weather_api_call())

#     data = {'base': 'stations',
#             'clouds': {'all': 1},
#             'cod': 200,
#             'coord': {'lat': 44.98, 'lon': -93.26},
#             'dt': 1582924218,
#             'id': 5037649,
#             'main': {'feels_like': 12.96,
#                     'humidity': 29,
#                     'pressure': 1021,
#                     'temp': 25.16,
#                     'temp_max': 28,
#                     'temp_min': 21.2},
#             'name': 'Minneapolis',
#             'sys': {'country': 'US',
#                     'id': 5829,
#                     'sunrise': 1582894417,
#                     'sunset': 1582934282,
#                     'type': 1},
#             'timezone': -21600,
#             'visibility': 16093,
#             'weather': [{'description': 'clear sky',
#                         'icon': '01d',
#                         'id': 800,
#                         'main': 'Clear'}],
#             'wind': {'deg': 350, 'gust': 17.22, 'speed': 10.29}}