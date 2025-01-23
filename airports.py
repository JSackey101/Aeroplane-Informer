import requests
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
import argparse
import json
from datetime import datetime, timedelta

# Instead of using print(), you should use the Console from Rich instead.
console = Console(record=True)
FLIGHT_DATE_FORMAT = '%Y-%m-%d %H:%M'



def load_weather_for_location(lat: str, lng: str, 
                              timestamp:int =datetime.now().timestamp()) -> dict:
    """Given a location, load the current weather for that location"""
    response = requests.get(
        f"http://api.weatherapi.com/v1/forecast.json?key=***REMOVED***&q={lat},{lng}&unixdt={timestamp}&aqi=yes",
        timeout=10)
    response.raise_for_status()
    return response.json()

def add_weather_to_flights(flights: list) -> None:
    """ Add the weather data to the flights. """
    for i, flight in enumerate(flights):
        arrival_date_obj = datetime.strptime(flight['arr_time_utc'], FLIGHT_DATE_FORMAT)
        arrival_date_obj = round_to_hour(arrival_date_obj)
        airport_info = find_airport_from_iata(flight['arr_iata'])
        weather = load_weather_for_location(airport_info['lat'],
                                            airport_info['lng'], arrival_date_obj.timestamp())
        flights[i] = flight | [
            hour for hour in weather['forecast']['forecastday'][0]['hour'] if hour['time_epoch'] == arrival_date_obj.timestamp()][0]

def round_to_hour(datetime_obj: datetime) -> "datetime":
    """ Returns a datetime object rounded to the nearest hour (?)"""
    datetime_obj = datetime_obj.replace(minute=0, second=0, microsecond=0)
    round_time = timedelta(hours = datetime_obj.minute // 30)
    return datetime_obj + round_time

def render_flights(flights: list) -> None:
    """Render a list of flights to the console using the Rich Library

    Consider using Panels, Grids, Tables or any of the more advanced
    features of the library"""
    table = Table(title="Flight Data")

    table.add_column("Flight Number")
    table.add_column("Terminal")
    table.add_column("Gate")
    table.add_column(f"Departure\nTime (UTC)")
    table.add_column(f"Arrival\nTime (UTC)")
    table.add_column(f"Temperature\n(Degrees)")
    table.add_column("Weather Condition")

    for flight in flights:
        table.add_row(flight['flight_number'], 
                      flight['dep_gate'] if flight['dep_gate'] is not None else "N/A",
                      flight['dep_terminal'] if flight['dep_terminal'] is not None else "N/A",
                      flight['dep_time_utc'], flight['arr_time_utc'], str(flight['temp_c']),
                      flight['condition']['text'])
    console.print(table)


def get_flights_from_iata(iata: str) -> list:
    """Given an IATA get the flights that are departing from that airport from Airlabs"""
    response = requests.get(f"https://airlabs.co/api/v9/schedules?dep_iata={iata}&api_key=***REMOVED***"
                            , timeout=10)
    response.raise_for_status()
    return response.json()


def find_airport_from_iata(iata: str) -> list:
    """Given an IATA get the Airport that matches the IATA from Airlabs. """
    response = requests.get(
        f"https://airlabs.co/api/v9/airports?iata_code={iata}&api_key=***REMOVED***",
        timeout=10)
    response.raise_for_status()
    return response.json()['response'][0]


def load_airport_json() -> list[dict]:
    """Returns airport information loaded from a file."""
    with open("airports.json", "r", encoding="UTF-8") as airports:
        airport_json = json.load(airports)
    return airport_json


def find_airports_from_name(name: str, airport_data: list) -> list:
    """
    Find an airport from the airport_data given a name
    Could return one or more airport objects
    """
    matches = [airport for airport in airport_data if name in str(airport['name'])]
    return matches

def choose_desired_airport(airport_matches: str) -> dict:
    """ Takes a list of airports and returns the correct match. """
    if len(airport_matches) == 0:
        raise ValueError("No airports found.")
    if len(airport_matches) > 1:
        airport_choice = Prompt.ask("Multiple airports found, please choose one: ", choices=[
                                    airport['name'] for airport in airport_matches])
        return list(airport for airport in airport_matches if airport['name'] == airport_choice)[0]
    return airport_matches[0]

def setup_command_line_arguments(options: list[str], choices: list) -> "Namespace":
    """ Takes command line input and returns it as a Namespace object. """
    parser = argparse.ArgumentParser()
    for index, option in enumerate(options):
        parser.add_argument(option, choices=choices[index])
    args = parser.parse_args()
    return args

def export_html(name: str) -> None:
    """ Exports the Console as a HTML file. """
    console.save_html(f"Search-{name}-{datetime.now().ctime()}.html")

def export_json(name: str) -> None:
    """ Exports the Console as a JSON file. """
    text_data = console.export_html()
    json_data = json.dumps(text_data)
    with open(f"Search-{name}-{datetime.now().ctime()}.json", "w", encoding='UTF-8') as json_file:
        json_file.write(json_data)
        

if __name__ == "__main__":
    airport_data = load_airport_json()
    command_line_input = setup_command_line_arguments(["--airport", "--export"],
                                                      [None, ['JSON', 'HTML']])
    airport_name = command_line_input.airport
    console.print(f"You are searching for {airport_name}.")

    airport = choose_desired_airport(find_airports_from_name(airport_name, airport_data))
    flight_data = get_flights_from_iata(airport['iata'])

    add_weather_to_flights(flight_data['response'])

    render_flights(flight_data['response'])

    if command_line_input.export == 'HTML':
        export_html(airport['name'])
    if command_line_input.export == 'JSON':
        export_json(airport['name'])
