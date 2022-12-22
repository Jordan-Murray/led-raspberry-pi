import requests

def get_current_temp_in_celsius():
    # Set the API endpoint URL and your API key
    api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
    api_key = "d99a3d3074d10c2908bae2c54b3e1f0d"
    
    # Set the location parameters
    params = {
        "lat": "53.2295",
        "appid": api_key,
        "lon": "0.5427",
        "units":"metric"
    }
    
    # Make the API request
    response = requests.get(api_endpoint, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the current temperature in Celsius
        current_temp = response.json()["main"]["temp"]
        current_temp = round(current_temp)
        return current_temp
    else:
        return None
