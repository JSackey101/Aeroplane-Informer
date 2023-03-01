import requests
from rich.prompt import Prompt
from rich.console import Console

# Instead of using print(), you should use the Console from Rich instead.
console = Console()


def loadWeatherForLocation(lat: str, lng: str) -> dict:
    """Given a location, load the current weather for that location"""

    return {}


def renderFlights(flights: list) -> None:
    """Render a list of flights to the console using the Rich Library

    Consider using Panels, Grids, Tables or any of the more advanced
    features of the library"""

    console.print(flights)


def getFlightsFromIata(iata: str) -> list:
    """Given an IATA get the flights that are departing from that airport from Airlabs"""

    return []


def loadAirportJSON() -> list:
    """Load airport data from airports.json"""

    return []


def findAirportsFromName(name: str, airportData: list) -> list:
    """
    Find an airport from the airportData given a name
    Could return one or more airport objects
    """

    return []


def findAirportFromIata(iata: str, airportData: list) -> dict:
    """
    Find an airport from the airportData given a name
    Should return exactly one airport object
    """

    return {}


def getSearch() -> str:
    return Prompt.ask("Search for an an airport")


def main() -> None:
    """Repeatedly prompts the user for airport names and displays the result."""

    console.print(" ")
    console.print("✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️")
    console.print("Welcome to the Airports Informer Tool")
    console.print("✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️")
    console.print(" ")

    airportData = loadAirportJSON()

    while 1:
        airportSearch = getSearch()


main()
