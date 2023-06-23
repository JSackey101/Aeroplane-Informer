import requests
from rich.prompt import Prompt
from rich.console import Console

# Instead of using print(), you should use the Console from Rich instead.
console = Console()


def load_weather_for_location(lat: str, lng: str) -> dict:
    """Given a location, load the current weather for that location"""

    return {}


def render_flights(flights: list) -> None:
    """Render a list of flights to the console using the Rich Library

    Consider using Panels, Grids, Tables or any of the more advanced
    features of the library"""

    console.print(flights)


def get_flights_from_iata(iata: str) -> list:
    """Given an IATA get the flights that are departing from that airport from Airlabs"""

    return []


def load_airport_JSON() -> list:
    """Load airport data from airports.json"""

    return []


def find_airports_from_name(name: str, airport_data: list) -> list:
    """
    Find an airport from the airportData given a name
    Could return one or more airport objects
    """

    return []


def find_airport_from_iata(iata: str, airport_data: list) -> dict:
    """
    Find an airport from the airport_data given a name
    Should return exactly one airport object
    """

    return {}


def get_search() -> str:
    return Prompt.ask("Search for an an airport")


def main() -> None:
    """Repeatedly prompts the user for airport names and displays the result."""

    console.print(" ")
    console.print("✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️")
    console.print("Welcome to the Airports Informer Tool")
    console.print("✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️")
    console.print(" ")

    airport_data = load_airport_JSON()

    while 1:
        airport_search = get_search()


if __name__ == "__main__":
    main()
