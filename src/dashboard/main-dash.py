import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from matrix import Matrix
from utils import args, led_matrix_options
from brightness_control import control_brightness
from temp_display import display_temp
from PIL import ImageFont
from layout_renderer import layout_renderer

def __init__(self):
        self.renderer = layout_renderer()
        
def run(self):
    # Get supplied command line arguments
    commandArgs = args()
    # Check for led configuration arguments
    matrixOptions = led_matrix_options(commandArgs)
    matrixOptions.drop_privileges = False

    # # Set up the options for the matrix
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.pwm_bits = 11
    options.brightness = 60
    options.pwm_lsb_nanoseconds = 130
    options.led_rgb_sequence = "RGB"
    # options.hardware_mapping = "adafruit-hat"

    # Create the matrix object with the options
    matrix = Matrix(RGBMatrix(options = matrixOptions))

    # Set the temperature update interval to 5 minutes (in seconds)
    temp_update_interval = 5 * 60

    while True:
        self.renderer.render_clock()

        time.sleep(30)

        self.renderer.render_temp()
        # # Clear the matrix
        # matrix.clear()

        # # Draw the time on the matrix
        # matrix.draw_text((0,0), time.strftime("%I:%M:%S"), ImageFont.truetype("DejaVuSansMono.ttf", 10), fill=(255,255,255), backgroundColor = (0,0,0))

        # # # Call the control_brightness function to adjust the brightness if necessary
        # # control_brightness(matrix)

        # matrix.render()
        
        # # Call the display_temp function to display the current temperature on the matrix
        # display_temp(matrix, temp_update_interval)

            

if __name__ == "__main__":
    run()