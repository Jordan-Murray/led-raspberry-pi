import time

def control_brightness(matrix):
    # Get the current time
    current_time = time.strftime("%I:%M %p")

    # Check if it's 10pm or 7am
    if current_time == "10:00 PM" or current_time == "07:00 AM":
        # Get the current brightness
        current_brightness = matrix.brightness

        # Check if it's 10pm or 7am
        if current_time == "10:00 PM":
            # Set the brightness to 0 at 10pm
            matrix.brightness = 0
        elif current_time == "07:00 AM":
            # Set the brightness to 60 at 7am
            matrix.brightness = 60

        # Sleep for 1 second
        time.sleep(1)

        # Restore the previous brightness
        matrix.brightness = current_brightness
    else:
        # Sleep for 1 second
        time.sleep(1)