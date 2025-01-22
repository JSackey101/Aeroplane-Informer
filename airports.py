import requests
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
import argparse
import json

# Instead of using print(), you should use the Console from Rich instead.
console = Console()


def load_weather_for_location(lat: str, lng: str) -> dict:
    """Given a location, load the current weather for that location"""
    ...


def render_flights(flights: list) -> None:
    """Render a list of flights to the console using the Rich Library

    Consider using Panels, Grids, Tables or any of the more advanced
    features of the library"""
    table = Table(title="Flight Data")

    table.add_column("Airline")
    table.add_column("Flight Number")
    table.add_column("Terminal")
    table.add_column("Gate")
    table.add_column("Departure Time (UTC)")
    table.add_column("Arrival Time (UTC)")

    for flight in flights:
        table.add_row(flight['dep_iata'], flight['flight_number'], flight['dep_gate'],
                       flight['dep_terminal'], flight['dep_time_utc'], flight['arr_time_utc'])
    console.print(table)


def get_flights_from_iata(iata: str) -> list:
    """Given an IATA get the flights that are departing from that airport from Airlabs"""
    response = requests.get(f"https://airlabs.co/api/v9/schedules?dep_iata={iata}&api_key=***REMOVED***"
                            , timeout=10)
    response.raise_for_status()
    return response.json()


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
        return (airport for airport in airport_matches if airport['name'] == airport_choice)
    return airport_matches[0]

def setup_command_line_arguments(option: str) -> "Namespace":
    """ Takes command line input and returns it as a Namespace object. """
    parser = argparse.ArgumentParser()
    parser.add_argument(option)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    airport_data = load_airport_json()
    airport_name = setup_command_line_arguments("--airport").airport
    console.print(f"You are searching for {airport_name}.")

    airport = choose_desired_airport(find_airports_from_name(airport_name, airport_data))
    flight_data = get_flights_from_iata(airport['iata'])
    render_flights(flight_data['response'])