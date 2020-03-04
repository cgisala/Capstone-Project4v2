from unittest import  TestCase
from unittest.mock import patch
import rest


class TestRestApi(TestCase):
    @patch('rest.get_restaurants')
    def test_get_all(self, mock_cities):
        mock_city = minneapolis
        exaple_api_response = {'city':'minneapolis'{'city':'mock_name'}}
        mock_name.side_effect = [example_api_response]
        # testRestApi = [testCity1, testCity2]
        # testRestApi = weather()
        # testRestApi.get_all(testRestApi)
        self.assertEqual(testRestaurant)