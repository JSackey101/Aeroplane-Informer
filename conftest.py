

import pytest

@pytest.fixture()
def test_unclean_data():
    """ Returns the unclean flight data. """
    return {
        'airline_iata': 'OP',
        'airline_icao': 'DIG',
        'flight_iata': 'OP146',
        'flight_icao': 'DIG146',
        'flight_number': '146',
        'dep_iata': 'ACC',
        'dep_icao': 'DGAA',
        'dep_terminal': '2',
        'dep_gate': None,
        'dep_time': '2025-01-24 10:00',
        'dep_time_utc': '2025-01-24 10:00',
        'arr_iata': 'KMS',
        'arr_icao': 'DGSI',
        'arr_terminal': None,
        'arr_gate': None,
        'arr_baggage': None,
        'arr_time': '2025-01-24 10:50',
        'arr_time_utc': '2025-01-24 10:50',
        'cs_airline_iata': None,
        'cs_flight_number': None,
        'cs_flight_iata': None,
        'status': 'scheduled',
        'duration': 50,
        'delayed': None,
        'dep_delayed': None,
        'arr_delayed': None,
        'aircraft_icao': None,
        'arr_time_ts': 1737715800,
        'dep_time_ts': 1737712800,
        'time_epoch': 1737712800,
        'time': '2025-01-24 10:00',
        'temp_c': 31.5,
        'temp_f': 88.8,
        'is_day': 1,
        'condition': {
            'text': 'Sunny',
            'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png',
            'code': 1000
        },
        'wind_mph': 3.6,
        'wind_kph': 5.8,
        'wind_degree': 201,
        'wind_dir': 'SSW',
        'pressure_mb': 1013.0,
        'pressure_in': 29.9,
        'precip_mm': 0.0,
        'precip_in': 0.0,
        'snow_cm': 0.0,
        'humidity': 46,
        'cloud': 5,
        'feelslike_c': 33.2,
        'feelslike_f': 91.8,
        'windchill_c': 31.5,
        'windchill_f': 88.8,
        'heatindex_c': 33.2,
        'heatindex_f': 91.8,
        'dewpoint_c': 18.4,
        'dewpoint_f': 65.2,
        'will_it_rain': 0,
        'chance_of_rain': 0,
        'will_it_snow': 0,
        'chance_of_snow': 0,
        'vis_km': 10.0,
        'vis_miles': 6.0,
        'gust_mph': 4.1,
        'gust_kph': 6.6,
        'uv': 5.8,
        'air_quality': {
            'co': 516.15,
            'no2': 2.59,
            'o3': 86.0,
            'so2': 1.48,
            'pm2_5': 30.525,
            'pm10': 65.49,
            'us-epa-index': 2,
            'gb-defra-index': 3
        },
        'name': 'Tafo',
        'region': 'Ashanti',
        'country': 'Ghana',
        'lat': 6.733,
        'lon': -1.617,
        'tz_id': 'Africa/Accra',
        'localtime_epoch': 1737719418,
        'localtime': '2025-01-24 11:50'
    }

@pytest.fixture()
def test_clean_data():
    """ Returns the clean flight data. """
    return {
        "flight_number": "146",
        "dep_terminal": "2",
        "dep_gate": None,
        "dep_time_utc": "2025-01-24 10:00",
        "arr_time_utc": "2025-01-24 10:50",
        "duration": 50,
        "condition": "Sunny",
        "temp_c": 31.5,
        "dest_name": "Tafo",
        "dest_country": "Ghana"
    }

@pytest.fixture()
def test_flight_data_gate_terminal():
    """ Returns 1 instance of flight data. """
    return {'flight_number': '2515', 'dep_terminal': '90', 'dep_gate': "S",
            'dep_time_utc': '2025-02-25 10:25', 'arr_time_utc': '2025-02-25 11:40',
            'duration': 75, 'condition': 'Windy', 'temp_c': 8.9, 
            'dest_name': 'Lijnden', 'dest_country': 'Netherlands'}


@pytest.fixture()
def test_flight_data_no_gate_terminal():
    """ Returns 1 instance of flight data. """
    return {'flight_number': '2515', 'dep_terminal': None, 'dep_gate': None,
            'dep_time_utc': '2025-02-25 10:25', 'arr_time_utc': '2025-02-25 11:40',
            'duration': 75, 'condition': 'Sunny', 'temp_c': 8.9,
            'dest_name': 'Lijnden', 'dest_country': 'Netherlands'}
