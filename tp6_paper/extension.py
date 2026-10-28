"""Sección 7 del TP 6: extensión bilateral y competencia entre dos plataformas.

Bilateral: usuarios θ ~ U[0,1] y comercios φ ~ U[0,1].
    usuarios:  U = θ·α_u·mᵉ − P_u   →  y = 1 − P_u/(α_u·mᵉ)
    comercios: V = φ·α_c·yᵉ − P_c   →  m = 1 − P_c/(α_c·yᵉ)
Competencia: dos billeteras A y B, U_i = θ·α·(y_iᵉ + β·y_jᵉ) − P_i.

Uso: python3 tp6_paper/extension.py  (imprime los resultados y guarda los gráficos 4 a 6)
"""
from math import sqrt
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np

OUT = Path(__file__).parent / "figuras"
OUT.mkdir(exist_ok=True)
GRIS, AZUL, ROJO = "#4d4d4d", "#2a72d5", "#c0504d"
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False})


def equilibrios(Pu, Pc, au=1.0, ac=1.0):
    """Equilibrios interiores (y, m) del modelo bilateral: alto y bajo (masa crítica)."""
    a, b = Pu / au, Pc / ac
    B = 1 + b - a
    d = B * B - 4 * b
    if d < 0:
        return None
    return [(y, 1 - b / y) for y in ((B + sqrt(d)) / 2, (B - sqrt(d)) / 2)]


def coma(ax):
    """Ejes con coma decimal, como en los gráficos 1 a 3."""
    fmt = matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}".replace(".", ","))
    ax.xaxis.set_major_formatter(fmt)
    ax.yaxis.set_major_formatter(fmt)


def titulo(fig, t, sub):
    fig.text(0.02, 0.97, t, fontsize=12, fontweight="bold", va="top")
    fig.text(0.02, 0.92, sub, fontsize=9.5, color="#666666", va="top")


# ---------------------------------------------------------------- resultados
print("== Bilateral simétrico (P_u = P_c = 0,16; α = 1) ==")
for y, m in equilibrios(0.16, 0.16):
    print(f"  y = {y:.3f}, m = {m:.3f}, √(ab)/(y·m) = {0.16 / (y * m):.2f}")

print("== Estructura de precios con precio total 0,32 ==")
for Pu in (0.16, 0.08, 0.04, 0.0):
    Pc = 0.32 - Pu
    (yH, mH), (yL, mL) = equilibrios(Pu, Pc)
    print(f"  P_u={Pu:.2f} P_c={Pc:.2f}  alto=({yH:.3f},{mH:.3f})  bajo=({yL:.3f},{mL:.3f})"
          f"  transacciones={yH * mH:.3f}  ingreso={Pu * yH + Pc * mH:.3f}")

print("== Plataforma monopolista (c = 0) ==")
for au, ac in ((1, 1), (1, 2)):
    best = None
    for Pu in np.linspace(0, 0.6, 601):
        for Pc in np.linspace(0, 1.2, 1201):
            e = equilibrios(Pu, Pc, au, ac) if Pc > 0 else None
            if not e:
                continue
            y, m = e[0]
            if 0 <= y <= 1 and 0 <= m <= 1 and (best is None or Pu * y + Pc * m > best[0]):
                best = (Pu * y + Pc * m, Pu, Pc, y, m)
    print(f"  α_u={au}, α_c={ac}: π={best[0]:.3f} P_u={best[1]:.3f} P_c={best[2]:.3f}"
          f" y={best[3]:.3f} m={best[4]:.3f}")

print("== Competencia: reparto simétrico y = (1 ± √(1 − 8P/(α(1+β))))/4 ==")
for beta in (0, 0.28, 0.5, 1):
    d = 1 - 8 * 0.16 / (1 + beta)
    print(f"  β={beta}: " + ("no existe" if d < 0 else
          f"cada una {(1 + sqrt(d)) / 4:.3f} (umbral {(1 - sqrt(d)) / 4:.3f})"))
print("== Precio máximo del entrante para atraer a θ = 1 (y_A = 0,8, y_Bᵉ = 0) ==")
for beta in (0, 0.25, 0.5, 0.75, 1):
    print(f"  β={beta}: P_B ≤ {0.16 - (1 - beta) * 0.8:+.2f}")

# ------------------------------------------- Gráfico 4: diagrama de fases bilateral
a = b = 0.16
f_u = lambda m: np.where(m > a, 1 - a / np.maximum(m, 1e-9), 0.0)   # respuesta de usuarios
f_c = lambda y: np.where(y > b, 1 - b / np.maximum(y, 1e-9), 0.0)   # respuesta de comercios


def destino(y, m, pasos=4000, dt=0.02):
    for _ in range(pasos):
        y, m = y + dt * (f_u(m) - y), m + dt * (f_c(y) - m)
    return y, m


g = np.linspace(0, 1, 161)
Y0, M0 = np.meshgrid(g, g)
YF, MF = destino(Y0.copy(), M0.copy())
alto = (YF + MF) > 1

fig, ax = plt.subplots(figsize=(6.4, 5.6))
fig.subplots_adjust(top=0.84, left=0.11, right=0.97, bottom=0.1)
ax.contourf(Y0, M0, alto.astype(float), levels=[-0.5, 0.5, 1.5],
            colors=["#f3d9d8", "#dbe8f8"])
