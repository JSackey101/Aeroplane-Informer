import requests
from rich.prompt import Prompt
from rich.console import Console
import argparse

# Instead of using print(), you should use the Console from Rich instead.
console = Console()


def load_weather_for_location(lat: str, lng: str) -> dict:
    """Given a location, load the current weather for that location"""
    ...


def render_flights(flights: list) -> None:
    """Render a list of flights to the console using the Rich Library

    Consider using Panels, Grids, Tables or any of the more advanced
    features of the library"""

    console.print(flights)


def get_flights_from_iata(iata: str) -> list:
    """Given an IATA get the flights that are departing from that airport from Airlabs"""
    ...


def load_airport_JSON() -> list[dict]:
    """Returns airport information loaded from a file."""
    ...


def find_airports_from_name(name: str, airport_data: list) -> list:
    """
    Find an airport from the airport_data given a name
    Could return one or more airport objects
    """
    ...

if __name__ == "__main__":
    airport_data = load_airport_JSON()
    airport_name = input("Enter an airport: ")
    print(f"You are searching for {airport_name}.")
