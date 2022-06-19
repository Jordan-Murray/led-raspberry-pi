from PriceRenderer import PriceRenderer
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
    # font = graphics.Font()
    # font.LoadFont("../../fonts/7x13.bdf")

    data = Data()
    # data.font = font
    # data.textColor = graphics.Color(255, 255, 255)
    price = PriceRenderer(data,matrix)
    while True:
        price.render()

if __name__ == "__main__":
    run()
