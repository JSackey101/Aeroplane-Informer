# pylint: skip-file

import pytest
from airports import AIRLABS_API_KEY, WEATHER_API_KEY, load_weather_for_location, flight_data_cleaner, add_weather_to_flights, round_to_hour, get_flights_from_iata, find_airport_from_iata, choose_desired_airport
import requests_mock
import requests
from datetime import datetime

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
        print(f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q=1,1&unixdt=1&aqi=yes")
        requests_mock.get(
            f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q=1,1&unixdt=1262304000&aqi=yes", status_code=200, json={})
        load_weather_for_location(1, 1, 1262304000)

        assert requests_mock.called
        assert requests_mock.call_count == 1
        assert requests_mock.last_request.method == "GET"

    @staticmethod
    def test_http_error_raised(requests_mock):
        with pytest.raises(requests.HTTPError):
            requests_mock.get(
                f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q=1,1&unixdt=1262304000&aqi=yes", status_code=404, json={})
            load_weather_for_location(1, 1, 1262304000)

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

class TestFlightDataCleaner():
    """ A class to test the flight_data_cleaner function. """
    @staticmethod
    def test_flight_data_correctly_cleaned():
        assert flight_data_cleaner([UNCLEAN_FLIGHT_DATA]) == [CLEAN_FLIGHT_DATA]

    @staticmethod
    def test_error_raised_if_no_flights():
        with pytest.raises(ValueError):
            flight_data_cleaner([])
    
    @staticmethod
    def test_error_raised_if_non_list_given():
        with pytest.raises(TypeError):
            flight_data_cleaner(UNCLEAN_FLIGHT_DATA)

    @staticmethod
    def test_error_raised_if_flights_not_dict():
        with pytest.raises(TypeError):
            flight_data_cleaner(['test', 'test2'])

class TestAddWeather():
    """ A class to test the add_weather_to_flights function. """
    @staticmethod
    def test_error_raised_if_no_flights():
        with pytest.raises(ValueError):
            add_weather_to_flights([])

    @staticmethod
    def test_error_raised_if_non_list_given():
        with pytest.raises(TypeError):
            add_weather_to_flights(UNCLEAN_FLIGHT_DATA)

    @staticmethod
    def test_error_raised_if_flights_not_dict():
        with pytest.raises(TypeError):
            add_weather_to_flights(['test', 'test2'])

class TestRoundHour():
    """ A class to test the round_to_hour function. """
    @staticmethod
    def test_error_raised_if_flights_not_dict():
        with pytest.raises(TypeError):
            round_to_hour('27/08/2002')

    @staticmethod
    def test_rounded_correctly():
        assert round_to_hour(datetime(2002,8,27,13,35,0)) == datetime(2002,8,27,14,0,0)

class TestFlightsFromIATA():
    """ A class to test the get_flights_from_iata function. """
    @staticmethod
    def test_calls_requests_get_method(requests_mock):
        requests_mock.get(
            f"https://airlabs.co/api/v9/schedules?dep_iata=ABCD&api_key={AIRLABS_API_KEY}", status_code=200, json={})
        get_flights_from_iata("ABCD")

        assert requests_mock.called
        assert requests_mock.call_count == 1
        assert requests_mock.last_request.method == "GET"

    @staticmethod
    def test_http_error_raised(requests_mock):
        with pytest.raises(requests.HTTPError):
            requests_mock.get(
                f"https://airlabs.co/api/v9/schedules?dep_iata=ABCD&api_key={AIRLABS_API_KEY}", status_code=404, json={})
            get_flights_from_iata("ABCD")

    @staticmethod
    def test_error_raised_if_non_string():
        with pytest.raises(TypeError):
            get_flights_from_iata(192)


class TestAirportFromIATA():
    """ A class to test the find_airport_from_iata function. """
    @staticmethod
    def test_calls_requests_get_method(requests_mock):
        requests_mock.get(
            f"https://airlabs.co/api/v9/airports?iata_code=ABCD&api_key={AIRLABS_API_KEY}", status_code=200, json={'response': [0]})
        find_airport_from_iata("ABCD")

        assert requests_mock.called
        assert requests_mock.call_count == 1
        assert requests_mock.last_request.method == "GET"

    @staticmethod
    def test_http_error_raised(requests_mock):
        with pytest.raises(requests.HTTPError):
            requests_mock.get(
                f"https://airlabs.co/api/v9/airports?iata_code=ABCD&api_key={AIRLABS_API_KEY}", status_code=404, json={'response': [0]})
            find_airport_from_iata("ABCD")

    @staticmethod
    def test_error_raised_if_non_string():
        with pytest.raises(TypeError):
            find_airport_from_iata(192)

class TestChooseDesiredAirport():
    """ A class to test the choose_desired_airport function. """

    @staticmethod
    def test_error_raised():
        with pytest.raises(ValueError):
            choose_desired_airport([])