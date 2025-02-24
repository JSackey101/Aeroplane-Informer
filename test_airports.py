
from os import environ
from datetime import datetime
import pytest
import requests_mock
from airports import (load_weather_for_location, flight_data_cleaner, add_weather_to_flights,
                      round_to_nearest_hour, get_flights_from_iata,
                      find_airport_from_iata, choose_desired_airport, remove_minutes)
import requests
from dotenv import load_dotenv

load_dotenv(".env")

UNCLEAN_FLIGHT_DATA = {
    'airline_iata': 'OP',
    'airline_icao': 'DIG',
    'flight_iata': 'OP146',
    'flight_icao': 'DIG146',
    'flight_number': '146',
    'dep_iata': 'ACC',
    'dep_icao': 'DGAA',
    'dep_terminal': '2',
    'dep_gate': None,
    'dep_time': '2025-01-24 10:00',
    'dep_time_utc': '2025-01-24 10:00',
    'arr_iata': 'KMS',
    'arr_icao': 'DGSI',
    'arr_terminal': None,
    'arr_gate': None,
    'arr_baggage': None,
    'arr_time': '2025-01-24 10:50',
    'arr_time_utc': '2025-01-24 10:50',
    'cs_airline_iata': None,
    'cs_flight_number': None,
    'cs_flight_iata': None,
    'status': 'scheduled',
    'duration': 50,
    'delayed': None,
    'dep_delayed': None,
    'arr_delayed': None,
    'aircraft_icao': None,
    'arr_time_ts': 1737715800,
    'dep_time_ts': 1737712800,
    'time_epoch': 1737712800,
    'time': '2025-01-24 10:00',
    'temp_c': 31.5,
    'temp_f': 88.8,
    'is_day': 1,
    'condition': {
        'text': 'Sunny',
        'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png',
        'code': 1000
    },
    'wind_mph': 3.6,
    'wind_kph': 5.8,
    'wind_degree': 201,
    'wind_dir': 'SSW',
    'pressure_mb': 1013.0,
    'pressure_in': 29.9,
    'precip_mm': 0.0,
    'precip_in': 0.0,
    'snow_cm': 0.0,
    'humidity': 46,
    'cloud': 5,
    'feelslike_c': 33.2,
    'feelslike_f': 91.8,
    'windchill_c': 31.5,
    'windchill_f': 88.8,
    'heatindex_c': 33.2,
    'heatindex_f': 91.8,
    'dewpoint_c': 18.4,
    'dewpoint_f': 65.2,
    'will_it_rain': 0,
    'chance_of_rain': 0,
    'will_it_snow': 0,
    'chance_of_snow': 0,
    'vis_km': 10.0,
    'vis_miles': 6.0,
    'gust_mph': 4.1,
    'gust_kph': 6.6,
    'uv': 5.8,
    'air_quality': {
        'co': 516.15,
        'no2': 2.59,
        'o3': 86.0,
        'so2': 1.48,
        'pm2_5': 30.525,
        'pm10': 65.49,
        'us-epa-index': 2,
        'gb-defra-index': 3
    },
    'name': 'Tafo',
    'region': 'Ashanti',
    'country': 'Ghana',
    'lat': 6.733,
    'lon': -1.617,
    'tz_id': 'Africa/Accra',
    'localtime_epoch': 1737719418,
    'localtime': '2025-01-24 11:50'
}
CLEAN_FLIGHT_DATA = {
    "flight_number": "146",
    "dep_terminal": "2",
    "dep_gate": None,
    "dep_time_utc": "2025-01-24 10:00",
    "arr_time_utc": "2025-01-24 10:50",
    "duration": 50,
    "condition": "Sunny",
    "temp_c": 31.5,
    "dest_name": "Tafo",
    "dest_country": "Ghana"
}

