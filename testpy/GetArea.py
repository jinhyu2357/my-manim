from manim import *

class GetAreaExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()
        curve = ax.plot(lambda x: 2 * np.sin(x), color=DARK_BLUE)
        area = ax.get_area(
            curve,
            x_range=(PI / 2, 3 * PI / 2),
            color=(GREEN_B, GREEN_D),
            opacity=1,
        )

        self.add(ax, curve, area)