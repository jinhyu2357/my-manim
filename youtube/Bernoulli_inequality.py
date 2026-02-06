from manim import *

config.pixel_width = 1920
config.pixel_height = 1080

class BernoulliInduction(Scene):
    def construct(self):

        title = Text("Proof Bernoulli inequality by Mathematical Induction", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        step0 = MathTex(
            r"\forall x \in \mathbb{R},\ x \ge -1,\ \forall r \in \mathbb{Z},\ r \ge 0,\ (1+x)^r \ge 1+rx."
        ).scale(0.8)

        step1 = MathTex(
            r"1)\ r=0:\ (1+x)^0 \ge 1+0\cdot x \iff 1 \ge 1"
        ).scale(0.8)

        step2 = MathTex(
            r"2)\ Assume\ (1+x)^k \ge 1+kx"
        ).scale(0.8)

        step3 = MathTex(
            r"(1+x)^{k+1}=(1+x)^k(1+x)"
        ).scale(0.8)

        step4 = MathTex(
            r"\ge (1+kx)(1+x)=1+(k+1)x+kx^2"
        ).scale(0.8)

        step5 = MathTex(
            r"\ge 1+(k+1)x"
        ).scale(0.8)

        conclusion = MathTex(
            r"\therefore (1+x)^r \ge 1+rx \quad (r\ge0)"
        ).scale(0.9)

        group = VGroup(step0,step1, step2, step3, step4, step5, conclusion)
        group.arrange(DOWN, aligned_edge=LEFT).shift(DOWN*0.3)

        for item in group:
            self.play(Write(item))
            self.wait(5)

        self.wait(2)
