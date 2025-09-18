from sympy import symbols
from sympy.plotting import plot

x = symbols('x')

p = plot(2*x + 5, x - 4, -3*x + 12,
        (x, -15, 15),
        ylim=(-15, 15),
        show=True,
        legend=True)

from manim import *

class GraphExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-15, 15, 5],
            y_range=[-15, 15, 5],
            axis_config={"include_numbers": True}
        )

        graph1 = axes.plot(lambda x: 2*x + 5, color=BLUE)
        graph2 = axes.plot(lambda x: x - 4, color=ORANGE)
        graph3 = axes.plot(lambda x: -3*x + 12, color=GREEN)

        labels = VGroup(
            axes.get_graph_label(graph1, "y=2x+5"),
            axes.get_graph_label(graph2, "y=x-4"),
            axes.get_graph_label(graph3, "y=-3x+12"),
        )

        self.add(axes, graph1, graph2, graph3, labels)

# GraphExample()

import matplotlib.pyplot as plt
import numpy as np
import tikzplotlib

x = np.linspace(-15, 15, 400)
plt.plot(x, 2*x+5, label="y=2x+5")
plt.plot(x, x-4, label="y=x-4")
plt.plot(x, -3*x+12, label="y=-3x+12")
plt.legend()
tikzplotlib.save("graph.tex")

