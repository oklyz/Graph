from manim import *

class ParabolaAnimation(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-2, 8],
            axis_config={"include_numbers": True}
        )
        self.add(axes)

        parabola = axes.plot(lambda x: x**2, color=GREEN)
        label = axes.get_graph_label(parabola, "y=x^2")

        self.play(Create(parabola), Write(label))
        self.wait(1)

        # Animate parabola changing to y = 2x^2
        new_parabola = axes.plot(lambda x: 2*x**2, color=RED)
        new_label = axes.get_graph_label(new_parabola, "y=2x^2")

        self.play(Transform(parabola, new_parabola),
                Transform(label, new_label),
                run_time=3)
        self.wait(2)
