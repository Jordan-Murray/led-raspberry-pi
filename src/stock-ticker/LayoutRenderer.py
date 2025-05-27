from getPrice import getprice
from rgbmatrix import graphics
from PIL import ImageFont
from time import strftime


class LayoutRenderer:
    def __init__(self,matrix):
        self.matrix = matrix
        self.font = ImageFont.truetype("DejaVuSansMono.ttf", 10)

    def renderBTCPrice(self):
        # Fetch latest BTC price
        btcPrice = str(getprice('bitcoin','usd'))
        
        self.matrix.clear()
        self.matrix.draw_text(
            (1,1),
            "BTC Price",
            self.font,
            fill = (225,225,225),
            backgroundColor = (0,0,0)
        )

        self.matrix.draw_text(
            (1,12),
            "$" + btcPrice,
            self.font,
            fill = (225,225,225),
            backgroundColor = (0,0,0)
        )

        self.matrix.draw_text(
            (1,23),
            strftime("%I:%M:%S"),
            self.font,
            fill = (225,225,225),
            backgroundColor = (0,0,0)
        )

        self.matrix.render()

    def renderClock(self):
        self.matrix.clear()
        self.matrix.draw_text(
            (2,8),
            strftime("%I:%M:%S"),
            ImageFont.truetype("DejaVuSansMono.ttf", 20),
            fill = (225,225,225),
            backgroundColor = (0,0,0)
        )
        self.matrix.render()

    ##ToDo:
    ## Use DrawTextLayout and create layouts to draw multiple lines of text
