""" A program to find and display flight data. """

import argparse
import json
from datetime import datetime, timedelta
import requests
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table


console = Console(record=True)
FLIGHT_DATE_FORMAT = '%Y-%m-%d %H:%M'
WEATHER_API_KEY = "***REMOVED***"
AIRLABS_API_KEY = "***REMOVED***"

class ErrorRaising():
    """ A class for raising errors. """
    @staticmethod
    def validate_load_weather_for_location(lat: float | int, lng: float | int,
                                            timestamp: float | int) -> None:
        """ Validates input Latitude, Longitude and Unix Timestamp data. """
        if not isinstance(lat, (float, int)):
            raise TypeError("Latitude must be a number.")
        if lat > 90 or lat < -90:
            raise ValueError("Invalid Latitude value.")
        if not isinstance(lng, (float, int)):
            raise TypeError("Longitude must be a number.")
        if lng > 180 or lng < -180:
            raise ValueError("Invalid Longitude value.")
        if not isinstance(timestamp, (float, int)):
            raise TypeError("Timestamp must be a number.")
        if timestamp < 1262304000:
            raise ValueError("Invalid Timestamp. Must be on/after 1st Jan 2010. ")
    @staticmethod
    def validate_flights_in_list(flights: list):
        """ Validates that there are flights in the list. """
        if len(flights) == 0:
            raise ValueError("There must be at least 1 flight. ")
    @staticmethod
    def validate_list_input(flights: list):
        """ Validates that the input is a list. """
        if not isinstance(flights, list):
            raise TypeError("The flights must be a list.")
    @staticmethod
    def validate_dicts_in_list(flights: list):
        """ Validates that the inputs within the list are dicts. """
        if not all(isinstance(flight, dict) for flight in flights):
            raise TypeError("Each flight must be a dict.")

    @staticmethod
    def validate_input_is_datetime(datetime_obj: datetime):
        """ Validates that the input is a datetime object"""
        if not isinstance(datetime_obj, datetime):
            raise TypeError("The date/time must be given as a datetime object.")
    @staticmethod
    def validate_input_is_str(string: str):
        """ Validates that the input is a string. """
        if not isinstance(string, str):
            raise TypeError("The input must be a string.")
        
    @staticmethod
    def raise_error_airlabs_api():
        """ Raises an error when the Airlabs API key reaches limit. """
        raise requests.HTTPError("Airlabs API key has reached the usage limit.")

def load_weather_for_location(lat: float, lng: float, 
                              timestamp:float =datetime.now().timestamp()) -> dict:
    """Given a location, load the current weather for that location"""
    ErrorRaising.validate_load_weather_for_location(lat, lng, timestamp)
    response = requests.get(
        f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={lat},{lng}&unixdt={timestamp}&aqi=yes",
        timeout=10)
    response.raise_for_status()
    return response.json()

def flight_data_cleaner(flights: list) -> list:
    """ Takes a list of flights and returns only the needed flight data. """
    ErrorRaising.validate_flights_in_list(flights)
    ErrorRaising.validate_list_input(flights)
    ErrorRaising.validate_dicts_in_list(flights)
    clean_flights = []
    for flight in flights:
        clean_flight = {
            'flight_number': flight['flight_number'],
            'dep_terminal': flight['dep_terminal'],
            'dep_gate': flight['dep_gate'],
            'dep_time_utc': flight['dep_time_utc'],
            'arr_time_utc': flight['arr_time_utc'],
            'duration': flight['duration'],
            'condition': flight['condition']['text'],
            'temp_c': flight['temp_c'], 
            'dest_name': flight['name'],
            'dest_country': flight['country']
        }
        clean_flights.append(clean_flight)
    return clean_flights

def add_weather_to_flights(flights: list) -> None:
    """ Add the weather data to the flights. """
    ErrorRaising.validate_flights_in_list(flights)
    ErrorRaising.validate_list_input(flights)
    ErrorRaising.validate_dicts_in_list(flights)
    for i, flight in enumerate(flights):
        arrival_date_obj = datetime.strptime(flight['arr_time_utc'], FLIGHT_DATE_FORMAT)
        arrival_date_obj = round_to_hour(arrival_date_obj)
        airport_info = find_airport_from_iata(flight['arr_iata'])
        weather = load_weather_for_location(float(airport_info['lat']),
                                            float(airport_info['lng']), 
                                            arrival_date_obj.timestamp())
        flights[i] = flight | [
            hour for hour in weather['forecast']['forecastday'][0]['hour'] if 
            hour['time_epoch'] == arrival_date_obj.timestamp()][0] | weather['location']

