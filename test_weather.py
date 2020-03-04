import unittest
from unittest import TestCase
from unittest.mock import patch, call
import requests

import weather

class TestWeather(TestCase):

        # @patch('weather.process_current_weather_json')
        # def test_process_current_weather_json(self, mock_temp):
        #         mock_temp = 25.16
        #         # weather_api_response = {'main': {'feels_like': 12.96,
        #         #                 'humidity': 29,
        #         #                 'pressure': 1021,
        #         #                 'temp': mock_temp,
        #         #                 'temp_max': 28,
        #         #                 'temp_min': 21.2},
        #         #         'weather': [{'description': 'clear sky',
        #         #                         'icon': '01d',
        #         #                         'id': 800,
        #         #                         'main': 'Clear'}],
        #         #         'wind': {'deg': 350, 'gust': 17.22, 'speed': 10.29}}
        #         # mock_temp.side_effect = [ weather_api_response ]
        #         result = weather.process_current_weather_json('minneapolis')
        #         temp = result['main']['temp']
        #         self.assertEqual(25.16, temp)
                
        @patch('weather.current_weather_api_call')
        def test_api_call(self, mock_city, mock_country):
                mock_city = 'minneapolis'
                mock_country = 'us'
                example_api_response = {'q': mock_city + ',' + mock_country, 'units': 'imperial', 'appid': weatherkey}

                forecast = data[ example_api_response ]
                weather = forecast[0]

                assert (weather != null)        

if __name__== '__main__':
        unittest.main()
                
