from manim import *

class EulerBasel(Scene):
    def construct(self):

        title = Text("proof of Basel problem by Euler", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # 1. sin x 테일러 급수
        step1 = MathTex(
            r"\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots"
        )
        self.play(Write(step1))
        self.wait(2)

        # 2. sin(x)/x 테일러 급수
        step2 = MathTex(
            r"\frac{\sin x}{x} = 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \cdots"
        )
        self.play(Transform(step1, step2))
        self.wait(2)

        # 3. 해 나열
        step3 = MathTex(
            r"\frac{\sin x}{x} = 0 \Rightarrow x = \pm \pi, \pm 2\pi, \pm 3\pi, \dots"
        )
        self.play(Transform(step1, step3))
        self.wait(2)

        # 4. 무한곱 방정식
        step4 = MathTex(
            r"\frac{\sin x}{x} = \prod_{n=1}^{\infty} \left(1 - \frac{x^2}{n^2\pi^2}\right)"
        )
        self.play(Transform(step1, step4))
        self.wait(2)

        self.play(Transform(step1, step4))
        self.wait(2)

        # 무한곱을 풀어 쓴 형태 (아래에 표시)
        step4_expand = MathTex(
            r"= \left(1 - \frac{x^2}{\pi^2}\right)"
            r"\left(1 - \frac{x^2}{4\pi^2}\right)"
            r"\left(1 - \frac{x^2}{9\pi^2}\right)\cdots"
        )

        step4_expand.scale(0.9)
        step4_expand.next_to(step4, DOWN)

        self.play(Write(step4_expand))
        self.wait(3)

        self.play(FadeOut(step4_expand))


        # 5. 전개 (x^2항까지만)
        step5 = MathTex(
            r"= 1 - \left(\frac{1}{\pi^2}\sum_{n=1}^\infty \frac{1}{n^2}\right)x^2 + \cdots"
        )
        self.play(Transform(step1, step5))
        self.wait(2)


        # step6
        # sin(x)/x 테일러 전개식
        taylor = MathTex(
            r"\frac{\sin x}{x} = 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \cdots"
        ).shift(UP*2)

        self.play(Write(taylor))
        self.wait(2)

        # x^2 항 강조
        taylor_x2 = taylor[0][9:14]   # - x^2/3! 부분 (인덱스는 환경에 따라 약간 조정 필요)

        self.play(
            taylor_x2.animate.set_color(RED),
        )
        self.wait(2)

        # 나머지 항 페이드 아웃 (계수만 남기기)
        self.play(
            FadeOut(taylor[0][0:9]),
            FadeOut(taylor[0][14:]),
        )
        self.wait(1)

        # 계수 비교 식만 중앙에 정리
        step6 = MathTex(
            r" \frac{x^{2}}{3!} = \left ( \frac{1}{\pi^2}\sum_{n=1}^\infty \frac{1}{n^2} \right )x^{2}"
        ).shift(UP*2)


        self.play(Transform(taylor_x2, step6))
        self.wait(2)



        # 7. 바젤 문제 결론
        step7 = MathTex(
            r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}"
        )
        self.play(Transform(step1, step7))
        self.wait(3)

        box = SurroundingRectangle(step7)
        self.play(Create(box))
        self.wait(2)