class TestLoadWeather():
    """ Contains tests of the load_weather_for_location function. """

    @staticmethod
    def test_calls_requests_get_method(requests_mock):
        """ Test to see whether a GET request is called. """
        print(
            f"http://api.weatherapi.com/v1/forecast.json?key={environ["WEATHER_API_KEY"]}&q=1,1&unixdt=1&aqi=yes")
        requests_mock.get(
            f"http://api.weatherapi.com/v1/forecast.json?key={environ["WEATHER_API_KEY"]}&q=1,1&unixdt=1262304000&aqi=yes", status_code=200, json={})
        load_weather_for_location(1, 1, 1262304000)

        assert requests_mock.called
        assert requests_mock.call_count == 1
        assert requests_mock.last_request.method == "GET"

    @staticmethod
    def test_http_error_raised(requests_mock):
        """ Test to see whether a HTTPError is raised if the GET request fails. """
        with pytest.raises(requests.HTTPError):
            requests_mock.get(
                f"http://api.weatherapi.com/v1/forecast.json?key={environ["WEATHER_API_KEY"]}&q=1,1&unixdt=1262304000&aqi=yes", status_code=400, json={'error':{'message':'Bad API key'}})
            load_weather_for_location(1, 1, 1262304000)

    @staticmethod
    def test_non_number_lat():
        """ Test to see whether a TypeError is raised when the latitude is not a number. """
        with pytest.raises(TypeError):
            load_weather_for_location("test", 1, 1262304000)

    @staticmethod
    def test_non_number_lng():
        """ Test to see whether a TypeError is raised when the longitude is not a number. """
        with pytest.raises(TypeError):
            load_weather_for_location(1, "test", 1262304000)

    @staticmethod
    def test_non_number_timestamp():
        """ Test to see whether a TypeError is raised when the timestamp is not a number. """
        with pytest.raises(TypeError):
            load_weather_for_location(1, 1, "test")

    @staticmethod
    def test_timestamp_too_early():
        """ Test to see whether a ValueError is raised when the timestamp is before 1st Jan 2010. """
        with pytest.raises(ValueError):
            load_weather_for_location(1, 1, 1262300000)

    @staticmethod
    def test_lat_too_high():
        """ Test to see whether a ValueError is raised when the latitude is too high. """
        with pytest.raises(ValueError):
            load_weather_for_location(90.5, 1, 1362300000)

    @staticmethod
    def test_lat_too_low():
        """ Test to see whether a ValueError is raised when the latitude is too low. """
        with pytest.raises(ValueError):
            load_weather_for_location(-90.5, 1, 1362300000)

    @staticmethod
    def test_lng_too_high():
        """ Test to see whether a ValueError is raised when the longitude is too high. """
        with pytest.raises(ValueError):
            load_weather_for_location(1, 180.5, 1362300000)

    @staticmethod
    def test_lng_too_low():
        """ Test to see whether a ValueError is raised when the longitude is too low. """
        with pytest.raises(ValueError):
            load_weather_for_location(1, -180.5, 1362300000)

class TestFlightDataCleaner():
    """ A class to test the flight_data_cleaner function. """
    @staticmethod
    def test_flight_data_correctly_cleaned():
        """ Test to see whether the flight data is correctly returned with only desired components. """
        assert flight_data_cleaner([UNCLEAN_FLIGHT_DATA]) == [CLEAN_FLIGHT_DATA]

    @staticmethod
    def test_error_raised_if_no_flights():
        """ Test to see whether a ValueError is raised when there are no flights given. """
        with pytest.raises(ValueError):
            flight_data_cleaner([])
    
    @staticmethod
    def test_error_raised_if_non_list_given():
        """ Test to see whether a TypeError is raised when the flight data given is not a list. """
        with pytest.raises(TypeError):
            flight_data_cleaner(UNCLEAN_FLIGHT_DATA)

    @staticmethod
    def test_error_raised_if_flights_not_dict():
        """ Test to see whether a TypeError is raised when the flights within the flight data are not dicts. """
        with pytest.raises(TypeError):
            flight_data_cleaner(['test', 'test2'])

class TestAddWeather():
    """ A class to test the add_weather_to_flights function. """
    @staticmethod
    def test_error_raised_if_no_flights():
        """ Test to see whether a ValueError is raised when there are no flights given. """
        with pytest.raises(ValueError):
            add_weather_to_flights([])

    @staticmethod
    def test_error_raised_if_non_list_given():
        """ Test to see whether a TypeError is raised when the flight data given is not a list. """
        with pytest.raises(TypeError):
            add_weather_to_flights(UNCLEAN_FLIGHT_DATA)

    @staticmethod
    def test_error_raised_if_flights_not_dict():
        """ Test to see whether a TypeError is raised when the flights within the flight data are not dicts. """
        with pytest.raises(TypeError):
            add_weather_to_flights(['test', 'test2'])

