""" Contains tests for the Aeroplane Informer. """

from os import environ
from unittest.mock import patch
from datetime import datetime
import pytest
import requests_mock
from airports import (load_weather_for_location, flight_data_cleaner, add_weather_to_flights,
                      round_to_nearest_hour, get_flights_from_iata,
                      find_airport_from_iata, choose_desired_airport, remove_minutes, render_flights,
                      find_airports_from_name)
import requests
from dotenv import load_dotenv

load_dotenv(".env")

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
    def test_flight_data_correctly_cleaned(test_unclean_data, test_clean_data):
        """ Test to see whether the flight data is correctly returned with only desired components. """
        assert flight_data_cleaner([test_unclean_data]) == [test_clean_data]

    @staticmethod
    def test_error_raised_if_no_flights():
        """ Test to see whether a ValueError is raised when there are no flights given. """
        with pytest.raises(ValueError):
            flight_data_cleaner([])
    
    @staticmethod
    def test_error_raised_if_non_list_given(test_unclean_data):
        """ Test to see whether a TypeError is raised when the flight data given is not a list. """
        with pytest.raises(TypeError):
            flight_data_cleaner(test_unclean_data)

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
    def test_error_raised_if_non_list_given(test_unclean_data):
        """ Test to see whether a TypeError is raised when the flight data given is not a list. """
        with pytest.raises(TypeError):
            add_weather_to_flights(test_unclean_data)

    @staticmethod
    def test_error_raised_if_flights_not_dict():
        """ Test to see whether a TypeError is raised when the flights within the flight data are not dicts. """
        with pytest.raises(TypeError):
            add_weather_to_flights(['test', 'test2'])

    @staticmethod
    @patch('airports.load_weather_for_location')
    def test_add_weather(test_load_weather, test_weather_data, test_flight_data, 
                         test_flight_weather_data):
        """ Test to see whether the weather data is correctly added to the flight data. """
        flights = [test_flight_data]
        test_load_weather.return_value = test_weather_data
        add_weather_to_flights(flights)
        assert flights[0] == test_flight_weather_data

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

class TestRenderFlights():
    """ A class to test the render_flights function. """

    @staticmethod
    def test_flight_output_headers(test_flight_data_gate_terminal, capsys):
        """ Test to see whether the Table headers are rendered onto the console. """
        render_flights([test_flight_data_gate_terminal],
                       "London Heathrow Airport")
        str_output = capsys.readouterr().out
        assert "Flight Number" in str_output
        assert "Terminal" in str_output
        assert "Gate" in str_output
        assert "Departure" in str_output
        assert "Time" in str_output
        assert str_output.count('Time') == 2
        assert "(UTC)" in str_output
        assert str_output.count("(UTC)") == 2
        assert "Arrival" in str_output
        assert "Destination" in str_output
        assert str_output.count("Destination") == 3
        assert "Duration" in str_output
        assert "(minutes)" in str_output
        assert "Temperature" in str_output
        assert "(Degrees)" in str_output
        assert "Weather" in str_output
        assert "Condition" in str_output

    @staticmethod
    def test_flight_output_no_gate_terminal(test_flight_data_no_gate_terminal, capsys):
        """ Test to see whether the flight data is correctly rendered onto the console when 
            there is no Gate/Terminal data. """
        render_flights([test_flight_data_no_gate_terminal], "London Heathrow Airport")
        str_output = capsys.readouterr().out
        assert '2515' in str_output
        assert 'N/A' in str_output
        assert str_output.count('N/A') == 2
        assert '2025-02-25' in str_output
        assert '10:25' in str_output
        assert '2025-02-25' in str_output
        assert '11:40' in str_output
        assert '75' in str_output
        assert 'Sunny' in str_output
        assert '8.9' in str_output
        assert 'Lijnden' in str_output
        assert 'Netherlands' in str_output

    @staticmethod
    def test_flight_output_gate_terminal(test_flight_data_gate_terminal, capsys):
        """ Test to see whether the flight data is correctly rendered onto the console when 
            there is Gate/Terminal data. """
        render_flights([test_flight_data_gate_terminal],
                       "London Heathrow Airport")
        str_output = capsys.readouterr().out
        assert '2515' in str_output
        assert 'S' in str_output
        assert '90' in str_output
        assert '2025-02-25' in str_output
        assert '10:25' in str_output
        assert '2025-02-25' in str_output
        assert '11:40' in str_output
        assert '75' in str_output
        assert 'Windy' in str_output
        assert '8.9' in str_output
        assert 'Lijnden' in str_output
        assert 'Netherlands' in str_output

    @staticmethod
    def test_error_raised_if_no_flights():
        """ Test to see whether a ValueError is raised when there are no flights given. """
        with pytest.raises(ValueError):
            render_flights([], "London Heathrow Airport")

    @staticmethod
    def test_error_raised_if_non_list_given(test_unclean_data):
        """ Test to see whether a TypeError is raised when the flight data given is not a list. """
        with pytest.raises(TypeError):
            render_flights(test_unclean_data,
                           "London Heathrow Airport")

    @staticmethod
    def test_error_raised_if_flights_not_dict():
        """ Test to see whether a TypeError is raised when the flights within the flight data are not dicts. """
        with pytest.raises(TypeError):
            render_flights(['test', 'test2'],
                           "London Heathrow Airport")
            
    @staticmethod
    def test_error_raised_if_non_string(test_flight_data_gate_terminal):
        """ Test to see whether a TypeError is raised when the airport_name input is not a string. """
        with pytest.raises(TypeError):
            render_flights([test_flight_data_gate_terminal], 192)

class TestFindAirportsFromName():
    """ A class to test the find_airports_from_name function. """

    @staticmethod
    def test_error_raised_if_no_flights():
        """ Test to see whether a ValueError is raised when there are no flights given. """
        with pytest.raises(ValueError):
            find_airports_from_name("London Heathrow Airport", [])

    @staticmethod
    def test_error_raised_if_non_list_given(test_unclean_data):
        """ Test to see whether a TypeError is raised when the flight data given is not a list. """
        with pytest.raises(TypeError):
            find_airports_from_name("London Heathrow Airport", test_unclean_data)

    @staticmethod
    def test_error_raised_if_flights_not_dict():
        """ Test to see whether a TypeError is raised when the flights within the flight data are not dicts. """
        with pytest.raises(TypeError):
            find_airports_from_name("London Heathrow Airport", ['test', 'test2'])

    @staticmethod
    def test_error_raised_if_non_string(test_flight_data_gate_terminal):
        """ Test to see whether a TypeError is raised when the airport_name input is not a string. """
        with pytest.raises(TypeError):
            find_airports_from_name(192, [test_flight_data_gate_terminal])
