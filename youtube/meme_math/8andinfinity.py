from manim import *

config.pixel_width = 1080
config.pixel_height = 1920

class InfinityToEight(Scene):
    def construct(self):
        infty = Tex(r"$\infty$", font_size=200)
        self.play(Write(infty))
        self.wait(1)

        self.play(Rotate(infty, angle=-PI/2))
        self.wait(0.5)

        eight = Tex(r"$8$", font_size=200)
        self.play(Transform(infty, eight))
        self.wait(2)

        eq = MathTex(r"\infty \times\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = 8").scale(1.2)
        eq.to_edge(DOWN)
        self.play(Write(eq))
        self.wait(2)
