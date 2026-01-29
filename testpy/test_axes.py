from manim import *

class AxesWithDifferentTips(Scene):
    def construct(self):
        ax = Axes(axis_config={'tip_shape': StealthTip})
        self.add(ax)