import time
import requests

def display_temp(matrix, temp_update_interval):
    # Get the current time
    start_time = time.time()

    while True:
        # Check if it's time to update the temperature
        elapsed_time = time.time() - start_time
        if elapsed_time % temp_update_interval == 0:
            # Get the current temperature in Celsius
            # You can use a library or API call to get the temperature here
            current_temp = get_current_temp_in_celsius()

            # Clear the matrix
            matrix.Clear()

            # Draw the temperature on the matrix
            matrix.DrawText(str(current_temp) + "°C", x=0, y=0, font=matrix.Font6x10, color=(255,255,255))

            # Sleep for 1 second
            time.sleep(1)

def get_current_temp_in_celsius():
    # Set the API endpoint URL and your API key
    api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
    api_key = "d99a3d3074d10c2908bae2c54b3e1f0d"
    
    # Set the location parameters
    params = {
        "lat": "53.2295",
        "appid": api_key,
        "lon": "0.5427"
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
