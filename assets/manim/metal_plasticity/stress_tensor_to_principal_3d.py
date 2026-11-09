"""Render a 3D stress-tensor transformation into its principal basis.

From the repository root:

    manim -qm assets/manim/metal_plasticity/stress_tensor_to_principal_3d.py \
        StressTensorToPrincipal3D

The animation uses the passive coordinate transformation

    sigma_new = R sigma_old R.T

and rotates the coordinate basis continuously from R = I to the orthogonal
eigenvector matrix Q.  At R = Q, sigma_new is diagonal.
"""

from __future__ import annotations

import numpy as np

from manim import (
    Arrow3D,
    BLACK,
    BLUE_D,
    BLUE_E,
    Create,
    Cube,
    DEGREES,
    DOWN,
    FadeIn,
    GREEN_D,
    GREY_B,
    GREY_D,
    LEFT,
    Matrix,
    MathTex,
    ORANGE,
    ORIGIN,
    RED_D,
    RIGHT,
    Rotate,
    RoundedRectangle,
    ThreeDAxes,
    ThreeDScene,
    UP,
    VGroup,
    WHITE,
    Write,
    smooth,
)


# Rows of Q are the principal basis vectors expressed in the original basis.
# Q is a proper orthogonal matrix: Q Q^T = I and det(Q) = +1.
Q = np.array(
    [
        [1.0, 2.0, 2.0],
        [2.0, 1.0, -2.0],
        [-2.0, 2.0, -1.0],
    ]
) / 3.0
SIGMA_PRINCIPAL = np.diag([90.0, 45.0, -27.0])
SIGMA_OLD = Q.T @ SIGMA_PRINCIPAL @ Q


def axis_angle_from_matrix(rotation: np.ndarray) -> tuple[np.ndarray, float]:
    """Return the unit axis and angle of a proper 3D rotation matrix."""
    angle = np.arccos(np.clip((np.trace(rotation) - 1.0) / 2.0, -1.0, 1.0))
    axis = np.array(
        [
            rotation[2, 1] - rotation[1, 2],
            rotation[0, 2] - rotation[2, 0],
            rotation[1, 0] - rotation[0, 1],
        ]
    ) / (2.0 * np.sin(angle))
    return axis / np.linalg.norm(axis), angle


# The coordinate triad is actively rotated by Q^T so its columns become the
# rows of Q.  This is the geometric counterpart of the passive transformation.
ACTIVE_ROTATION = Q.T
ROTATION_AXIS, ROTATION_ANGLE = axis_angle_from_matrix(ACTIVE_ROTATION)


def rodrigues(axis: np.ndarray, angle: float) -> np.ndarray:
    """Construct an active rotation matrix from an axis and angle."""
    x, y, z = axis
    cross = np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])
    identity = np.eye(3)
    return identity + np.sin(angle) * cross + (1.0 - np.cos(angle)) * (cross @ cross)


def transformed_stress(alpha: float) -> np.ndarray:
    """Return stress components in the basis at animation progress alpha."""
    active = rodrigues(ROTATION_AXIS, alpha * ROTATION_ANGLE)
    passive = active.T
    return passive @ SIGMA_OLD @ passive.T


def matrix_display(
    values: np.ndarray,
    center=np.array([3.65, 0.35, 0.0]),
    principal: bool = False,
) -> tuple[VGroup, Matrix]:
    """Create a fixed-frame numeric 3x3 matrix and its surrounding panel."""
    panel = RoundedRectangle(
        width=5.25,
        height=3.45,
        corner_radius=0.16,
        stroke_color=GREY_B,
        stroke_width=1.5,
        fill_color=WHITE,
        fill_opacity=0.94,
    ).move_to(center)
    title = MathTex(
        r"[\boldsymbol\sigma]'=R[\boldsymbol\sigma]R^T\quad(\mathrm{MPa})",
        color=BLACK,
        font_size=32,
    ).move_to(center + 1.34 * UP)

    numeric_values = np.rint(values).astype(int).tolist()
    matrix = Matrix(
        numeric_values,
        element_to_mobject=MathTex,
        element_to_mobject_config={"color": BLACK, "font_size": 30},
        h_buff=1.05,
        v_buff=0.62,
        bracket_h_buff=0.18,
        bracket_v_buff=0.12,
    ).move_to(center + 0.05 * DOWN)
    matrix.get_brackets().set_color(BLACK)
    for index in (1, 2, 3, 5, 6, 7):
        matrix.get_entries()[index].set_color(RED_D)

    status = MathTex(
        r"\sigma_{ij}=0\ (i\ne j):\ \mathrm{principal\ basis}"
        if principal
        else r"\sigma_{ij}\ (i\ne j):\ \mathrm{shear\ components}",
        color=BLUE_D if principal else RED_D,
        font_size=25,
    ).move_to(center + 1.32 * DOWN)

    group = VGroup(
        panel,
        title,
        matrix,
        status,
    )
    return group, matrix


