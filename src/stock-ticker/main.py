from LayoutRenderer import LayoutRenderer
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from matrix import Matrix
from data import Data
from utils import args, led_matrix_options

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
        renderer.render()

if __name__ == "__main__":
    run()
