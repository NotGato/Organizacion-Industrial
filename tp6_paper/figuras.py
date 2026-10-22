"""Figuras del TP 6: efectos de red y masa crítica en billeteras virtuales.

Modelo: U = theta * alpha * n^e - P, theta ~ U[0,1], alpha = 1, P = 0.16.
Uso: python3 tp6_paper/figuras.py  (guarda los PNG en tp6_paper/figuras/)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ALPHA = 1.0
P = 0.16
OUT = Path(__file__).parent / "figuras"
OUT.mkdir(exist_ok=True)

n_L = (1 - np.sqrt(1 - 4 * P / ALPHA)) / 2
n_H = (1 + np.sqrt(1 - 4 * P / ALPHA)) / 2


def demanda(ne, p=P, alpha=ALPHA):
    """Fracción que adopta dada la expectativa ne: D = 1 - p/(alpha*ne), acotada a [0,1]."""
    ne = np.asarray(ne, dtype=float)
    with np.errstate(divide="ignore"):
        d = 1 - p / (alpha * ne)
    return np.clip(np.where(ne > 0, d, 0.0), 0, 1)


plt.rcParams.update({"font.family": "serif", "font.size": 11})

# Figura 1: demanda de red en EEA p(n) = alpha n (1-n) y precio P
n = np.linspace(0, 1, 400)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(n, ALPHA * n * (1 - n), color="#1f4e79", lw=2, label=r"$p(n)=\alpha\,n(1-n)$")
ax.axhline(P, color="#c0504d", ls="--", lw=1.5, label=r"$P=0{,}16$")
for x, lab in [(0, "0"), (n_L, r"$n_L=0{,}2$"), (n_H, r"$n_H=0{,}8$")]:
    ax.plot(x, P if x else 0, "o", color="black", mfc="white" if x == n_L else "black")
    ax.annotate(lab, (x, P if x else 0), textcoords="offset points",
                xytext=(-62, 6) if x == n_L else (4, 8))
ax.annotate("", xy=(0.55, P + 0.012), xytext=(0.35, P + 0.012),
            arrowprops=dict(arrowstyle="->", color="gray"))
ax.annotate("", xy=(0.05, P - 0.02), xytext=(0.17, P - 0.02),
            arrowprops=dict(arrowstyle="->", color="gray"))
ax.annotate("", xy=(0.82, P - 0.02), xytext=(0.95, P - 0.02),
            arrowprops=dict(arrowstyle="->", color="gray"))
ax.set_xlabel("Fracción de adoptantes $n$")
ax.set_ylabel("Precio / costo de adopción")
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.28)
ax.legend(loc="upper right", frameon=False)
fig.tight_layout()
fig.savefig(OUT / "fig1_demanda_red.png", dpi=200)

# Figura 2: función de reacción de expectativas D(n^e) vs. recta de 45°
fig, ax = plt.subplots(figsize=(5, 5))
ne = np.linspace(0.001, 1, 400)
ax.plot(ne, demanda(ne), color="#1f4e79", lw=2, label=r"$D(n^e)=1-P/(\alpha n^e)$")
ax.plot([0, 1], [0, 1], color="gray", lw=1, ls=":", label=r"$n=n^e$ (45°)")
ax.plot([0, n_L, n_H], [0, n_L, n_H], "o", color="black")
ax.plot([n_L], [n_L], "o", color="black", mfc="white")
ax.annotate("Inestable\n(masa crítica)", (n_L, n_L), textcoords="offset points", xytext=(8, -28))
ax.annotate("Estable", (n_H, n_H), textcoords="offset points", xytext=(-55, 8))
ax.set_xlabel("Tamaño esperado de la red $n^e$")
ax.set_ylabel("Adopción efectiva $D(n^e)$")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.legend(loc="upper left", frameon=False)
fig.tight_layout()
fig.savefig(OUT / "fig2_expectativas.png", dpi=200)

# Figura 3: dinámica con expectativas adaptativas n_{t+1} = D(n_t)
fig, ax = plt.subplots(figsize=(6.5, 4))
for n0 in (0.15, 0.19, 0.21, 0.25, 0.5, 1.0):
    path = [n0]
    for _ in range(14):
        path.append(float(demanda(path[-1])))
    ax.plot(range(len(path)), path, marker=".", lw=1.3, label=f"$n_0={n0}$".replace(".", "{,}"))
ax.axhline(n_L, color="#c0504d", ls="--", lw=1)
ax.axhline(n_H, color="#1f4e79", ls="--", lw=1)
ax.set_xlabel("Período $t$")
ax.set_ylabel("Adopción $n_t$")
ax.set_ylim(-0.02, 1.02)
ax.legend(ncol=3, fontsize=9, frameon=False, loc="center right")
fig.tight_layout()
fig.savefig(OUT / "fig3_dinamica.png", dpi=200)

# Figura 4: masa crítica en función de P para distintos alpha (interoperabilidad)
fig, ax = plt.subplots(figsize=(6.5, 4))
for alpha in (0.8, 1.0, 1.5, 2.0):
    p = np.linspace(0, alpha / 4, 300)
    ax.plot(p, (1 - np.sqrt(1 - 4 * p / alpha)) / 2, lw=2, label=rf"$\alpha={alpha}$".replace(".", "{,}"))
ax.axvline(P, color="gray", ls=":", lw=1)
ax.set_xlabel("Precio / costo de adopción $P$")
ax.set_ylabel("Masa crítica $n_L$")
ax.set_xlim(0, 0.5)
ax.set_ylim(0, 0.52)
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(OUT / "fig4_masa_critica.png", dpi=200)

print(f"n_L = {n_L:.4f}, n_H = {n_H:.4f}; figuras en {OUT}")