s = np.linspace(0.001, 1, 400)
ax.plot(s, f_c(s), color=GRIS, lw=2, label="Comercios: m = 1 − P_c/(α_c·yᵉ)")
ax.plot(f_u(s), s, color=GRIS, lw=2, ls="--", label="Usuarios: y = 1 − P_u/(α_u·mᵉ)")
for y0, m0 in ((0.9, 0.12), (0.12, 0.9), (0.3, 0.25), (0.18, 0.2), (0.05, 0.5)):
    tray = [(y0, m0)]
    y, m = y0, m0
    for _ in range(400):
        y, m = y + 0.02 * (float(f_u(m)) - y), m + 0.02 * (float(f_c(y)) - m)
        tray.append((y, m))
    tray = np.array(tray)
    ax.plot(tray[:, 0], tray[:, 1], color=AZUL, lw=1, alpha=0.8)
    ax.plot(y0, m0, "o", color=AZUL, ms=3)
ax.plot([0, 0.8], [0, 0.8], "o", color="black", ms=7)
ax.plot(0.2, 0.2, "o", color="black", mfc="white", ms=7)
ax.annotate("Alto (0,8; 0,8)\nestable", (0.8, 0.8), xytext=(8, 6), textcoords="offset points")
ax.annotate("Masa crítica (0,2; 0,2)\ninestable", (0.2, 0.2), xytext=(8, -26), textcoords="offset points")
ax.text(0.03, 0.04, "La red colapsa", color=ROJO, fontsize=9)
ax.text(0.62, 0.95, "La red despega", color=AZUL, fontsize=9)
ax.set_xlabel("Fracción de usuarios y")
ax.set_ylabel("Fracción de comercios m")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.legend(loc="center right", fontsize=8.5, frameon=False)
coma(ax)
titulo(fig, "El huevo y la gallina: hace falta masa crítica en los dos lados",
       "P_u = P_c = 0,16; α_u = α_c = 1. Zona azul: converge al equilibrio alto; zona roja: a cero")
fig.savefig(OUT / "grafico4_bilateral_fases.png", dpi=200)

# --------------------------------------- Gráfico 5: la estructura de precios importa
Pus = np.linspace(0, 0.32, 161)
res = np.array([equilibrios(p, 0.32 - p)[0] for p in Pus])
fig, ax = plt.subplots(figsize=(6.4, 4.4))
fig.subplots_adjust(top=0.82, left=0.1, right=0.97, bottom=0.13)
ax.plot(Pus, res[:, 0], color=AZUL, lw=2, label="Usuarios y (equilibrio alto)")
ax.plot(Pus, res[:, 1], color=GRIS, lw=2, ls="--", label="Comercios m (equilibrio alto)")
ax.plot(Pus, res[:, 0] * res[:, 1], color=ROJO, lw=2, label="Transacciones y·m")
ax.axvline(0.16, color="#999999", lw=1, ls=":")
ax.text(0.162, 0.42, "Reparto\nsimétrico", fontsize=8.5, color="#666666")
ax.set_xlabel("Precio a usuarios P_u (el resto, 0,32 − P_u, lo pagan los comercios)")
ax.set_ylabel("Fracción / volumen")
ax.set_ylim(0.4, 1.02)
ax.set_xlim(0, 0.32)
ax.legend(frameon=False, fontsize=8.5, loc="lower left")
coma(ax)
titulo(fig, "Mismo precio total, distinto reparto: cambia la adopción",
       "Precio total P_u + P_c = 0,32; α_u = α_c = 1 (definición de mercado de dos lados)")
fig.savefig(OUT / "grafico5_estructura_precios.png", dpi=200)

# ------------------------------- Gráfico 6: ventaja del incumbente e interoperabilidad
betas = np.linspace(0, 1, 101)
fig, ax = plt.subplots(figsize=(6.4, 4.4))
fig.subplots_adjust(top=0.82, left=0.11, right=0.97, bottom=0.13)
ax.plot(betas, 0.16 - (1 - betas) * 0.8, color=AZUL, lw=2)
ax.axhline(0, color="#999999", lw=1)
ax.axhline(0.16, color=GRIS, lw=1, ls="--")
ax.text(0.01, 0.175, "Precio del incumbente P_A = 0,16", fontsize=8.5, color=GRIS)
for bb in (0, 0.5, 0.8):
    v = 0.16 - (1 - bb) * 0.8
    ax.plot(bb, v, "o", color=AZUL)
    ax.annotate(f"β = {bb:g}: P_B ≤ {v:+.2f}".replace(".", ",").replace("+0,00", "0"), (bb, v),
                xytext=(8, 4) if bb == 0 else (-30, -16) if bb == 0.8 else (8, -12),
                textcoords="offset points", fontsize=8.5)
ax.fill_between(betas, 0.16 - (1 - betas) * 0.8, 0, where=betas < 0.8,
                color="#f3d9d8", alpha=0.7)
ax.text(0.25, -0.1, "Subsidio necesario\npara entrar", color=ROJO, fontsize=9)
ax.set_xlabel("Grado de interoperabilidad β")
ax.set_ylabel("Precio máximo del entrante B")
ax.set_xlim(0, 1)
coma(ax)
titulo(fig, "La interoperabilidad elimina la ventaja de red del incumbente",
       "Incumbente con y_A = 0,8; entrante sin usuarios esperados; usuario más intensivo (θ = 1)")
fig.savefig(OUT / "grafico6_interoperabilidad.png", dpi=200)
print("Gráficos guardados en", OUT)
