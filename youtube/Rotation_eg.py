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

        # 회전된 좌표계 복사
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