def round_to_hour(datetime_obj: datetime) -> "datetime":
    """ Returns a datetime object rounded to the nearest hour. """
    ErrorRaising.validate_input_is_datetime(datetime_obj)
    round_time = timedelta(hours=datetime_obj.minute // 30)
    datetime_obj = datetime_obj.replace(minute=0, second=0, microsecond=0)
    return datetime_obj + round_time

def render_flights(flights: list) -> None:
    """Render a list of flights to the console using the Rich Library

    Consider using Panels, Grids, Tables or any of the more advanced
    features of the library"""
    table = Table(title="Flight Data")

    table.add_column("Flight Number")
    table.add_column("Terminal")
    table.add_column("Gate")
    table.add_column("Departure\nTime (UTC)")
    table.add_column("Arrival\nTime (UTC)")
    table.add_column("Destination")
    table.add_column("Duration\n(minutes)")
    table.add_column("Temperature\n(Degrees)")
    table.add_column("Weather Condition")

    for flight in flights:
        table.add_row(flight['flight_number'],
                      flight['dep_gate'] if flight['dep_gate'] is not None else "N/A",
                      flight['dep_terminal'] if flight['dep_terminal'] is not None else "N/A",
                      flight['dep_time_utc'], flight['arr_time_utc'],
                      f"{flight['dest_name']}, {flight['dest_country']}",
                      str(flight['duration']),
                      str(flight['temp_c']),
                      flight['condition'])
    console.print(table)


def get_flights_from_iata(iata: str) -> list:
    """Given an IATA get the flights that are departing from that airport from Airlabs"""
    ErrorRaising.validate_input_is_str(iata)
    response = requests.get(f"https://airlabs.co/api/v9/schedules?dep_iata={iata}&api_key={AIRLABS_API_KEY}"
                            , timeout=10)
    response.raise_for_status()
    try:
        response.json()['response']
    except KeyError:
        ErrorRaising.raise_error_airlabs_api()
    return response.json()


def find_airport_from_iata(iata: str) -> list:
    """Given an IATA get the Airport that matches the IATA from Airlabs. """
    ErrorRaising.validate_input_is_str(iata)
    response = requests.get(
        f"https://airlabs.co/api/v9/airports?iata_code={iata}&api_key={AIRLABS_API_KEY}",
        timeout=10)
    response.raise_for_status()
    try:
        return response.json()['response'][0]
    except KeyError:
        ErrorRaising.raise_error_airlabs_api()


def load_airport_json() -> list[dict]:
    """Returns airport information loaded from a file."""
    with open("airports.json", "r", encoding="UTF-8") as airports:
        airport_json = json.load(airports)
    return airport_json


def find_airports_from_name(name: str, airport_data_input: list) -> list:
    """
    Find an airport from the airport_data given a name
    Could return one or more airport objects
    """
    ErrorRaising.validate_input_is_str(name)
    ErrorRaising.validate_list_input(airport_data_input)
    ErrorRaising.validate_dicts_in_list(airport_data_input)
    matches = [airport for airport in airport_data_input if name in str(airport['name'])]
    return matches

def choose_desired_airport(airport_matches: list) -> dict:
    """ Takes a list of airports and returns the correct match. """
    if len(airport_matches) == 0:
        raise ValueError("No airports found.")
    if len(airport_matches) > 1:
        airport_choice = Prompt.ask("Multiple airports found, please choose one: ", choices=[
                                    airport['name'] for airport in airport_matches])
        return list(airport for airport in airport_matches if airport['name'] == airport_choice)[0]
    return airport_matches[0]

def setup_command_line_arguments(options: list[str], choices: list) -> "argparse.Namespace":
    """ Takes command line input and returns it as a Namespace object. """
    parser = argparse.ArgumentParser()
    for index, option in enumerate(options):
        parser.add_argument(option, choices=choices[index])
    args = parser.parse_args()
    return args

def export_html(name: str) -> None:
    """ Exports the Console as a HTML file. """
    console.save_html(f"Search-{name}-{datetime.now().ctime()}.html")

def export_json(name: str, flight_data_input: list) -> None:
    """ Exports the Console as a JSON file. """
    with open(f"Search-{name}-{datetime.now().ctime()}.json", "w", encoding='UTF-8') as json_file:
        json.dump(flight_data_input, json_file)
        

if __name__ == "__main__":
    airport_data = load_airport_json()
    command_line_input = setup_command_line_arguments(["--airport", "--export"],
                                                      [None, ['JSON', 'HTML']])
    airport_name = command_line_input.airport
    console.print(f"You are searching for {airport_name}.")

    airport = choose_desired_airport(find_airports_from_name(airport_name, airport_data))
    flight_data = get_flights_from_iata(airport['iata'])

    add_weather_to_flights(flight_data['response'])
    clean_flight_data = flight_data_cleaner(flight_data['response'])

    render_flights(clean_flight_data)

    if command_line_input.export == 'HTML':
        export_html(airport['name'])
    if command_line_input.export == 'JSON':
        export_json(airport['name'], clean_flight_data)
