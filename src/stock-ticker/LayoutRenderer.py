from getPrice import getprice
from rgbmatrix import graphics
from PIL import ImageFont
from time import strftime


class LayoutRenderer:
    def __init__(self,matrix):
        self.matrix = matrix
        self.font = ImageFont.truetype("DejaVuSansMono.ttf", 10)
        self.btc_price = None
        self.btc_change_24h = None
        self.last_price_update = None

    def updateBTCPrice(self):
        # Fetch latest BTC price and 24h change
        price_data = getprice('bitcoin','usd')
        self.btc_price = str(price_data['price'])
        self.btc_change_24h = price_data['change_24h']
        self.last_price_update = strftime("%M")

    def renderBTCPrice(self):
        current_time = strftime("%I:%M:%S")
        self.matrix.clear()
        self.matrix.draw_text(
            (1,1),
            "BTC Price",
            self.font,
            fill = (225,225,225),
            backgroundColor = (0,0,0)
        )

        if self.btc_price:
            self.matrix.draw_text(
                (1,12),
                "$" + self.btc_price,
                ImageFont.truetype("DejaVuSansMono.ttf", 14),
                fill = (225,225,225),
                backgroundColor = (0,0,0)
            )

            # Display 24h change with color based on positive/negative
            if self.btc_change_24h is not None:
                change_text = f"{self.btc_change_24h:+.2f}%"
                color = (0, 255, 0) if self.btc_change_24h >= 0 else (255, 0, 0)
                self.matrix.draw_text(
                    (1, 23),
                    change_text,
                    self.font,
                    fill = color,
                    backgroundColor = (0,0,0)
                )

        # self.matrix.draw_text(
        #     (1,23),
        #     current_time,
        #     self.font,
        #     fill = (225,225,225),
        #     backgroundColor = (0,0,0)
        # )

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
