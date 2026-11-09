"""Animate a 2D stress element as its coordinate axes rotate to principal axes.

Run from the repository root with

    python3 assets/tikz/metal_plasticity/stress_transformation_to_principal_animation.py

The example follows the passive coordinate transformation used in
metal_plasticity_11_stress_transformation.md:

    sigma_new = R sigma_old R^T,
    R = [[cos(theta), sin(theta)], [-sin(theta), cos(theta)]].
"""

from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/mpl-stress-transformation")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Arc, Polygon
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = (
    ROOT
    / "assets/img/lecture_notes/coordinate_transformation/"
    / "stress_transformation_to_principal_animation.gif"
)

SIGMA_OLD = np.array([[80.0, 20.0], [20.0, 50.0]])  # MPa
THETA_P = 0.5 * np.arctan2(
    2.0 * SIGMA_OLD[0, 1], SIGMA_OLD[0, 0] - SIGMA_OLD[1, 1]
)

NORMAL_COLOR = "#1769aa"
SHEAR_COLOR = "#d1495b"
AXIS_COLOR = "#1b7f5a"
ELEMENT_COLOR = "#e8f1f8"


def transformed_stress(theta):
    """Return R sigma R^T for a counterclockwise rotation of the axes."""
    c, s = np.cos(theta), np.sin(theta)
    rotation = np.array([[c, s], [-s, c]])
    return rotation @ SIGMA_OLD @ rotation.T


def arrow(ax, start, vector, color, width=2.2, mutation_scale=13):
    """Draw one stress arrow in data coordinates."""
    ax.annotate(
        "",
        xy=np.asarray(start) + np.asarray(vector),
        xytext=start,
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=width,
            mutation_scale=mutation_scale,
            shrinkA=0,
            shrinkB=0,
        ),
        zorder=6,
    )


def draw_stress_element(ax, theta, stress):
    """Draw the rotated element and normal/shear tractions on all four faces."""
    e1 = np.array([np.cos(theta), np.sin(theta)])
    e2 = np.array([-np.sin(theta), np.cos(theta)])
    half = 0.95
    corners = np.array(
        [
            -half * e1 - half * e2,
            half * e1 - half * e2,
            half * e1 + half * e2,
            -half * e1 + half * e2,
        ]
    )
    ax.add_patch(
        Polygon(
            corners,
            closed=True,
            facecolor=ELEMENT_COLOR,
            edgecolor="#315a76",
            linewidth=2.2,
            zorder=2,
        )
    )

    sigma_11, sigma_22, tau_12 = stress[0, 0], stress[1, 1], stress[0, 1]
    normal_scale = 0.62 / 90.0
    shear_scale = 0.72 / 20.0

    # On a face whose outward normal is n, traction is sigma*n.  Normal arrows
    # point outward because this example has tensile normal stresses.
    for sign in (-1.0, 1.0):
        face_1 = sign * half * e1
        face_2 = sign * half * e2
        arrow(ax, face_1, sign * normal_scale * sigma_11 * e1, NORMAL_COLOR)
        arrow(ax, face_2, sign * normal_scale * sigma_22 * e2, NORMAL_COLOR)
        if abs(tau_12) > 0.15:
            arrow(
                ax,
                face_1,
                sign * shear_scale * tau_12 * e2,
                SHEAR_COLOR,
                width=2.0,
            )
            arrow(
                ax,
                face_2,
                sign * shear_scale * tau_12 * e1,
                SHEAR_COLOR,
                width=2.0,
            )

    # Fixed original axes and rotating new axes.
    ax.plot([-1.75, 1.75], [0, 0], color="#a7adb4", lw=1.1, zorder=0)
    ax.plot([0, 0], [-1.75, 1.75], color="#a7adb4", lw=1.1, zorder=0)
    arrow(ax, np.zeros(2), 1.55 * e1, AXIS_COLOR, width=1.8, mutation_scale=11)
    arrow(ax, np.zeros(2), 1.55 * e2, AXIS_COLOR, width=1.8, mutation_scale=11)
    ax.text(*(1.70 * e1), r"$e'_1$", color=AXIS_COLOR, fontsize=13, ha="center")
    ax.text(*(1.70 * e2 - np.array([0.10, 0.0])), r"$e'_2$", color=AXIS_COLOR, fontsize=13, ha="center")
    ax.text(1.73, -0.14, r"$e_1$", color="#737a82", fontsize=11)
    ax.text(0.14, 1.62, r"$e_2$", color="#737a82", fontsize=11)

    angle_deg = np.degrees(theta)
    ax.add_patch(
        Arc((0, 0), 0.72, 0.72, theta1=0, theta2=angle_deg, color=AXIS_COLOR, lw=1.7)
    )
    if angle_deg > 2.0:
        label_angle = theta / 2.0
        ax.text(
            0.48 * np.cos(label_angle),
            0.48 * np.sin(label_angle),
            r"$\theta$",
            color=AXIS_COLOR,
            fontsize=12,
        )

    ax.text(
        -1.82,
        -1.88,
        "blue: normal stress     red: shear stress",
        fontsize=10.5,
        color="#3d4650",
    )


