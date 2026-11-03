"""Gráfico 2 del paper final: subsidio que necesita un rival para que cada usuario se cambie.

Incumbente A con y_A = 0,8; rival B sin usuarios esperados (y_Bᵉ = 0).
El usuario θ se pasa a B si el subsidio s cubre la red que pierde: s(θ) = θ·α·(1 − β)·(y_A − y_Bᵉ).
Uso: python3 tp6_paper/paper_final/grafico_subsidio.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np

ALPHA, Y_A = 1.0, 0.8
OUT = Path(__file__).parent / "grafico2_subsidio_cambio.png"
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False})

theta = np.linspace(0.2, 1, 200)
fig, ax = plt.subplots(figsize=(6.4, 4.2))
fig.subplots_adjust(top=0.82, left=0.11, right=0.97, bottom=0.13)
for beta, color, ls in ((0, "#c0504d", "-"), (0.5, "#4d4d4d", "--"), (1, "#2a72d5", "-")):
    ax.plot(theta, theta * ALPHA * (1 - beta) * Y_A, color=color, lw=2, ls=ls,
            label=f"β = {beta:g}".replace(".", ","))
ax.plot(0.2, 0.16, "o", color="black")
ax.annotate("Consumidor marginal (θ* = 0,2):\nB debe cubrir todo su costo de adopción",
            (0.2, 0.16), xytext=(0.5, 0.08), textcoords="data", fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color="#999999"))
ax.plot(1, 0.8, "o", color="#c0504d")
ax.annotate("Usuario más intensivo: 0,8", (1, 0.8), xytext=(-135, -4),
            textcoords="offset points", fontsize=8.5)
ax.set_xlabel("Intensidad de uso del adoptante θ (adoptan los θ ≥ 0,2)")
ax.set_ylabel("Subsidio necesario s(θ)")
ax.set_xlim(0.18, 1.02)
ax.set_ylim(-0.03, 0.9)
ax.legend(title="Interoperabilidad", frameon=False, fontsize=8.5, title_fontsize=8.5, loc="upper left")
fmt = matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}".replace(".", ","))
ax.xaxis.set_major_formatter(fmt)
ax.yaxis.set_major_formatter(fmt)
fig.text(0.02, 0.97, "Sin interoperabilidad, solo se cambia de billetera con subsidios",
         fontsize=12, fontweight="bold", va="top")
fig.text(0.02, 0.92, "Incumbente con y_A = 0,8; rival sin usuarios esperados; α = 1",
         fontsize=9.5, color="#666666", va="top")
fig.savefig(OUT, dpi=200)
print("Gráfico guardado en", OUT)