class TestRoundHour():
    """ A class to test the round_to_nearest_hour function. """
    @staticmethod
    def test_error_raised_if_not_datetime():
        """ Test to see whether a TypeError is raised when the input is not a datetime object. """
        with pytest.raises(TypeError):
            round_to_nearest_hour('27/08/2002')

    @staticmethod
    def test_rounded_correctly_up():
        """ Test to see whether the datetime object is correctly rounded to the nearest hour upwards. """
        assert round_to_nearest_hour(datetime(2002,8,27,13,35,0)) == datetime(2002,8,27,14,0,0)

    @staticmethod
    def test_rounded_correctly_down():
        """ Test to see whether the datetime object is correctly rounded to the nearest hour downwards. """
        assert round_to_nearest_hour(
            datetime(2002, 8, 27, 13, 25, 0)) == datetime(2002, 8, 27, 13, 0, 0)


class TestRemoveMinutes():
    """ A class to test the round_to_nearest_hour function. """
    @staticmethod
    def test_error_raised_if_not_datetime():
        """ Test to see whether a TypeError is raised when the input is not a datetime object."""
        with pytest.raises(TypeError):
            remove_minutes('27/08/2002')

    @staticmethod
    def test_removed_correctly():
        """ Test to see whether the datetime object is correctly stripped of its minutes/seconds. """
        assert remove_minutes(
            datetime(2002, 8, 27, 13, 35, 0)) == datetime(2002, 8, 27, 13, 0, 0)

class TestFlightsFromIATA():
    """ A class to test the get_flights_from_iata function. """
    @staticmethod
    def test_calls_requests_get_method(requests_mock):
        """ Test to see whether a GET request is called. """
        requests_mock.get(
            f"https://airlabs.co/api/v9/schedules?dep_iata=ABCD&api_key={environ["AIRLABS_API_KEY"]}", status_code=200, json={})
        get_flights_from_iata("ABCD")

        assert requests_mock.called
        assert requests_mock.call_count == 1
        assert requests_mock.last_request.method == "GET"

    @staticmethod
    def test_http_error_raised(requests_mock):
        """ Test to see whether a HTTPError is raised if the GET request fails. """
        with pytest.raises(requests.HTTPError):
            requests_mock.get(
                f"https://airlabs.co/api/v9/schedules?dep_iata=ABCD&api_key={environ["AIRLABS_API_KEY"]}", status_code=404, json={'error': {'message': 'Bad API key'}})
            get_flights_from_iata("ABCD")

    @staticmethod
    def test_error_raised_if_non_string():
        """ Test to see whether a TypeError is raised when the input is not a string. """
        with pytest.raises(TypeError):
            get_flights_from_iata(192)


class TestAirportFromIATA():
    """ A class to test the find_airport_from_iata function. """
    @staticmethod
    def test_calls_requests_get_method(requests_mock):
        """ A class to test the get_flights_from_iata function. """
        requests_mock.get(
            f"https://airlabs.co/api/v9/airports?iata_code=ABCD&api_key={environ["AIRLABS_API_KEY"]}", status_code=200, json={'response': [0]})
        find_airport_from_iata("ABCD")

        assert requests_mock.called
        assert requests_mock.call_count == 1
        assert requests_mock.last_request.method == "GET"

    @staticmethod
    def test_http_error_raised(requests_mock):
        """ Test to see whether a HTTPError is raised if the GET request fails. """
        with pytest.raises(requests.HTTPError):
            requests_mock.get(
                f"https://airlabs.co/api/v9/airports?iata_code=ABCD&api_key={environ["AIRLABS_API_KEY"]}", status_code=404, json={'error': {'message': 'Bad API key'}})
            find_airport_from_iata("ABCD")

    @staticmethod
    def test_error_raised_if_non_string():
        """ Test to see whether a TypeError is raised when the input is not a string. """
        with pytest.raises(TypeError):
            find_airport_from_iata(192)

class TestChooseDesiredAirport():
    """ A class to test the choose_desired_airport function. """

    @staticmethod
    def test_error_raised():
        """ Test to see whether a ValueError is raised when the airport matches list is empty. """
        with pytest.raises(ValueError):
            choose_desired_airport([])
