from rgbmatrix import graphics
from PIL import ImageFont
from time import strftime
from datetime import datetime, timedelta
from temp_display import get_current_temp_in_celsius


class layout_renderer:
    def __init__(self,matrix):
        self.matrix = matrix
        self.font = ImageFont.truetype("DejaVuSansMono.ttf", 10)

    def render_clock(self, duration):
        stop_time = self.stop_time(duration)
        while strftime("%I:%M:%S") != stop_time:
            self.matrix.clear()
            self.matrix.draw_text(
                (8,8),
                strftime("%I:%M:%S"),
                ImageFont.truetype("DejaVuSansMono.ttf", 10),
                fill = (225,225,225),
                backgroundColor = (0,0,0)
            )
            self.matrix.render()

    def render_temp(self, duration):
        temp = get_current_temp_in_celsius()
        stop_time = self.stop_time(duration)
        while strftime("%I:%M:%S") != stop_time:
            self.matrix.clear()
            self.matrix.draw_text(
                (8,8),
                temp + "°C",
                ImageFont.truetype("DejaVuSansMono.ttf", 10),
                fill = (225,225,225),
                backgroundColor = (0,0,0)
            )
            self.matrix.render()

    def stop_time(self, duration):
        time_str = strftime("%I:%M:%S")
        time = datetime.strptime(time_str, "%I:%M:%S")
        time += timedelta(seconds=duration)
        new_time_str = time.strftime("%I:%M:%S")
        return new_time_str
