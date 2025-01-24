# pylint: skip-file

import pytest
from airports import load_weather_for_location
import requests_mock
import requests

class TestLoadWeather():
    """ Contains tests of the load_weather_for_location function. """

    @staticmethod
    def test_calls_requests_get_method(requests_mock):
        requests_mock.get("http://api.weatherapi.com/v1/forecast.json?key=***REMOVED***&q=1,1&unixdt=1&aqi=yes"
                         , status_code = 200, json={})
        load_weather_for_location("1", "1", 1)

        assert requests_mock.called
        assert requests_mock.call_count == 1
        assert requests_mock.last_request.method == "GET"

    @staticmethod
    def test_http_error_raised(requests_mock):
        with pytest.raises(requests.HTTPError):
            requests_mock.get(
                "http://api.weatherapi.com/v1/forecast.json?key=***REMOVED***&q=1,1&unixdt=1&aqi=yes", status_code=404, json={})
            load_weather_for_location(1, 1, 1)
    
    @staticmethod
    def test_non_number_lat():
        with pytest.raises(TypeError):
            load_weather_for_location("test", 1, 1262304000)

    @staticmethod
    def test_non_number_lng():
        with pytest.raises(TypeError):
            load_weather_for_location(1, "test", 1262304000)

    @staticmethod
    def test_non_number_timestamp():
        with pytest.raises(TypeError):
            load_weather_for_location(1, 1, "test")

    @staticmethod
    def test_timestamp_too_early():
        with pytest.raises(ValueError):
            load_weather_for_location(1, 1, 1262300000)
    
    @staticmethod
    def test_lat_too_high():
        with pytest.raises(ValueError):
            load_weather_for_location(90.5, 1, 1362300000)

    @staticmethod
    def test_lat_too_low():
        with pytest.raises(ValueError):
            load_weather_for_location(-90.5, 1, 1362300000)

    @staticmethod
    def test_lng_too_high():
        with pytest.raises(ValueError):
            load_weather_for_location(1, 180.5, 1362300000)

    @staticmethod
    def test_lng_too_low():
        with pytest.raises(ValueError):
            load_weather_for_location(1, -180.5, 1362300000)
