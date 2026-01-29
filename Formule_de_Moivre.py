from manim import *

class DeMoivre(Scene):
    def construct(self):
        title = Text("Derived using Euler's formula").to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        note = Text(
            "for any real number x and integer n",
            font_size=28
        ).shift(UP*1)
        
        self.play(Write(note))

        eq1 = MathTex(r"e^{ix} = \cos x + i\sin x")
        eq2 = MathTex(r"\left(e^{ix}\right)^n = e^{i(nx)}")
        eq3 = MathTex(r"e^{i(nx)} = \cos(nx) + i\sin(nx)")

        eq1.move_to(ORIGIN)

        self.play(Write(eq1))
        self.wait(2)

        eq2.next_to(eq1, DOWN, buff=0.8)
        self.play(Write(eq2))
        self.wait(2)

        eq3.next_to(eq2, DOWN, buff=0.8)
        self.play(Write(eq3))
        self.wait(1)

        box = SurroundingRectangle(eq3, color=YELLOW)
        self.play(Create(box))
        self.wait(2)
