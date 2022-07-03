import requests
from rich.prompt import Prompt
from rich.console import Console

# Instead of using print(), you should use the Console from Rich instead.
console = Console()


def loadWeatherForLocation(location):
    # Given a location, load the current weather for that location
    return {}


def loadAirportJSON():
    # Load the data from the airports.json file
    return []


def findAirportFromIATA(iata):
    # Find the airport object from the JSON based on it
    # IATA number and return it
    return {}


def getSearch():
    # Use Prompt to ask the user for their airport search
    return ""


def main():
    console.print(" ")
    console.print("✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️")
    console.print("Welcome to the Airports Informer Tool")
    console.print("✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️ ✈️")
    console.print(" ")

    while 1:
        search = getSearch()
        # Then do something with the search


main()
