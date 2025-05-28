from LayoutRenderer import LayoutRenderer
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from matrix import Matrix
from utils import args, led_matrix_options
from time import strftime, sleep

def run():
    # Get supplied command line arguments
    commandArgs = args()
    # Check for led configuration arguments
    matrixOptions = led_matrix_options(commandArgs)
    matrixOptions.drop_privileges = False

    # Initialize the matrix
    matrix = Matrix(RGBMatrix(options = matrixOptions))
    matrix.set_brightness(75)

    renderer = LayoutRenderer(matrix)
    # Initial price fetch
    renderer.updateBTCPrice()
    
    while True:
        current_minute = strftime("%M")
        
        # Update BTC price every 2 minutes
        if int(current_minute) % 2 == 0 and renderer.last_price_update != current_minute:
            renderer.updateBTCPrice()
        
        # Render appropriate display
        if int(current_minute) % 2 == 0:
            renderer.renderBTCPrice()
        else:
            renderer.renderClock()
            
        sleep(1)  # Update display every second

if __name__ == "__main__":
    run()
