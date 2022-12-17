import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import requests

# Set up the options for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.pwm_bits = 11
options.brightness = 100
options.pwm_lsb_nanoseconds = 130
options.led_rgb_sequence = "RGB"

# Create the matrix object with the options
matrix = RGBMatrix(options = options)

# Set the temperature update interval to 5 minutes (in seconds)
temp_update_interval = 300

try:
    while True:
        # Get the current time
        current_time = time.strftime("%I:%M %p")

        # Clear the matrix
        matrix.Clear()

        # Draw the time on the matrix
        matrix.DrawText(current_time, x=0, y=0, font=matrix.Font6x10, color=(255,0,0))

        # Sleep for 1 second
        time.sleep(1)

        # Check if it's time to update the temperature
        elapsed_time = time.time() - start_time
        if elapsed_time % temp_update_interval == 0:
            # Get the current temperature in Celsius
            # You can use a library or API call to get the temperature here
            current_temp = get_current_temp_in_celsius()

            # Clear the matrix
            matrix.Clear()

            # Draw the temperature on the matrix
            matrix.DrawText(str(current_temp) + "°C", x=0, y=0, font=matrix.Font6x10, color=(255,0,0))

            # Sleep for 1 second
            time.sleep(1)

except KeyboardInterrupt:
    matrix.Clear()
    matrix.Terminate()


def get_current_temp_in_celsius():
    # Set the API endpoint URL and your API key
    api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
    api_key = "YOUR_API_KEY_HERE"
    
    # Set the location parameters
    params = {
        "q": "CITY_NAME,COUNTRY_CODE",
        "appid": api_key,
        "units": "metric"
    }
    
    # Make the API request
    response = requests.get(api_endpoint, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the current temperature in Celsius
        current_temp = response.json()["main"]["temp"]
        
        return current_temp
    else:
        return None
