from manim import *
from manim_slides import Slide,ThreeDSlide
import numpy as np


# def argmin(f, x, x_dir):
#     """Find the argmin of a function f in the direction x_dir at point x"""
#     def g(s):
#         return f(x + s * x_dir)
#     mins = 0.01
#     for a in np.arange(0.1, 2, 0.1):
#         if g(a) < (g(mins)):
#             mins = a
#     return mins

class BasicAlgorithm(Slide):
    def construct(self):
        # A 2d plot of a function being minimized
        axes = Axes(
            x_range=(-3.5, 3.5, 1),
            y_range=(-0.5, 4, 1),
            x_length=7,
            y_length=7,
            axis_config={"include_tip": False, "include_numbers": False},
            # x_axis_config={"numbers_to_include": [0]},
            # y_axis_config={"numbers_to_include": [0,1,2]},
        )
        axes.add_coordinates()

        # Define the function and its gradient
        def function(x):
            #return (x - 1) ** 2 + 1
            return 0.05 * x**4 - 0.05*x**3 - 0.4*x**2 + 0.1 *x + 1.5
        def gradient(x):
            #return 2 * (x - 1)
            return 0.2 * x**3 - 0.15*x**2 - 0.8*x + 0.1
        
        def tangent_line(x0):
            return lambda x: gradient(x0) * (x - x0) + function(x0)

        # Create the function plot
        function_plot = axes.plot(function, color=BLUE)
        function_label = axes.get_graph_label(function_plot, label="f(x)", x_val=3)

        # Create the point representing the current position
        start_x = -2.6
        point = Dot(color=YELLOW).move_to(axes.coords_to_point(start_x, function(start_x)))

        # Create the update equation
        equation = MathTex(
            "x_{n+1}", "=", "x_n", "-", "\\alpha", "\\cdot", "\\nabla f(x_n)"
        ).next_to(point, direction=RIGHT)

        # Initialize the animation
        self.play(Create(axes), Create(function_plot), Create(function_label))

        # Start the gradient descent animation
        #self.play(Create(gradient_plot), Create(gradient_label))
        self.play(Create(point), Write(equation))

        # Misleading
        self.wait(3)
        self.play(FadeOut(function_plot))
        self.wait(3)

        # Perform gradient descent iterations
        alpha = 0.8  # learning rate
        num_iterations = 4
        self.wait()
        self.next_slide()

        for _ in range(num_iterations):
            xn = point.get_center()[0]
            grad = gradient(xn)
            xnp1 = xn - alpha * grad
            #xnp1 = argmin(function, xn, -grad)

            # # Create the arrow indicating the update direction
            # arrow = Arrow(
            #     start=point.get_center(),
            #     end=axes.coords_to_point(xnp1, function(xnp1)),
            #     color=GREEN,
            # )

            gradient_plot = axes.plot(tangent_line(xn), color=RED)
            gradient_label = axes.get_graph_label(gradient_plot, label="\\nabla f(x)", x_val=3)

        

            self.wait()
            self.play(Create(gradient_plot), Create(gradient_label))
            self.wait()
            self.next_slide()
        
            point.generate_target()
            point.target.move_to(axes.coords_to_point(xnp1, function(xnp1)))

            # Move the point to the new position
            self.play(MoveToTarget(point))
            self.wait()
            self.next_slide()
        
            self.play(FadeOut(gradient_plot), FadeOut(gradient_label))

            # self.play(FadeOut(arrow))


        self.wait(2)
        self.next_slide()
        self.play(Create(function_plot))        


class ConvexConcave(Slide):
    def construct(self):
        # 2d plot of a convex function
        axes = Axes(
            x_range=(-2, 2, 1),
            y_range=(0, 3, 1),
            tips=False,
            # x_axis_config={"numbers_to_include": [0]},
            # y_axis_config={"numbers_to_include": [0,1,2]},
        )
        labels = axes.get_axis_labels()
        
        convex = axes.plot(lambda x: (0.6*x**2), x_range=[-2,2], color=BLUE)
        convex_label = axes.get_graph_label(convex, label="convex", x_val=-2)

        concave = axes.plot(lambda x: -0.6*x**2 + 3, x_range=[-2,2], color=RED)
        concave_label = axes.get_graph_label(concave, label="concave", x_val=2)


        line_segment = axes.plot(lambda x: 1.5-0.2*x, x_range=[-2,2], color=YELLOW)
        self.play(FadeIn(axes), Create(convex), FadeIn(convex_label), Create(concave), FadeIn(concave_label))
        self.wait()
        self.next_slide()
        self.play(Create(line_segment))
        self.wait(3)



# class TwoDExOne(Slide):
#     def func(self, u, v):
#         return np.array([u,v,u**2 + v**2])
#     def construct(self):
#         axes = ThreeDAxes(x_range=[-2,2], x_length=4)
#         surface = Surface(self.func, u_range=[-2,2], v_range=[-2,2], resolution=(20,20))
#         surface.set_style(fill_opacity=1)
#         surface.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        
#         self.add(surface)
#         self.wait(5)