from getPrice import getprice
from rgbmatrix import graphics
from PIL import ImageFont
from utils import get_file
from time import gmtime, strftime


class PriceRenderer:
    def __init__(self,data,matrix):
        self.matrix = matrix
        self.font = ImageFont.truetype("DejaVuSansMono.ttf", 10)
        self.btcPrice = str(getprice('bitcoin','usd')) 
        #ImageFont.truetype("04b.ttf", 8)

    def render(self):

        self.matrix.draw_text(
            (1,1),
            "BTC Price:",
            self.font,
            fill = (225,225,225),
            backgroundColor = (0,0,0)
        )

        self.matrix.draw_text(
            (1,12),
            "$" + self.btcPrice,
            self.font,
            fill = (225,225,225),
            backgroundColor = (0,0,0)
        )

        self.matrix.draw_text(
            1,23,
            strftime("%H:%M:%S", gmtime()),
            self.font,
            fill = (225,225,225),
            backgroundColor = (0,0,0)

        )
        self.matrix.render()

    ##ToDo:
    ## Use DrawTextLayout and create layouts to draw multiple lines of text
