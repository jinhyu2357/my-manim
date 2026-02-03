from manim import *

config.pixel_width = 1920
config.pixel_height = 1080

class Derivative_ax(Scene):
    def construct(self):
        step0 = MathTex(r"(a^x)' = a^x \ln a \quad (a>0,\ a\ne 1)").shift(UP*3)
        self.play(Write(step0))
        self.wait(1)



        step1 = MathTex(r"\lim_{h\to 0} \frac{a^h - 1}{h} = \ln a").shift(UP*2)
        self.play(Write(step1))
        self.wait(2)

        step2 = MathTex(r"let,    u = a^h - 1 \Rightarrow a^h = 1+u")
        step2.next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(2)

        step3 = MathTex(r"h = \log_a(1+u) = \frac{\ln(1+u)}{\ln a}")
        step3.next_to(step2, DOWN)
        self.play(Write(step3))
        self.wait(2)

        step4 = MathTex(
            r"\lim_{h\to 0}\frac{a^h-1}{h}"
            r"=\lim_{u\to 0}\frac{ulna}{\ln(1+u)}"
        )
        step4.next_to(step3, DOWN)
        self.play(Write(step4))
        self.wait(2)

        step5 = MathTex(
            r"=\ln a \cdot \lim_{u\to 0} \frac{u}{\ln(1+u)} = \ln a"
        )
        step5.next_to(step4, DOWN)
        self.play(Write(step5))
        self.wait(2)

        self.play(Indicate(step1))
        self.play(FadeOut(step2, step3, step4, step5))

        








        step6 = MathTex(r"f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}").shift(UP*0.5)
        self.play(Write(step6))
        self.wait(2)

        step7 = MathTex(r"f(x)=a^x")
        step7.next_to(step6, DOWN)
        self.play(Write(step7))
        self.wait(1)

        step8 = MathTex(r"\frac{d}{dx}(a^x)=\lim_{h\to0}\frac{a^{x+h}-a^x}{h}")
        step8.next_to(step7, DOWN)
        self.play(Write(step8))
        self.wait(2)


        self.play(FadeOut(step6, step7))
        self.play(step8.animate.shift(UP*1.5))




        step9 = MathTex(r"= a^x\lim_{h\to0}\frac{a^h-1}{h}")
        step9.next_to(step8, DOWN)
        self.play(Write(step9))
        self.wait(2)

        step10 = MathTex(r"= a^x \ln a")
        step10.next_to(step9, DOWN)
        self.play(Write(step10))
        self.wait(2)

        box = SurroundingRectangle(step10)
        self.play(Create(box))
        self.wait(2)
