"""Create the matrix-vector linear-transformation animation used in lecture 12."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter


OUTPUT = Path("assets/img/lecture_notes/data_mse/linear_transformation_matrix_vector.gif")
TARGET_MATRIX = np.array([[1.2, 0.6], [0.2, 1.1]])
VECTOR = np.array([1.0, 1.0])


def smoothstep(value: float) -> float:
    return value * value * (3.0 - 2.0 * value)


def animation_parameters() -> list[float]:
    forward = [smoothstep(value) for value in np.linspace(0.0, 1.0, 36)]
    backward = [smoothstep(value) for value in np.linspace(1.0, 0.0, 36)]
    return [0.0] * 8 + forward + [1.0] * 12 + backward + [0.0] * 8


def draw_arrow(axis, start, end, color, label, label_offset=(0.08, 0.08)):
    axis.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.7},
    )
    axis.text(
        end[0] + label_offset[0],
        end[1] + label_offset[1],
        label,
        color=color,
        fontsize=13,
        weight="bold",
    )


def main() -> None:
    parameters = animation_parameters()
    figure, axis = plt.subplots(figsize=(6.8, 6.8), dpi=110)

    def update(frame: int):
        amount = parameters[frame]
        matrix = (1.0 - amount) * np.eye(2) + amount * TARGET_MATRIX
        transformed_vector = matrix @ VECTOR

        axis.clear()
        axis.set_aspect("equal")
        axis.set_xlim(-2.4, 3.0)
        axis.set_ylim(-2.3, 3.0)
        axis.set_xticks(np.arange(-2, 4, 1))
        axis.set_yticks(np.arange(-2, 4, 1))
        axis.tick_params(labelsize=9, colors="#666666")
        axis.axhline(0.0, color="#555555", lw=1.0)
        axis.axvline(0.0, color="#555555", lw=1.0)

        # Draw the grid well beyond the visible axes so transformed line
        # segments reach every plot boundary without exposed endpoints.
        values = np.linspace(-4.0, 4.0, 160)
        for fixed_value in np.arange(-4.0, 4.1, 0.5):
            vertical = np.vstack((np.full_like(values, fixed_value), values))
            horizontal = np.vstack((values, np.full_like(values, fixed_value)))
            transformed_vertical = matrix @ vertical
            transformed_horizontal = matrix @ horizontal
            axis.plot(
                transformed_vertical[0],
                transformed_vertical[1],
                color="#4f81bd",
                alpha=0.42,
                lw=0.8,
            )
            axis.plot(
                transformed_horizontal[0],
                transformed_horizontal[1],
                color="#4f81bd",
                alpha=0.42,
                lw=0.8,
            )

        draw_arrow(axis, np.zeros(2), matrix[:, 0], "#2b6cb0", r"$A(t)[1,0]^T$")
        draw_arrow(
            axis,
            np.zeros(2),
            matrix[:, 1],
            "#2f855a",
            r"$A(t)[0,1]^T$",
            (-0.58, 0.08),
        )
        draw_arrow(
            axis,
            np.zeros(2),
            transformed_vector,
            "#c53030",
            r"$\boldsymbol{y}=A(t)\boldsymbol{x}$",
            (0.08, 0.08),
        )

        axis.plot(VECTOR[0], VECTOR[1], "o", color="#777777", ms=5)
        axis.text(
            VECTOR[0] - 0.60,
            VECTOR[1] - 0.30,
            r"input $\boldsymbol{x}$",
            color="#666666",
            fontsize=11,
        )
        axis.text(
            0.02,
            0.02,
            rf"$A(t)=(1-t)I+tA,\quad t={amount:.2f}$",
            transform=axis.transAxes,
            fontsize=11,
            bbox={"facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.9},
        )
        return []

    animation = FuncAnimation(
        figure,
        update,
        frames=len(parameters),
        interval=55,
        blit=False,
        repeat=True,
    )
    figure.subplots_adjust(left=0.10, right=0.97, bottom=0.10, top=0.97)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    animation.save(OUTPUT, writer=PillowWriter(fps=18), dpi=110)
    plt.close(figure)


if __name__ == "__main__":
    main()
