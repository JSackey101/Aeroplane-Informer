import requests
from rich.prompt import Prompt
from rich.console import Console

# Instead of using print(), you should use the Console from Rich instead.
console = Console()


def loadWeatherForLocation(lat, lng):
    # Given a location, load the current weather for that location
    return {}


def renderFlights(flights):
    # Render a list of flights to the console using the Rich Library
    #
    # Consider using Panels, Grids, Tables or any of the more advanced
    # features of the library
    console.print(flights)


def getFlightsFromIata(iata):
    # Given an IATA get the flights that are departing from that airport from Airlabs
    return {}


def loadAirportJSON():
    # Load airport data from airports.json
    return []


def findAirportsFromName(name, airportData):
    # Find an airport from the airportData given a name
    # Could return one or more airport objects

    return []


def findAirportFromIata(iata, airportData):
    # Find an airport from the airportData given a name
    # Should return exactly one airport object

    return {}


def getSearch():
    return Prompt.ask("Search for an an airport")


def main():
    console.print(" ")
    console.print("✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️")
    console.print("Welcome to the Airports Informer Tool")
    console.print("✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️")
    console.print(" ")

    airportData = loadAirportJSON()

    while 1:
        airportSearch = getSearch()


main()
