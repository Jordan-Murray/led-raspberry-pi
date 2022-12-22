import time
from layout_renderer import layout_renderer


class RenderManager:
    def __init__(self,matrix):
        self.renderer = layout_renderer(matrix)

    def render(self):
        while True:
            self.renderer.render_clock()

            time.sleep(30)

            self.renderer.render_temp()