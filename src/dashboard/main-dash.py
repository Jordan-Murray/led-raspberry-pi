from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from matrix import Matrix
from utils import args, led_matrix_options
from render_manager import RenderManager

        
def run():
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
    RenderManager(matrix).render()

if __name__ == "__main__":
    run()
