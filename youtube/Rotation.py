from manim import *
import numpy as np

config.pixel_width = 1920
config.pixel_height = 1080

class Rotation(Scene):
    def construct(self):
        # 기본 좌표축
        axes = Axes(
            x_range=[-4,4,1],
            y_range=[-4,4,1],
            x_length=6,
            y_length=6,
            tips=True
        ).scale(0.8)
        axes_labels = axes.get_axis_labels("x", "y")


        # 회전 각도 (30도)
        theta = 30 * DEGREES

        # 회전 행렬
        R = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta),  np.cos(theta), 0],
            [0, 0, 1]
        ])

        # 회전된 좌표계
        rotated_axes = axes.copy().set_color(YELLOW)
        rotated_labels = VGroup(
            MathTex("x'").next_to(rotated_axes.x_axis.get_end()),
            MathTex("y'").next_to(rotated_axes.y_axis.get_end()),
        )
        rotated_group = VGroup(rotated_axes, rotated_labels)


        # 각도 표시 (30도)
        angle_arc = Arc(
            radius=1,
            start_angle=0,
            angle=theta,
            color=RED
        )
        angle_text = MathTex("30^\\circ").next_to(angle_arc, RIGHT)


        # 애니메이션
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)

        #회전하는 애니메이션
        self.play(Create(rotated_group))
        self.play(Rotate(rotated_group, angle=theta, about_point=rotated_axes.get_origin()))

        #각도 표시
        self.play(Create(angle_arc), Write(angle_text))
        self.wait(2)
        self.play(FadeOut(angle_arc), FadeOut(angle_text))



        #좌표계 분리
        self.play(axes.animate.shift(RIGHT*2), axes_labels.animate.shift(RIGHT*2)) #기존 좌표계
        self.play(rotated_group.animate.shift(LEFT*2))#회전된 좌표계
        self.wait(2)






        #다음 장면 넘어가기(페이드 아웃)
        self.play(FadeOut(axes, axes_labels, rotated_group))

        #설명(무엇을 할것인지)
        texts = VGroup(
            Text("We rotated the coordinate system."),
            Text("What will the coordinates of a point be in the new coordinate system?"),
            Text("Let's find out.")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.5)

        self.play(Write(texts))
        self.wait(2)
        self.play(FadeOut(texts))





        #좌표계(기존과 회전)에서 같은 선분에 대해 삼각형을 만듬
        theta = 15 * DEGREES # 시각적으로 잘 보이게 하기위한 각도 설정
        # 기본 좌표축(new)
        axes = Axes(
            x_range=[-1,4,1],
            y_range=[-1,4,1],
            x_length=6,
            y_length=6,
            tips=True
        ).shift(LEFT*4)
        axes_labels = axes.get_axis_labels("x", "y")

        self.play(Create(axes), Write(axes_labels))
        self.wait(1)

        #회전한 좌표계(new)
        rotated_axes = axes.copy().shift(RIGHT*8)
        origin = rotated_axes.get_origin()
        rotated_axes.rotate(theta, about_point=origin)
        self.play(Create(rotated_axes))




        #각 좌표계에서 같은 선분 생성
        L = 2
        angle = 45 * DEGREES  # Manim 상수
        angle1 = 30 * DEGREES  # Manim 상수
        # 기본 좌표계에서 선분
        start1 = axes.c2p(0, 0)
        end1 = axes.c2p(
            L*np.cos(angle),
            L*np.sin(angle)
        )
        line1 = Line(start1, end1, color=BLUE)

        # 회전 좌표계에서 선분
        start2 = rotated_axes.c2p(0, 0)
        end2 = rotated_axes.c2p(
            L*np.cos(angle1),
            L*np.sin(angle1)
        )
        line2 = Line(start2, end2, color=RED)

        self.play(Create(line1), Create(line2))


        #수선 내리기
        # 수선 (기본 좌표계)
        x1, y1 = L*np.cos(angle), L*np.sin(angle)
        foot1 = axes.c2p(x1, 0)

        perp1 = DashedLine(
            axes.c2p(x1, y1),
            foot1,
            color=BLUE
        )

        base1 = Line(
            axes.c2p(0, 0),
            foot1,
            color=BLUE
        )

        # 수선 (회전 좌표계)
        x2, y2 = L*np.cos(angle1), L*np.sin(angle1)
        foot2 = rotated_axes.c2p(x2, 0)

        perp2 = DashedLine(
            rotated_axes.c2p(x2, y2),
            foot2,
            color=RED
        )

        base2 = Line(
            rotated_axes.c2p(0, 0),
            foot2,
            color=RED
        )

        self.play(Create(perp1), Create(perp2))
        self.play(Create(base1), Create(base2))




        #무엇을 했는지 설명
        text = Text("The same line segment was placed in both coordinate systems.", font_size=20).shift(UP*3)
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))

        #각도를 표시하기
        x_axis_vec1 = Line(
            axes.c2p(0, 0),
            axes.c2p(1, 0),
        )

        x_axis_vec2 = Line(
            rotated_axes.c2p(0, 0),
            rotated_axes.c2p(1, 0),
        )

        # 각도 표시
        angle_theta = Angle(x_axis_vec1, line1, radius=0.7, color=YELLOW)
        angle_theta_p = Angle(x_axis_vec2, line2, radius=0.7, color=GREEN)

        # 각도 라벨
        theta_label = MathTex(r"\theta").next_to(angle_theta, UP)
        theta_p_label = MathTex(r"\theta'").next_to(angle_theta_p, UP)

        self.play(Create(angle_theta), Create(angle_theta_p))
        self.play(Write(theta_label), Write(theta_p_label))


        #회전된 좌표계를 기존 좌표계와 같이 보기(축을 원래대로)
        group = VGroup(line2, perp2, theta_p_label, angle_theta_p, rotated_axes, base2)
        self.play(group.animate.rotate(-15*DEGREES, about_point=origin))

        #삼각형만 남기기
        group = VGroup(axes, rotated_axes, axes_labels)
        self.play(FadeOut(group))
        self.wait(1)

        # 기존 좌표계


        # 텍스트 (아무 문자 써도 된다고 하셨으니 A,B,C 사용)
        label_hyp1 = MathTex("d").next_to(line1.get_center(), UP*2)
        label_base1 = MathTex("x").next_to(base1.get_center(), DOWN)
        label_perp1 = MathTex("y").next_to(perp1.get_center(), RIGHT)

        self.play(Write(label_hyp1), Write(label_base1), Write(label_perp1))

        #회전 좌표게


        label_hyp2 = MathTex("d").next_to(line2.get_center(), UP*2)
        label_base2 = MathTex("x'").next_to(base2.get_center(), DOWN)
        label_perp2 = MathTex("y'").next_to(perp2.get_center(), RIGHT)

        self.play(Write(label_hyp2), Write(label_base2), Write(label_perp2))

        #수식 출력
        formula_s = MathTex(r"x = d \cos(\theta) \\ y = d \sin(\theta)").shift(UP*2, LEFT*2)
        self.play(Write(formula_s))

        formula = MathTex(r"x' = d \cos(\theta + \gamma) \\ y' = d \sin(\theta + \gamma) \\ \theta' = \theta + \gamma").shift(UP*2, RIGHT*2)
        self.play(Write(formula))

        group = VGroup(theta_label, theta_p_label, perp1, perp2, base1, base2, label_hyp1, label_hyp2, label_base1, label_base2, label_perp1, label_perp2, line1, line2, angle_theta, angle_theta_p)
        self.play(FadeOut(group))


        
        formula = MathTex(r"\cos(A + B) = \cos(A) \cos(B) - \sin(A) \sin(B) \\ \sin(A + B) = \sin(A) \cos(B) + \cos(A) \sin(B)").scale(0.8)
        self.play(Write(formula))

        texts = VGroup(
            Text("We will use the angle addition and subtraction formulas.")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.5).shift(DOWN*2)
        self.play(Write(texts))
        self.wait(3)
        self.play(FadeOut(texts))


        formula = MathTex(r"x' = d \cos(\theta + \gamma)").shift(DOWN*1.5, LEFT*3).scale(0.7)
        self.play(Write(formula))

        formula = MathTex(r"x' = d \cos(\theta) \cos(\gamma) - d \sin(\theta) \sin(\gamma)").shift(DOWN*2.2, LEFT*3).scale(0.7)
        self.play(Write(formula))

        self.play(Indicate(formula_s)) #인용한 식 강조

        formula_x = MathTex(r"x' = x \cos(\gamma) - y \sin(\gamma)").shift(DOWN*2.9, LEFT*3).scale(0.7)
        self.play(Write(formula_x))
        self.wait(3)



        formula = MathTex(r"y' = d\sin(\theta + \gamma)").shift(DOWN*1.5, RIGHT*3).scale(0.7)
        self.play(Write(formula))

        formula = MathTex(r"y' = d\sin(\theta)\cos(\gamma) + d\cos(\theta)\sin(\gamma)").shift(DOWN*2.2, RIGHT*3).scale(0.7)
        self.play(Write(formula))

        self.play(Indicate(formula_s)) #인용한 식 강조

        formula_y = MathTex(r"y' = y\cos(\gamma) + x\sin(\gamma)").shift(DOWN*2.9, RIGHT*3).scale(0.7)
        self.play(Write(formula_y))
        self.wait(3)
        self.play(Indicate(formula_x))
        self.play(Indicate(formula_y))
        




        









        