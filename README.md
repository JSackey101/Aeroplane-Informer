# Aeroplane Informer

## Description

Sends requests to the [Airlabs API](https://airlabs.co/) used for Aviation Data and the [Weather API](https://www.weatherapi.com/) used for Weather data.

Program can:

- Search for any Airport in the world.
- Find all the flights leaving that airport.
- Extract the location of all of the destinations of the airports.
- Combine that data with the weather at each of the destinations of the flights.
- Display a Table containing flight information alongside important destination weather details for the airport.
- Export this table to a HTML file 
- Export the combined data into a JSON file.

## Installation Instructions

Install dependencies with:

```
pip install -r requirements.txt
```
## Before Use

You will need both an [Airlabs API](https://airlabs.co/) key and a [Weather API](https://www.weatherapi.com/) key to use this program.

You will need to sign up to both sites to get the keys.

Once you get the keys, you should place them under the respective variables in the .env file.

Example:
```
WEATHER_API_KEY=[Your Weather API key]
AIRLABS_API_KEY=[Your Airlabs API key]
```

NOTE:

As of the 25th of February 2025, Airlabs registrations are undergoing manual verification so this may impact your ability to obtain a key.


## Usage
To obtain a console print of the table, run:

```
python3 airports.py --airport [Name of Desired Airport]
```

To obtain a console print of the table and export the table as HTML, run:

```
python3 airports.py --airport [Name of Desired Airport] --export HTML
```

To obtain a console print of the table and export the flight data as JSON, run:

```
python3 airports.py --airport [Name of Desired Airport] --export JSON
```

### Future Work

- Currently the airport data is obtained from a provided JSON file with airports - this is used to gain flight data.
  I would like to make use of Airlabs for the airport data too and remove the JSON file entirely.
  This would allow for more detailed information and better/more up-to-date airport coverage.
- Add progress display for when code is searching the APIs for data.
- Add multiprocessing so requests can run in parallel to speed things up.