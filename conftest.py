""" Contains Fixtures for the Tests. """

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

@pytest.fixture()
def test_weather_data():
    """ Returns 1 instance of weather data. """
    return {'location': {'name': 'Kloten', 'region': '', 'country': 'Switzerland', 'lat': 47.45, 'lon': 8.583, 'tz_id': 'Europe/Zurich', 'localtime_epoch': 1740496677, 'localtime': '2025-02-25 16:17'}, 'current': {'last_updated_epoch': 1740496500, 'last_updated': '2025-02-25 16:15', 'temp_c': 9.3, 'temp_f': 48.7, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 4.9, 'wind_kph': 7.9, 'wind_degree': 242, 'wind_dir': 'WSW', 'pressure_mb': 1014.0, 'pressure_in': 29.94, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 87, 'cloud': 75, 'feelslike_c': 8.2, 'feelslike_f': 46.8, 'windchill_c': 7.7, 'windchill_f': 45.8, 'heatindex_c': 8.9, 'heatindex_f': 47.9, 'dewpoint_c': 5.2, 'dewpoint_f': 41.3, 'vis_km': 10.0, 'vis_miles': 6.0, 'uv': 0.3, 'gust_mph': 6.3, 'gust_kph': 10.2, 'air_quality': {'co': 534.65, 'no2': 70.115, 'o3': 24.0, 'so2': 3.33, 'pm2_5': 28.12, 'pm10': 34.595, 'us-epa-index': 2, 'gb-defra-index': 3}}, 'forecast': {'forecastday': [{'date': '2025-02-25', 'date_epoch': 1740441600, 'day': {'maxtemp_c': 10.7, 'maxtemp_f': 51.2, 'mintemp_c': 5.2, 'mintemp_f': 41.3, 'avgtemp_c': 7.3, 'avgtemp_f': 45.1, 'maxwind_mph': 14.5, 'maxwind_kph': 23.4, 'totalprecip_mm': 0.78, 'totalprecip_in': 0.03, 'totalsnow_cm': 0.0, 'avgvis_km': 9.0, 'avgvis_miles': 5.0, 'avghumidity': 79, 'daily_will_it_rain': 1, 'daily_chance_of_rain': 85, 'daily_will_it_snow': 0, 'daily_chance_of_snow': 0, 'condition': {'text': 'Patchy rain nearby', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'uv': 0.3}, 'astro': {'sunrise': '07:14 AM', 'sunset': '06:05 PM', 'moonrise': '06:17 AM', 'moonset': '02:43 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 12, 'is_moon_up': 0, 'is_sun_up': 0}, 'hour': [{'time_epoch': 1740438000, 'time': '2025-02-25 00:00', 'temp_c': 6.2, 'temp_f': 43.1, 'is_day': 0, 'condition': {'text': 'Partly Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 2.0, 'wind_kph': 3.2, 'wind_degree': 256, 'wind_dir': 'WSW', 'pressure_mb': 1021.0, 'pressure_in': 30.16, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 83, 'cloud': 26, 'feelslike_c': 6.2, 'feelslike_f': 43.1, 'windchill_c': 6.2, 'windchill_f': 43.1, 'heatindex_c': 6.2, 'heatindex_f': 43.1, 'dewpoint_c': 3.5, 'dewpoint_f': 38.4, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 4.2, 'gust_kph': 6.7, 'uv': 0}, {'time_epoch': 1740441600, 'time': '2025-02-25 01:00', 'temp_c': 5.8, 'temp_f': 42.5, 'is_day': 0, 'condition': {'text': 'Partly Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 1.3, 'wind_kph': 2.2, 'wind_degree': 238, 'wind_dir': 'WSW', 'pressure_mb': 1021.0, 'pressure_in': 30.15, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 85, 'cloud': 30, 'feelslike_c': 5.8, 'feelslike_f': 42.5, 'windchill_c': 5.8, 'windchill_f': 42.5, 'heatindex_c': 5.8, 'heatindex_f': 42.5, 'dewpoint_c': 3.6, 'dewpoint_f': 38.4, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 2.7, 'gust_kph': 4.4, 'uv': 0}, {'time_epoch': 1740445200, 'time': '2025-02-25 02:00', 'temp_c': 6.3, 'temp_f': 43.3, 'is_day': 0, 'condition': {'text': 'Partly Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 1.8, 'wind_kph': 2.9, 'wind_degree': 161, 'wind_dir': 'SSE', 'pressure_mb': 1020.0, 'pressure_in': 30.13, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 84, 'cloud': 47, 'feelslike_c': 6.3, 'feelslike_f': 43.3, 'windchill_c': 6.3, 'windchill_f': 43.3, 'heatindex_c': 6.3, 'heatindex_f': 43.3, 'dewpoint_c': 3.7, 'dewpoint_f': 38.7, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 3.4, 'gust_kph': 5.4, 'uv': 0}, {'time_epoch': 1740448800, 'time': '2025-02-25 03:00', 'temp_c': 5.6, 'temp_f': 42.0, 'is_day': 0, 'condition': {'text': 'Partly Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 0.9, 'wind_kph': 1.4, 'wind_degree': 189, 'wind_dir': 'S', 'pressure_mb': 1020.0, 'pressure_in': 30.11, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 86, 'cloud': 49, 'feelslike_c': 5.6, 'feelslike_f': 42.0, 'windchill_c': 5.6, 'windchill_f': 42.0, 'heatindex_c': 5.6, 'heatindex_f': 42.0, 'dewpoint_c': 3.5, 'dewpoint_f': 38.2, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 1.8, 'gust_kph': 2.9, 'uv': 0}, {'time_epoch': 1740452400, 'time': '2025-02-25 04:00', 'temp_c': 5.2, 'temp_f': 41.4, 'is_day': 0, 'condition': {'text': 'Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/night/119.png', 'code': 1006}, 'wind_mph': 0.9, 'wind_kph': 1.4, 'wind_degree': 110, 'wind_dir': 'ESE', 'pressure_mb': 1020.0, 'pressure_in': 30.11, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 87, 'cloud': 65, 'feelslike_c': 5.2, 'feelslike_f': 41.4, 'windchill_c': 5.2, 'windchill_f': 41.4, 'heatindex_c': 5.2, 'heatindex_f': 41.4, 'dewpoint_c': 3.2, 'dewpoint_f': 37.8, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 1.9, 'gust_kph': 3.0, 'uv': 0}, {'time_epoch': 1740456000, 'time': '2025-02-25 05:00', 'temp_c': 5.2, 'temp_f': 41.4, 'is_day': 0, 'condition': {'text': 'Partly Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 2.2, 'wind_kph': 3.6, 'wind_degree': 151, 'wind_dir': 'SSE', 'pressure_mb': 1020.0, 'pressure_in': 30.11, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 87, 'cloud': 62, 'feelslike_c': 5.0, 'feelslike_f': 40.9, 'windchill_c': 5.0, 'windchill_f': 40.9, 'heatindex_c': 5.2, 'heatindex_f': 41.4, 'dewpoint_c': 3.2, 'dewpoint_f': 37.7, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 4.6, 'gust_kph': 7.3, 'uv': 0}, {'time_epoch': 1740459600, 'time': '2025-02-25 06:00', 'temp_c': 5.3, 'temp_f': 41.6, 'is_day': 0, 'condition': {'text': 'Partly Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 2.9, 'wind_kph': 4.7, 'wind_degree': 141, 'wind_dir': 'SE', 'pressure_mb': 1019.0, 'pressure_in': 30.09, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 85, 'cloud': 58, 'feelslike_c': 4.6, 'feelslike_f': 40.2, 'windchill_c': 4.6, 'windchill_f': 40.2, 'heatindex_c': 5.3, 'heatindex_f': 41.6, 'dewpoint_c': 3.0, 'dewpoint_f': 37.4, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 5.8, 'gust_kph': 9.4, 'uv': 0}, {'time_epoch': 1740463200, 'time': '2025-02-25 07:00', 'temp_c': 5.2, 'temp_f': 41.3, 'is_day': 0, 'condition': {'text': 'Partly Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/night/116.png', 'code': 1003}, 'wind_mph': 2.9, 'wind_kph': 4.7, 'wind_degree': 103, 'wind_dir': 'ESE', 'pressure_mb': 1018.0, 'pressure_in': 30.06, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 84, 'cloud': 56, 'feelslike_c': 4.4, 'feelslike_f': 40.0, 'windchill_c': 4.4, 'windchill_f': 40.0, 'heatindex_c': 5.2, 'heatindex_f': 41.3, 'dewpoint_c': 2.8, 'dewpoint_f': 37.0, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 5.8, 'gust_kph': 9.4, 'uv': 0}, {'time_epoch': 1740466800, 'time': '2025-02-25 08:00', 'temp_c': 5.8, 'temp_f': 42.5, 'is_day': 1, 'condition': {'text': 'Partly Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 2.5, 'wind_kph': 4.0, 'wind_degree': 72, 'wind_dir': 'ENE', 'pressure_mb': 1017.0, 'pressure_in': 30.03, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 84, 'cloud': 46, 'feelslike_c': 5.4, 'feelslike_f': 41.8, 'windchill_c': 5.4, 'windchill_f': 41.8, 'heatindex_c': 5.8, 'heatindex_f': 42.5, 'dewpoint_c': 3.3, 'dewpoint_f': 37.9, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 4.4, 'gust_kph': 7.1, 'uv': 0.1}, {'time_epoch': 1740470400, 'time': '2025-02-25 09:00', 'temp_c': 7.0, 'temp_f': 44.7, 'is_day': 1, 'condition': {'text': 'Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/day/119.png', 'code': 1006}, 'wind_mph': 2.2, 'wind_kph': 3.6, 'wind_degree': 50, 'wind_dir': 'NE', 'pressure_mb': 1016.0, 'pressure_in': 30.0, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 80, 'cloud': 67, 'feelslike_c': 7.0, 'feelslike_f': 44.5, 'windchill_c': 7.0, 'windchill_f': 44.5, 'heatindex_c': 7.0, 'heatindex_f': 44.7, 'dewpoint_c': 3.8, 'dewpoint_f': 38.8, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 3.2, 'gust_kph': 5.2, 'uv': 0.5}, {'time_epoch': 1740474000, 'time': '2025-02-25 10:00', 'temp_c': 8.3, 'temp_f': 46.9, 'is_day': 1, 'condition': {'text': 'Partly Cloudy ', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 2.7, 'wind_kph': 4.3, 'wind_degree': 34, 'wind_dir': 'NE', 'pressure_mb': 1015.0, 'pressure_in': 29.96, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 75, 'cloud': 55, 'feelslike_c': 8.0, 'feelslike_f': 46.5, 'windchill_c': 8.0, 'windchill_f': 46.5, 'heatindex_c': 8.3, 'heatindex_f': 46.9, 'dewpoint_c': 4.1, 'dewpoint_f': 39.5, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 3.3, 'gust_kph': 5.3, 'uv': 1.0}, {'time_epoch': 1740477600, 'time': '2025-02-25 11:00', 'temp_c': 9.4, 'temp_f': 48.9, 'is_day': 1, 'condition': {'text': 'Overcast ', 'icon': '//cdn.weatherapi.com/weather/64x64/day/122.png', 'code': 1009}, 'wind_mph': 1.6, 'wind_kph': 2.5, 'wind_degree': 349, 'wind_dir': 'N', 'pressure_mb': 1014.0, 'pressure_in': 29.95, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 71, 'cloud': 100, 'feelslike_c': 9.4, 'feelslike_f': 48.9, 'windchill_c': 9.4, 'windchill_f': 48.9, 'heatindex_c': 9.4, 'heatindex_f': 48.9, 'dewpoint_c': 4.5, 'dewpoint_f': 40.1, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 1.8, 'gust_kph': 2.9, 'uv': 1.3}, {'time_epoch': 1740481200, 'time': '2025-02-25 12:00', 'temp_c': 9.6, 'temp_f': 49.4, 'is_day': 1, 'condition': {'text': 'Overcast ', 'icon': '//cdn.weatherapi.com/weather/64x64/day/122.png', 'code': 1009}, 'wind_mph': 3.6, 'wind_kph': 5.8, 'wind_degree': 258, 'wind_dir': 'WSW', 'pressure_mb': 1015.0, 'pressure_in': 29.96, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 70, 'cloud': 100, 'feelslike_c': 9.1, 'feelslike_f': 48.4, 'windchill_c': 9.1, 'windchill_f': 48.4, 'heatindex_c': 9.7, 'heatindex_f': 49.4, 'dewpoint_c': 4.5, 'dewpoint_f': 40.1, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 4.2, 'gust_kph': 6.7, 'uv': 1.4}, {'time_epoch': 1740484800, 'time': '2025-02-25 13:00', 'temp_c': 9.9, 'temp_f': 49.9, 'is_day': 1, 'condition': {'text': 'Overcast ', 'icon': '//cdn.weatherapi.com/weather/64x64/day/122.png', 'code': 1009}, 'wind_mph': 4.9, 'wind_kph': 7.9, 'wind_degree': 252, 'wind_dir': 'WSW', 'pressure_mb': 1014.0, 'pressure_in': 29.96, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 67, 'cloud': 100, 'feelslike_c': 9.0, 'feelslike_f': 48.1, 'windchill_c': 9.0, 'windchill_f': 48.1, 'heatindex_c': 9.9, 'heatindex_f': 49.9, 'dewpoint_c': 4.0, 'dewpoint_f': 39.2, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 5.7, 'gust_kph': 9.2, 'uv': 1.0}, {'time_epoch': 1740488400, 'time': '2025-02-25 14:00', 'temp_c': 10.7, 'temp_f': 51.2, 'is_day': 1, 'condition': {'text': 'Patchy rain nearby', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 5.4, 'wind_kph': 8.6, 'wind_degree': 246, 'wind_dir': 'WSW', 'pressure_mb': 1014.0, 'pressure_in': 29.93, 'precip_mm': 0.02, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 64, 'cloud': 100, 'feelslike_c': 9.7, 'feelslike_f': 49.4, 'windchill_c': 9.7, 'windchill_f': 49.4, 'heatindex_c': 10.7, 'heatindex_f': 51.2, 'dewpoint_c': 4.2, 'dewpoint_f': 39.6, 'will_it_rain': 1, 'chance_of_rain': 85, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 6.2, 'gust_kph': 9.9, 'uv': 1.0}, {'time_epoch': 1740492000, 'time': '2025-02-25 15:00', 'temp_c': 9.6, 'temp_f': 49.4, 'is_day': 1, 'condition': {'text': 'Light drizzle', 'icon': '//cdn.weatherapi.com/weather/64x64/day/266.png', 'code': 1153}, 'wind_mph': 7.2, 'wind_kph': 11.5, 'wind_degree': 269, 'wind_dir': 'W', 'pressure_mb': 1014.0, 'pressure_in': 29.94, 'precip_mm': 0.16, 'precip_in': 0.01, 'snow_cm': 0.0, 'humidity': 75, 'cloud': 100, 'feelslike_c': 8.0, 'feelslike_f': 46.3, 'windchill_c': 8.0, 'windchill_f': 46.3, 'heatindex_c': 9.7, 'heatindex_f': 49.4, 'dewpoint_c': 5.4, 'dewpoint_f': 41.6, 'will_it_rain': 1, 'chance_of_rain': 100, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 2.0, 'vis_miles': 1.0, 'gust_mph': 8.5, 'gust_kph': 13.7, 'uv': 0.5}, {'time_epoch': 1740495600, 'time': '2025-02-25 16:00', 'temp_c': 9.3, 'temp_f': 48.7, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 4.9, 'wind_kph': 7.9, 'wind_degree': 242, 'wind_dir': 'WSW', 'pressure_mb': 1014.0, 'pressure_in': 29.94, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 87, 'cloud': 75, 'feelslike_c': 7.7, 'feelslike_f': 45.8, 'windchill_c': 7.7, 'windchill_f': 45.8, 'heatindex_c': 8.9, 'heatindex_f': 47.9, 'dewpoint_c': 5.2, 'dewpoint_f': 41.3, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 6.3, 'gust_kph': 10.2, 'uv': 0.3}, {'time_epoch': 1740499200, 'time': '2025-02-25 17:00', 'temp_c': 8.4, 'temp_f': 47.1, 'is_day': 1, 'condition': {'text': 'Patchy rain nearby', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 2.5, 'wind_kph': 4.0, 'wind_degree': 157, 'wind_dir': 'SSE', 'pressure_mb': 1013.0, 'pressure_in': 29.91, 'precip_mm': 0.05, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 78, 'cloud': 76, 'feelslike_c': 8.3, 'feelslike_f': 47.0, 'windchill_c': 8.3, 'windchill_f': 47.0, 'heatindex_c': 8.4, 'heatindex_f': 47.1, 'dewpoint_c': 4.9, 'dewpoint_f': 40.7, 'will_it_rain': 1, 'chance_of_rain': 100, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 3.4, 'gust_kph': 5.5, 'uv': 0.1}, {'time_epoch': 1740502800, 'time': '2025-02-25 18:00', 'temp_c': 7.6, 'temp_f': 45.7, 'is_day': 1, 'condition': {'text': 'Light drizzle', 'icon': '//cdn.weatherapi.com/weather/64x64/day/266.png', 'code': 1153}, 'wind_mph': 3.1, 'wind_kph': 5.0, 'wind_degree': 169, 'wind_dir': 'S', 'pressure_mb': 1013.0, 'pressure_in': 29.92, 'precip_mm': 0.23, 'precip_in': 0.01, 'snow_cm': 0.0, 'humidity': 82, 'cloud': 100, 'feelslike_c': 7.0, 'feelslike_f': 44.6, 'windchill_c': 7.0, 'windchill_f': 44.6, 'heatindex_c': 7.6, 'heatindex_f': 45.7, 'dewpoint_c': 4.7, 'dewpoint_f': 40.5, 'will_it_rain': 1, 'chance_of_rain': 100, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 2.0, 'vis_miles': 1.0, 'gust_mph': 5.0, 'gust_kph': 8.0, 'uv': 0.0}, {'time_epoch': 1740506400, 'time': '2025-02-25 19:00', 'temp_c': 7.2, 'temp_f': 44.9, 'is_day': 0, 'condition': {'text': 'Light drizzle', 'icon': '//cdn.weatherapi.com/weather/64x64/night/266.png', 'code': 1153}, 'wind_mph': 4.0, 'wind_kph': 6.5, 'wind_degree': 148, 'wind_dir': 'SSE', 'pressure_mb': 1013.0, 'pressure_in': 29.92, 'precip_mm': 0.16, 'precip_in': 0.01, 'snow_cm': 0.0, 'humidity': 86, 'cloud': 100, 'feelslike_c': 6.1, 'feelslike_f': 43.0, 'windchill_c': 6.1, 'windchill_f': 43.0, 'heatindex_c': 7.2, 'heatindex_f': 44.9, 'dewpoint_c': 5.1, 'dewpoint_f': 41.1, 'will_it_rain': 1, 'chance_of_rain': 100, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 2.0, 'vis_miles': 1.0, 'gust_mph': 6.4, 'gust_kph': 10.3, 'uv': 0}, {'time_epoch': 1740510000, 'time': '2025-02-25 20:00', 'temp_c': 7.2, 'temp_f': 45.0, 'is_day': 0, 'condition': {'text': 'Patchy rain nearby', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 4.3, 'wind_kph': 6.8, 'wind_degree': 222, 'wind_dir': 'SW', 'pressure_mb': 1014.0, 'pressure_in': 29.95, 'precip_mm': 0.11, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 87, 'cloud': 100, 'feelslike_c': 6.0, 'feelslike_f': 42.9, 'windchill_c': 6.0, 'windchill_f': 42.9, 'heatindex_c': 7.2, 'heatindex_f': 45.0, 'dewpoint_c': 5.3, 'dewpoint_f': 41.5, 'will_it_rain': 1, 'chance_of_rain': 100, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 6.5, 'gust_kph': 10.5, 'uv': 0}, {'time_epoch': 1740513600, 'time': '2025-02-25 21:00', 'temp_c': 7.9, 'temp_f': 46.2, 'is_day': 0, 'condition': {'text': 'Patchy rain nearby', 'icon': '//cdn.weatherapi.com/weather/64x64/night/176.png', 'code': 1063}, 'wind_mph': 14.5, 'wind_kph': 23.4, 'wind_degree': 230, 'wind_dir': 'SW', 'pressure_mb': 1014.0, 'pressure_in': 29.95, 'precip_mm': 0.04, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 68, 'cloud': 100, 'feelslike_c': 4.4, 'feelslike_f': 39.8, 'windchill_c': 4.4, 'windchill_f': 39.8, 'heatindex_c': 7.9, 'heatindex_f': 46.2, 'dewpoint_c': 2.4, 'dewpoint_f': 36.4, 'will_it_rain': 1, 'chance_of_rain': 80, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 20.8, 'gust_kph': 33.4, 'uv': 0}, {'time_epoch': 1740517200, 'time': '2025-02-25 22:00', 'temp_c': 6.4, 'temp_f': 43.6, 'is_day': 0, 'condition': {'text': 'Overcast ', 'icon': '//cdn.weatherapi.com/weather/64x64/night/122.png', 'code': 1009}, 'wind_mph': 11.2, 'wind_kph': 18.0, 'wind_degree': 234, 'wind_dir': 'SW', 'pressure_mb': 1015.0, 'pressure_in': 29.98, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 74, 'cloud': 100, 'feelslike_c': 3.1, 'feelslike_f': 37.6, 'windchill_c': 3.1, 'windchill_f': 37.6, 'heatindex_c': 6.4, 'heatindex_f': 43.6, 'dewpoint_c': 2.1, 'dewpoint_f': 35.8, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 16.1, 'gust_kph': 26.0, 'uv': 0}, {'time_epoch': 1740520800, 'time': '2025-02-25 23:00', 'temp_c': 5.9, 'temp_f': 42.7, 'is_day': 0, 'condition': {'text': 'Overcast ', 'icon': '//cdn.weatherapi.com/weather/64x64/night/122.png', 'code': 1009}, 'wind_mph': 12.5, 'wind_kph': 20.2, 'wind_degree': 232, 'wind_dir': 'SW', 'pressure_mb': 1016.0, 'pressure_in': 30.0, 'precip_mm': 0.0, 'precip_in': 0.0, 'snow_cm': 0.0, 'humidity': 76, 'cloud': 100, 'feelslike_c': 2.2, 'feelslike_f': 36.0, 'windchill_c': 2.2, 'windchill_f': 36.0, 'heatindex_c': 5.9, 'heatindex_f': 42.7, 'dewpoint_c': 2.1, 'dewpoint_f': 35.8, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 17.8, 'gust_kph': 28.7, 'uv': 0}]}]}}

@pytest.fixture()
def test_flight_data():
    """ Returns unclean flight data for the add_weather_to_flights function. """
    return {'airline_iata': 'LX', 'airline_icao': 'SWR', 'flight_iata': 'LX457', 'flight_icao': 'SWR457', 'flight_number': '457', 'dep_iata': 'LCY', 'dep_icao': 'EGLC', 'dep_terminal': None, 'dep_gate': None, 'dep_time': '2025-02-25 13:30', 'dep_time_utc': '2025-02-25 13:30', 'dep_estimated': '2025-02-25 13:26', 'dep_estimated_utc': '2025-02-25 13:26', 'dep_actual': '2025-02-25 13:26', 'dep_actual_utc': '2025-02-25 13:26', 'arr_iata': 'ZRH', 'arr_icao': 'LSZH', 'arr_terminal': '2', 'arr_gate': None, 'arr_baggage': '22', 'arr_time': '2025-02-25 16:05', 'arr_time_utc': '2025-02-25 15:05', 'arr_estimated': '2025-02-25 15:54', 'arr_estimated_utc': '2025-02-25 14:54', 'arr_actual': '2025-02-25 15:54', 'arr_actual_utc': '2025-02-25 14:54', 'cs_airline_iata': None, 'cs_flight_number': None, 'cs_flight_iata': None, 'status': 'landed', 'duration': 95, 'delayed': None, 'dep_delayed': None, 'arr_delayed': None, 'aircraft_icao': None, 'arr_time_ts': 1740495900, 'dep_time_ts': 1740490200, 'arr_estimated_ts': 1740495240, 'dep_estimated_ts': 1740489960, 'arr_actual_ts': 1740495240, 'dep_actual_ts': 1740489960}

@pytest.fixture()
def test_flight_weather_data():
    """ Returns combined weather and flight data for the add_weather_to_flights function. """
    return {'airline_iata': 'LX', 'airline_icao': 'SWR', 'flight_iata': 'LX457', 'flight_icao': 'SWR457', 'flight_number': '457', 'dep_iata': 'LCY', 'dep_icao': 'EGLC', 'dep_terminal': None, 'dep_gate': None, 'dep_time': '2025-02-25 13:30', 'dep_time_utc': '2025-02-25 13:30', 'dep_estimated': '2025-02-25 13:26', 'dep_estimated_utc': '2025-02-25 13:26', 'dep_actual': '2025-02-25 13:26', 'dep_actual_utc': '2025-02-25 13:26', 'arr_iata': 'ZRH', 'arr_icao': 'LSZH', 'arr_terminal': '2', 'arr_gate': None, 'arr_baggage': '22', 'arr_time': '2025-02-25 16:05', 'arr_time_utc': '2025-02-25 15:05', 'arr_estimated': '2025-02-25 15:54', 'arr_estimated_utc': '2025-02-25 14:54', 'arr_actual': '2025-02-25 15:54', 'arr_actual_utc': '2025-02-25 14:54', 'cs_airline_iata': None, 'cs_flight_number': None, 'cs_flight_iata': None, 'status': 'landed', 'duration': 95, 'delayed': None, 'dep_delayed': None, 'arr_delayed': None, 'aircraft_icao': None, 'arr_time_ts': 1740495900, 'dep_time_ts': 1740490200, 'arr_estimated_ts': 1740495240, 'dep_estimated_ts': 1740489960, 'arr_actual_ts': 1740495240, 'dep_actual_ts': 1740489960, 'time_epoch': 1740492000, 'time': '2025-02-25 15:00', 'temp_c': 9.6, 'temp_f': 49.4, 'is_day': 1, 'condition': {'text': 'Light drizzle', 'icon': '//cdn.weatherapi.com/weather/64x64/day/266.png', 'code': 1153}, 'wind_mph': 7.2, 'wind_kph': 11.5, 'wind_degree': 269, 'wind_dir': 'W', 'pressure_mb': 1014.0, 'pressure_in': 29.94, 'precip_mm': 0.16, 'precip_in': 0.01, 'snow_cm': 0.0, 'humidity': 75, 'cloud': 100, 'feelslike_c': 8.0, 'feelslike_f': 46.3, 'windchill_c': 8.0, 'windchill_f': 46.3, 'heatindex_c': 9.7, 'heatindex_f': 49.4, 'dewpoint_c': 5.4, 'dewpoint_f': 41.6, 'will_it_rain': 1, 'chance_of_rain': 100, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 2.0, 'vis_miles': 1.0, 'gust_mph': 8.5, 'gust_kph': 13.7, 'uv': 0.5, 'name': 'Kloten', 'region': '', 'country': 'Switzerland', 'lat': 47.45, 'lon': 8.583, 'tz_id': 'Europe/Zurich', 'localtime_epoch': 1740496677, 'localtime': '2025-02-25 16:17'}