def draw_component_plot(ax, theta, stress):
    """Plot all transformed components and mark the current orientation."""
    theta_grid = np.linspace(0.0, THETA_P, 240)
    values = np.array([transformed_stress(value) for value in theta_grid])
    angle_grid = np.degrees(theta_grid)

    ax.plot(angle_grid, values[:, 0, 0], color=NORMAL_COLOR, lw=2.5, label=r"$\sigma'_{11}$")
    ax.plot(
        angle_grid,
        values[:, 1, 1],
        color="#5b8e3e",
        lw=2.5,
        label=r"$\sigma'_{22}$",
    )
    ax.plot(angle_grid, values[:, 0, 1], color=SHEAR_COLOR, lw=2.5, label=r"$\tau'_{12}$")
    angle_deg = np.degrees(theta)
    ax.axvline(angle_deg, color="#4d5966", lw=1.2, ls="--")
    ax.scatter(
        [angle_deg] * 3,
        [stress[0, 0], stress[1, 1], stress[0, 1]],
        s=38,
        color=[NORMAL_COLOR, "#5b8e3e", SHEAR_COLOR],
        edgecolor="white",
        linewidth=0.8,
        zorder=5,
    )
    ax.axhline(0, color="#b1b6bc", lw=0.9)
    ax.set_xlim(-0.5, np.degrees(THETA_P) + 1.0)
    ax.set_ylim(-5, 100)
    ax.set_xlabel(r"axis rotation $\theta$ (deg)")
    ax.set_ylabel("stress component (MPa)")
    ax.grid(color="#d9dde2", lw=0.7, alpha=0.8)
    ax.legend(loc="center right", frameon=True, fontsize=11)


def update(frame, figure, element_ax, plot_ax, angles):
    """Redraw one animation frame."""
    theta = angles[frame]
    stress = transformed_stress(theta)
    element_ax.clear()
    plot_ax.clear()

    draw_stress_element(element_ax, theta, stress)
    element_ax.set_aspect("equal")
    element_ax.set_xlim(-2.0, 2.0)
    element_ax.set_ylim(-2.05, 2.05)
    element_ax.axis("off")

    draw_component_plot(plot_ax, theta, stress)
    figure.suptitle(
        r"Stress transformation to the principal axes"
        + "\n"
        + rf"$\theta={np.degrees(theta):5.2f}^\circ$:  "
        + rf"$\sigma'_{{11}}={stress[0, 0]:5.1f}$ MPa,  "
        + rf"$\sigma'_{{22}}={stress[1, 1]:5.1f}$ MPa,  "
        + rf"$\tau'_{{12}}={stress[0, 1]:5.1f}$ MPa",
        fontsize=15,
        y=0.98,
    )
    if abs(theta - THETA_P) < 1.0e-10:
        element_ax.text(
            0,
            1.92,
            r"Principal axes: $\tau'_{12}=0$",
            ha="center",
            color="#8b2535",
            fontsize=13,
            weight="bold",
        )
    return []


def main():
    """Create a looping GIF with pauses at the original and principal axes."""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    forward = np.linspace(0.0, THETA_P, 42)
    backward = np.linspace(THETA_P, 0.0, 42)[1:-1]
    angles = np.concatenate(
        [np.repeat(0.0, 10), forward[1:], np.repeat(THETA_P, 18), backward]
    )

    figure, (element_ax, plot_ax) = plt.subplots(
        1,
        2,
        figsize=(12, 6.8),
        gridspec_kw={"width_ratios": [1.0, 1.15]},
        facecolor="white",
    )
    figure.subplots_adjust(left=0.035, right=0.97, bottom=0.11, top=0.84, wspace=0.18)
    animation = FuncAnimation(
        figure,
        update,
        frames=len(angles),
        fargs=(figure, element_ax, plot_ax, angles),
        interval=80,
        blit=False,
    )
    animation.save(OUTPUT, writer=PillowWriter(fps=12), dpi=100, savefig_kwargs={"facecolor": "white"})
    plt.close(figure)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
