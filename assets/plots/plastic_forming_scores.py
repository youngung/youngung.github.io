"""Render the score distribution directly from the published Markdown table."""
from pathlib import Path
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "_news/announcement_06.md"
OUTPUT = ROOT / "assets/img/news/plastic_forming_scores_2026.png"
scores = np.array([float(score) for score in re.findall(
    r"^\|\s*\d{8}\s*\|\s*([\d.]+)\s*\|", SOURCE.read_text(), re.M
)])
if not len(scores):
    raise ValueError("No scores found in the Markdown table")
for family in ("AppleGothic", "NanumGothic", "Noto Sans CJK KR", "Malgun Gothic"):
    if any(font.name == family for font in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = family
        break
else:
    raise RuntimeError("Install a Korean font: NanumGothic or Noto Sans CJK KR")
plt.rcParams.update({"font.size": 12, "axes.unicode_minus": False})
mean = scores.mean()
bins = np.arange(np.floor(scores.min() / 10) * 10,
                 np.floor(scores.max() / 10) * 10 + 11, 10)
fig, ax = plt.subplots(figsize=(9, 5.5), layout="constrained")
counts, edges, bars = ax.hist(scores, bins=bins, color="#42779d",
                            edgecolor="white", linewidth=1.5)
ax.bar_label(bars, labels=[str(int(n)) if n else "" for n in counts], padding=5)
ax.axvline(mean, color="#bd4938", linewidth=2.2, linestyle="--",
           label=f"평균 {mean:.2f}점")
ax.set(title=f"소성가공 중간고사 성적 분포 (총 {len(scores)}명)",
       xlabel="점수 (점)", ylabel="학생 수 (명)",
       xticks=bins, yticks=np.arange(0, counts.max() + 2),
       xlim=(bins[0], bins[-1]), ylim=(0, counts.max() + 1.5))
ax.set_axisbelow(True)
ax.grid(axis="y", alpha=0.2)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="upper left", frameon=False)
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT, dpi=180, facecolor="white")
plt.close(fig)
print(f"n={len(scores)}, sum={scores.sum():.1f}, mean={mean:.8f}")
print(f"bin counts={counts.astype(int).tolist()}")
