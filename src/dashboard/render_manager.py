import time
from layout_renderer import layout_renderer


class RenderManager:
    def __init__(self):
        self.renderer = layout_renderer()

    def render(self):
        self.renderer.render_clock()

        time.sleep(30)

        self.renderer.render_temp()