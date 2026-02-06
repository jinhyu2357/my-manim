from manim import *
import numpy as np

config.pixel_width = 1920
config.pixel_height = 1080

class PtolemyProof(Scene):
    def construct(self):

        # 원
        circle = Circle(radius=2, color=WHITE)

        # 점 좌표 (원 위)
        A_angle = 0 * DEGREES
        B_angle = 80 * DEGREES
        C_angle = 140 * DEGREES
        D_angle = 250 * DEGREES

        A = Dot(circle.point_at_angle(A_angle), color=RED)
        B = Dot(circle.point_at_angle(B_angle), color=RED)
        C = Dot(circle.point_at_angle(C_angle), color=RED)
        D = Dot(circle.point_at_angle(D_angle), color=RED)


        labelA = MathTex("A").next_to(A, RIGHT)
        labelB = MathTex("B").next_to(B, UP)
        labelC = MathTex("C").next_to(C, LEFT)
        labelD = MathTex("D").next_to(D, DOWN)

        self.play(Create(circle))
        self.play(FadeIn(A, B, C, D))
        self.play(Write(labelA), Write(labelB), Write(labelC), Write(labelD))
        self.wait(1)

        # 사각형 선분
        AB = Line(A, B)
        BC = Line(B, C)
        CD = Line(C, D)
        DA = Line(D, A)

        self.play(Create(AB), Create(BC), Create(CD), Create(DA))
        self.wait(1)

        # 대각선
        AC = Line(A, C, color=WHITE)
        BD = Line(B, D, color=WHITE)

        self.play(Create(AC))
        self.play(Create(BD))
        self.wait(1)
        

        #위 까지는 기본적인 도형 생성과정임
        #아래는 각도를 표시할거임
        color_text = MathTex(
            r"\alpha \text{ is yellow},\; \beta \text{ is blue},\; \gamma \text{ is green},\; \delta \text{ is purple.}"
        ).shift(UP*3)

        CA = Line(C, A)
        DB = Line(D, B)
        DC = Line(D, C)
        AD = Line(A, D)
        BA = Line(B, A)
        CB = Line(C, B)

        self.play(Write(color_text))
        angle_BAC = Angle(AB, AC, radius=0.7, color=YELLOW)
        self.play(Create(angle_BAC))
        angle_CBD = Angle(BC, BD, radius=0.7, color=BLUE)
        self.play(Create(angle_CBD))
        angle_ACD = Angle(CD, CA, radius=0.7, color=GREEN)
        self.play(Create(angle_ACD))
        angle_BDA = Angle(DA, DB, radius=0.7, color=PURPLE)
        self.play(Create(angle_BDA))

        angle_CDB = Angle(DB, DC, radius=0.7, color=YELLOW)
        self.play(Create(angle_CDB))
        angle_CAD = Angle(AC, AD, radius=0.7, color=BLUE)
        self.play(Create(angle_CAD))
        angle_ABD = Angle(BD, BA, radius=0.7, color=GREEN)
        self.play(Create(angle_ABD))
        angle_BCA = Angle(CA, CB, radius=0.7, color=PURPLE)
        self.play(Create(angle_BCA))
        self.wait(3)
        group = VGroup(
            circle,
            A, B, C, D,
            labelA, labelB, labelC, labelD,
            AB, BC, CD, DA,
            AC, BD,
            CA, DB, DC, AD, BA, CB,
            angle_BAC, angle_CBD, angle_ACD, angle_BDA,
            angle_CDB, angle_CAD, angle_ABD, angle_BCA,
        )
        self.play(group.animate.shift(LEFT*4.5).scale(0.7))
        self.wait(3)
        
        lines = VGroup(
            Tex(r"$AB = 2R\sin\alpha,\quad AD = 2R\sin\delta,\quad BC = 2R\sin\beta,\quad CD = 2R\sin\gamma$"),
            Tex(r"$AC = 2R\sin(\alpha+\beta),\quad BD = 2R\sin(\beta+\gamma)$"),

            Tex(r"$AB\cdot CD + AD\cdot BC$"),
            Tex(r"$= 2R\sin\alpha \cdot 2R\sin\gamma + 2R\sin\delta \cdot 2R\sin\beta$"),
            Tex(r"$= 4R^2(\sin\alpha\sin\gamma + \sin\delta\sin\beta)$"),
            Tex(r"$= 2R^2\{\cos(\alpha-\gamma)-\cos(\alpha+\gamma)+ \cos(\beta-\delta)-\cos(\beta+\delta)\}$"),

            Tex(r"$\cos(\alpha+\gamma)=\cos(\pi-(\beta+\delta))=-\cos(\beta+\delta)$"),
            Tex(r"So, $AB\cdot CD + AD\cdot BC = 2R^2\{\cos(\alpha-\gamma)+\cos(\beta-\delta)\}$"),

            Tex(r"Meanwhile, $AC\cdot BD = 2R\sin(\alpha+\beta)\cdot 2R\sin(\beta+\gamma)$"),
            Tex(r"$= 4R^2\sin(\alpha+\beta)\sin(\beta+\gamma)$"),
            Tex(r"$= 2R^2\{\cos(\alpha-\gamma)-\cos(\alpha+2\beta+\gamma)\}$"),

            Tex(r"$\alpha+\beta+\gamma=\pi-\delta$"),
            Tex(r"$\cos(\alpha+2\beta+\gamma)=\cos(\pi+(\beta-\delta))=-\cos(\beta-\delta)$"),

            Tex(r"So, $AC\cdot BD = 2R^2\{\cos(\alpha-\gamma)+\cos(\beta-\delta)\}$"),
        )



        lines.arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.55)
        lines.shift(RIGHT*2.5, DOWN*0.7)

        for line in lines:
            self.play(Write(line))
            self.wait(0.6)

        line1 = lines[13]  # So, AC·BD = ...
        line2 = lines[7]   # So, AB·CD + AD·BC = ...

        rect1 = SurroundingRectangle(line1, color=YELLOW, buff=0.1)
        rect2 = SurroundingRectangle(line2, color=YELLOW, buff=0.1)

        self.play(Create(rect1), Create(rect2))
        self.wait(1)
        self.play(Write(Tex(r"Therefore, $AB\cdot CD + AD\cdot BC = AC\cdot BD$").shift(DOWN*3.85).scale(0.55)))
        self.wait(3)



