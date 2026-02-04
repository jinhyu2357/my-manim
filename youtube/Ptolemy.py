from manim import *
import numpy as np

config.pixel_width = 1920
config.pixel_height = 1080

class PtolemyProof(Scene):
    def construct(self):

        # 원
        circle = Circle(radius=2)

        # 점 좌표 (원 위)
        A_angle = 30 * DEGREES
        B_angle = 120 * DEGREES
        C_angle = 180 * DEGREES
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
        AC = Line(A, C, color=BLUE)
        BD = Line(B, D, color=BLUE)

        self.play(Create(AC))
        self.play(Create(BD))
        self.wait(1)



        #설명
        E_text = MathTex(r"\text{Choose point } E \text{ on segment } AC \text{ so that } \angle ABE = \angle DBC.").shift(UP*3)
        self.play(Write(E_text))
        self.wait(3)
        



        #점 E를 찾는 과정
        DBC_angle = Angle(Line(B, D), Line(B, C)).get_value()

        # B에서 BA 방향 벡터
        BA_dir = (A.get_center() - B.get_center())
        BA_dir = BA_dir / np.linalg.norm(BA_dir)

        # BA를 angle_DBC 만큼 회전
        rot_matrix = rotation_matrix(DBC_angle, OUT)
        BE_dir = np.dot(rot_matrix, BA_dir)

        # B에서 충분히 긴 점 하나 생성 (임시점)
        temp_point = B.get_center() + BE_dir * 10
        temp_line = Line(B.get_center(), temp_point)

        # AC 직선
        ACum = Line(A.get_center(), C.get_center())

        # 교점 계산
        E_point = line_intersection(
            [temp_line.get_start(), temp_line.get_end()],
            [ACum.get_start(), ACum.get_end()]
        )

        # 점 E
        E = Dot(E_point, color=BLUE)
        labelE = MathTex("E").next_to(E, DOWN)
        self.play(Create(temp_line))
        self.play(FadeIn(E), Write(labelE))
        self.wait(1)
        
        #각이 같음을 표시하기


        # 각 객체 생성
        BA = Line(B, A)
        BE = Line(B, E)

        angle_ABE = Angle(BE, BA, radius=0.4, color=YELLOW)
        angle_DBC = Angle(BC, BD, radius=0.4, color=YELLOW)

        # 각 애니메이션
        self.play(Create(angle_ABE), Create(angle_DBC))
        self.wait(1)

        

        self.play(FadeOut(E_text))
        self.play(FadeOut(angle_ABE), FadeOut(angle_DBC), FadeOut(BA), FadeOut(BE),)
        self.wait(1)

        # 삼각형 ABE, DBC 강조
        '''tri1 = Polygon(A, B, E, color=BLUE)
        tri2 = Polygon(D, B, C, color=GREEN)''' #객체가 안맞는듯

        tri1 = Polygon(
            A.get_center(),
            B.get_center(),
            E.get_center(),
            color=YELLOW
        )

        tri2 = Polygon(
            D.get_center(),
            B.get_center(),
            C.get_center(),
            color=PURPLE
        )

        #삼각형 생성
        self.play(Create(tri1))
        self.play(Create(tri2))
        self.wait(1)


        #수식 작성을 위한 공간 확보
        group = VGroup(A, B, C, D, E, AB, BC, CD, DA, AC, BD, circle, labelA, labelB, labelC, labelD, labelE, temp_line, tri1, tri2)
        self.play(group.animate.shift(RIGHT*2.5, UP*2).scale(0.8))
        self.wait(1)
        
        
        #삼각형 강조
        self.play(Indicate(tri1))
        self.play(Indicate(tri2))
        #수식 작성
        eq0 = MathTex(r"\triangle ABE \sim \triangle DBC").shift(LEFT*2, UP*2)
        self.play(Write(eq0))
        self.wait(1)

        eq1 = MathTex(r"AB \cdot CD = AE \cdot BD").next_to(eq0, DOWN)
        self.play(Write(eq1))
        self.wait(5)

        group.remove(tri1)
        group.remove(tri2)
        self.play(FadeOut(tri1), FadeOut(tri2))


        # 삼각형 ABD, EBC 생성
        tri3 = Polygon(
            A.get_center(),
            B.get_center(),
            D.get_center(),
            color=YELLOW
        )
        
        tri4 = Polygon(
            E.get_center(),
            B.get_center(),
            C.get_center(),
            color=PURPLE
        )

        
        # 삼각형 생성
        self.play(Create(tri3))
        self.play(Create(tri4))
        self.wait(1)

        self.play(Indicate(tri3))
        self.play(Indicate(tri4))

        eq3 = MathTex(r"\triangle ABD \sim \triangle EBC").shift(LEFT*2)
        self.play(Write(eq3))
        self.wait(1)

        eq4 = MathTex(r"AD \cdot BC = EC \cdot BD").next_to(eq3, DOWN)
        self.play(Write(eq4))
        self.wait(5)

        # 최종 식
        final_eq = MathTex(
            r"AB\cdot CD + AD\cdot BC = (AE+EC)\cdot BD = AC\cdot BD"
        ).to_edge(DOWN)

        self.play(Write(final_eq))
        self.wait(3)
        self.play(FadeOut(tri3), FadeOut(tri4), FadeOut(eq0), FadeOut(eq1), FadeOut(eq3), FadeOut(eq4))
