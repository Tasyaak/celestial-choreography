import numpy as np
from manim import *


class TestCelestial(Scene):
    def construct(self) -> None:
        title = Text("Celestial Choreography", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        colors = [RED, GREEN, BLUE]
        angles = [0, 2 * PI / 3, 4 * PI / 3]

        orbit = Circle(radius=2, color=GRAY, stroke_opacity=0.5)
        self.play(Create(orbit))

        bodies = VGroup()

        for color, angle in zip(colors, angles):
            position = 2 * np.array([
                np.cos(angle),
                np.sin(angle),
                0,
            ])
            body = Dot(point=position, color=color, radius=0.12)
            bodies.add(body)

        self.play(FadeIn(bodies))

        # One shared parameter controls the orbital motion.
        phase = ValueTracker(0)

        for body, angle in zip(bodies, angles):
            body.add_updater(
                lambda mob, a=angle: mob.move_to(
                    2 * np.array([
                        np.cos(phase.get_value() + a),
                        np.sin(phase.get_value() + a),
                        0,
                    ])
                )
            )

        self.play(
            phase.animate.set_value(TAU),
            run_time=5,
            rate_func=linear,
        )

        for body in bodies:
            body.clear_updaters()

        self.wait(1)