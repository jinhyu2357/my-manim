from manim import *
import numpy as np
import math

class TaylorSeriesScene(Scene):
    #좌표 축 설정
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 10, 1],
            x_length=8,
            y_length=5,
            axis_config={"color": BLUE},
        ).to_edge(DOWN)

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))


        # 원래 함수 e^x
        equation = MathTex("y = e^x").shift(RIGHT*4 + DOWN*1)
        self.play(Write(equation))

        exp_graph = axes.plot(lambda x: np.exp(x), color=YELLOW)
        exp_label = MathTex("f(x)=e^x").next_to(exp_graph, UP)

        self.play(Create(exp_graph), Write(exp_label))
        self.wait(1)

        note = Text(
            "We apply Taylor series  as  an example.",
            font_size=20
        ).shift(LEFT*3 + UP*2)
        self.play(Write(note))



        # 테일러 함수
        def taylor_exp(x, n):
            return sum((x**k) / math.factorial(k) for k in range(n+1))

        # 전개식 문자열 생성 함수
        def expanded_taylor_tex(n):
            terms = []
            for k in range(n+1):
                if k == 0:
                    terms.append("1")
                elif k == 1:
                    terms.append("x")
                else:
                    terms.append(rf"\frac{{x^{k}}}{{{k}!}}")
            return " + ".join(terms)

        colors = [RED, GREEN, ORANGE, PURPLE, RED]
        orders = [1, 2, 3, 4, 7]

        previous_graph = None

        # 폰트 크기
        SIGMA_FONT = 36
        EXPAND_FONT = 28

        for n, color in zip(orders, colors):
            taylor_graph = axes.plot(
                lambda x: taylor_exp(x, n),
                color=color
            )

            sigma_formula = MathTex(
                rf"T_{n}(x)=\sum_{{k=0}}^{n} \frac{{x^k}}{{k!}}",
                font_size=SIGMA_FONT
            ).shift(LEFT*4)

            expanded_formula = MathTex(
                rf"T_{n}(x)= {expanded_taylor_tex(n)}",
                font_size=EXPAND_FONT
            ).next_to(sigma_formula, DOWN)

            # 이전 그래프 제거
            if previous_graph:
                self.play(FadeOut(previous_graph))

            self.play(Write(sigma_formula))
            self.play(Write(expanded_formula))
            self.play(Create(taylor_graph))
            self.wait(2)

            self.play(FadeOut(sigma_formula), FadeOut(expanded_formula))

            previous_graph = taylor_graph

        self.play(FadeOut(previous_graph))
        self.wait(2)
        note = Text(
            "Taylor series makes sense",
            font_size=20
        ).shift(LEFT*3)
        self.play(Write(note))
