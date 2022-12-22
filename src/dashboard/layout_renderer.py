from rgbmatrix import graphics
from PIL import ImageFont
from time import strftime


class layout_renderer:
    def __init__(self,matrix):
        self.matrix = matrix
        self.font = ImageFont.truetype("DejaVuSansMono.ttf", 10)
        # self.btcPrice = str(getprice('bitcoin','usd')) 
        #ImageFont.truetype("04b.ttf", 8)

    def renderBTCPrice(self):
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
            "$1000",
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

    def render_clock(self):
        self.matrix.clear()
        self.matrix.draw_text(
            (8,8),
            strftime("%I:%M:%S"),
            ImageFont.truetype("DejaVuSansMono.ttf", 10),
            fill = (225,225,225),
            backgroundColor = (0,0,0)
        )
        self.matrix.render()

    def render_temp(self):
        self.matrix.clear()
        self.matrix.draw_text(
            (8,8),
            "5 degrees",
            ImageFont.truetype("DejaVuSansMono.ttf", 10),
            fill = (225,225,225),
            backgroundColor = (0,0,0)
        )
        self.matrix.render()


    ##ToDo:
    ## Use DrawTextLayout and create layouts to draw multiple lines of text
