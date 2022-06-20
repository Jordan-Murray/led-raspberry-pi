from LayoutRenderer import LayoutRenderer
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from matrix import Matrix
from utils import args, led_matrix_options
from time import strftime

def run():
    # Get supplied command line arguments
    commandArgs = args()
    # Check for led configuration arguments
    matrixOptions = led_matrix_options(commandArgs)
    matrixOptions.drop_privileges = False

    # Initialize the matrix
    matrix = Matrix(RGBMatrix(options = matrixOptions))

    renderer = LayoutRenderer(matrix)
    while True:
        renderer.renderClock()
        
        #doesnt clear after swtiching, can use matrix.Clear() but will clear after every frame because inside true
        # minuite = strftime("%M")
        # if(int(minuite) % 5 == 0):
        #     renderer.renderBTCPrice()
        # else:
        # renderer.renderClock()

if __name__ == "__main__":
    run()
