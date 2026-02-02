from manim import *

class Eulers_equation_prove(Scene):
    def construct(self):

        # Taylor series summary
        ex_final = VGroup(
            MathTex(r"e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots"),
            MathTex(r"\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots"),
            MathTex(r"\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots")
        ).arrange(DOWN, aligned_edge=LEFT)

        ex_final.scale(0.7)
        ex_final.to_corner(UL)

        self.play(Write(ex_final))
        self.wait(2)

        note = Text(
            "We have collected Taylor expansions. Let's prove Euler's equation.",
            font_size=28
        )
        note.next_to(ex_final, DOWN, aligned_edge=LEFT)
        self.play(Write(note))
        self.wait(2)



        # Step 1: e^(ix)
        eq1 = MathTex(
            r"e^{ix} = \sum_{n=0}^{\infty} \frac{(ix)^n}{n!}"
        ).shift(DOWN*1)

        self.play(Write(eq1))
        self.wait(2)

        # Step 2: expand
        eq2 = MathTex(
            r"= 1 + ix + \frac{(ix)^2}{2!} + \frac{(ix)^3}{3!} + \frac{(ix)^4}{4!} + \cdots"
        ).shift(DOWN*1)

        self.play(Transform(eq1, eq2))
        self.wait(2)

        # Step 3: separate real and imaginary parts
        eq3 = MathTex(
            r"= \left(1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots\right)"
            r"+ i\left(x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots\right)"
        ).shift(DOWN*0.8)

        self.play(Transform(eq1, eq3))
        self.wait(2)


        # 왼쪽 상단 cos 강조
        eq4 = MathTex(
            r"= cosx"
            r"+ i\left(x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots\right)"
        ).shift(DOWN*0.8)
        self.play(Indicate(ex_final[2], color=YELLOW))
        self.wait(1)
        self.play(Transform(eq1, eq4))
        self.wait(2)


        # 왼쪽 상단 sin 강조
        eq4 = MathTex(
            r"= cosx"
            r"+ isinx"
        ).shift(DOWN*0.8)
        self.play(Indicate(ex_final[1], color=YELLOW))
        self.wait(1)
        self.play(Transform(eq1, eq4))
        self.wait(2)


        # Step 4: final Euler formula
        final_eq = MathTex(r"e^{ix} = \cos x + i\sin x").scale(1.3).set_color(YELLOW).shift(DOWN*0.8)
        self.play(Transform(eq1, final_eq))
        self.wait(2)