class StressTensorToPrincipal3D(ThreeDScene):
    """Show a 3D stress tensor becoming diagonal in its principal basis."""

    def construct(self):
        self.camera.background_color = WHITE
        self.set_camera_orientation(phi=67 * DEGREES, theta=-48 * DEGREES, zoom=0.78)

        title = MathTex(
            r"\text{3D stress transformation to the principal basis}",
            color=BLACK,
            font_size=35,
        ).to_edge(UP, buff=0.22)
        subtitle = MathTex(
            r"[\boldsymbol\sigma]_{\mathrm{old}}="
            r"\begin{bmatrix}18&42&-6\\42&33&36\\-6&36&57\end{bmatrix}\,\mathrm{MPa}",
            color=BLACK,
            font_size=28,
        ).next_to(title, DOWN, buff=0.15).shift(3.2 * LEFT)
        self.add_fixed_in_frame_mobjects(title, subtitle)

        axes = ThreeDAxes(
            x_range=[-2.8, 2.8, 1],
            y_range=[-2.8, 2.8, 1],
            z_range=[-2.8, 2.8, 1],
            x_length=5.3,
            y_length=5.3,
            z_length=5.3,
            axis_config={"color": GREY_D, "stroke_opacity": 0.45, "stroke_width": 1.4},
            tips=False,
        ).shift(2.9 * LEFT)

        cube = Cube(
            side_length=1.65,
            fill_color=BLUE_E,
            fill_opacity=0.07,
            stroke_color=BLUE_D,
            stroke_width=2.1,
            stroke_opacity=0.72,
        ).shift(2.9 * LEFT)

        origin = 2.9 * LEFT
        axis_colors = [BLUE_D, GREEN_D, ORANGE]
        basis_vectors = VGroup(
            *[
                Arrow3D(
                    start=origin,
                    end=origin + 2.35 * direction,
                    color=color,
                    thickness=0.032,
                    height=0.22,
                    base_radius=0.085,
                )
                for direction, color in zip(np.eye(3), axis_colors)
            ]
        )
        rotating_group = VGroup(cube, basis_vectors)

        principal_vectors = VGroup(
            *[
                Arrow3D(
                    start=origin,
                    end=origin + 2.65 * Q[row],
                    color=GREY_D,
                    thickness=0.012,
                    height=0.12,
                    base_radius=0.045,
                ).set_opacity(0.32)
                for row in range(3)
            ]
        )

        component_panel, _ = matrix_display(SIGMA_OLD)
        principal_panel, _ = matrix_display(
            SIGMA_PRINCIPAL,
            principal=True,
        )
        final_caption = MathTex(
            r"[\boldsymbol\sigma]_{\mathrm{principal}}="
            r"\operatorname{diag}(90,45,-27)\,\mathrm{MPa}",
            color=BLACK,
            font_size=28,
        ).next_to(principal_panel, DOWN, buff=0.12)
        basis_legend_row = VGroup(
            MathTex(r"e'_1", color=BLUE_D, font_size=28),
            MathTex(r"e'_2", color=GREEN_D, font_size=28),
            MathTex(r"e'_3", color=ORANGE, font_size=28),
            MathTex(r"\text{: colored arrows = basis vectors}", color=BLACK, font_size=22),
        ).arrange(RIGHT, buff=0.18)
        legend = VGroup(
            basis_legend_row,
            MathTex(
                r"\text{arrows are directions, not stress components }\sigma_{ij}",
                color=RED_D,
                font_size=21,
            ),
            MathTex(
                r"\text{faint gray arrows = target eigenvector directions}",
                color=GREY_D,
                font_size=20,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).to_edge(DOWN, buff=0.16).shift(2.45 * LEFT)
        final_legend = VGroup(
            MathTex(r"e'_1", color=BLUE_D, font_size=28),
            MathTex(r"e'_2", color=GREEN_D, font_size=28),
            MathTex(r"e'_3", color=ORANGE, font_size=28),
            MathTex(r"\text{: principal-basis vectors}", color=BLACK, font_size=22),
        ).arrange(RIGHT, buff=0.18).to_edge(DOWN, buff=0.25).shift(2.55 * LEFT)
        self.add_fixed_in_frame_mobjects(
            component_panel,
            principal_panel,
            final_caption,
            legend,
            final_legend,
        )
        principal_panel.set_opacity(0)
        final_caption.set_opacity(0)
        final_legend.set_opacity(0)

        self.play(Write(title), Write(subtitle), run_time=1.5)
        self.play(Create(axes), FadeIn(cube), Create(basis_vectors), run_time=1.8)
        self.play(FadeIn(component_panel), FadeIn(legend), run_time=1.2)
        self.wait(1.0)

        self.play(FadeIn(principal_vectors), run_time=1.2)
        self.wait(0.8)

        self.play(
            Rotate(
                rotating_group,
                angle=ROTATION_ANGLE,
                axis=ROTATION_AXIS,
                about_point=origin,
            ),
            run_time=6.0,
            rate_func=smooth,
        )

        # Swap fixed-frame panels only after the continuous 3D rotation.  This
        # avoids transient glyph distortion in Cairo's fixed-frame rendering.
        # Reveal already-registered fixed-frame objects without adding or
        # removing glyphs after the 3D camera has begun rendering.
        principal_panel.set_opacity(1)
        final_caption.set_opacity(1)
        principal_vectors.set_opacity(0)
        legend.set_opacity(0)
        final_legend.set_opacity(1)
        self.wait(1.0)

        # Hold the original view, then cut to the opposite side.  The two
        # projections clarify the three spatial directions without moving the
        # arrows behind the fixed-frame matrix panel.
        self.wait(2.0)
        self.set_camera_orientation(
            phi=55 * DEGREES,
            theta=-112 * DEGREES,
            zoom=0.82,
        )
        self.wait(2.8)

