from manim import *

class WallisProduct(Scene):
    def construct(self):
        title = Text("Wallis Product", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        eq1 = MathTex(
            r"\frac{\sin x}{x} = 1 - \frac{x^2}{3} + \frac{x^4}{5} - \frac{x^6}{7} + \cdots"
        ).scale(0.8)

        eq2 = MathTex(
            r"= \left(1-\frac{x^2}{\pi^2}\right)\left(1-\frac{x^2}{4\pi^2}\right)\left(1-\frac{x^2}{9\pi^2}\right)\cdots"
        ).scale(0.8)

        group1 = VGroup(eq1, eq2).arrange(DOWN)
        group1.next_to(title, DOWN, buff=0.5)

        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(2)

        eq3 = MathTex(r"x=\frac{\pi}{2}")
        eq3.next_to(group1, DOWN, buff=0.8)
        self.play(Write(eq3))
        self.wait(1)

        eq4 = MathTex(
            r"f\left(\frac{\pi}{2}\right)=\frac{2}{\pi}"
        )
        eq5 = MathTex(
            r"=\left(1-\frac{1}{4}\right)\left(1-\frac{1}{16}\right)\left(1-\frac{1}{36}\right)\cdots"
        )

        group2 = VGroup(eq4, eq5).arrange(DOWN)
        group2.next_to(eq3, DOWN)

        self.play(Write(eq4))
        self.wait(1)
        self.play(Write(eq5))
        self.wait(2)

        final = MathTex(
            r"\frac{\pi}{2} = \frac{4}{3}\cdot\frac{16}{15}\cdot\frac{36}{35}\cdots = \prod_{n=1}^{\infty} \frac{4n^2}{4n^2-1}"
        ).scale(0.9)

        final.to_edge(DOWN)

        self.play(Write(final))
        self.wait(3)
