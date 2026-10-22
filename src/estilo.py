"""Configuración común de gráficos y rutas para los notebooks del equipo 8."""
from pathlib import Path
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "data" / "raw" / "vgsales.csv"
LIMPIO = RAIZ / "data" / "processed" / "vgsales_limpio.csv"
IMG = RAIZ / "img"
MODELO = RAIZ / "dashboard" / "modelo"

# Paleta categórica (mismo orden en todo el proyecto y en el tema de Power BI)
AZUL, NARANJA, AQUA, AMARILLO = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
GRIS = "#898781"
COLOR_REGION = {"Norteamérica": AZUL, "Europa": NARANJA, "Japón": AQUA, "Otros": AMARILLO}

REGIONES = {"NA_Sales": "Norteamérica", "EU_Sales": "Europa",
            "JP_Sales": "Japón", "Other_Sales": "Otros"}

GENERO_ES = {"Action": "Acción", "Adventure": "Aventura", "Fighting": "Pelea",
             "Misc": "Misceláneo", "Platform": "Plataformas", "Puzzle": "Puzle",
             "Racing": "Carreras", "Role-Playing": "Rol (RPG)", "Shooter": "Disparos",
             "Simulation": "Simulación", "Sports": "Deportes", "Strategy": "Estrategia"}


def configurar():
    plt.rcParams.update({
        "figure.dpi": 110, "savefig.dpi": 150, "savefig.bbox": "tight",
        "figure.facecolor": "#fcfcfb", "axes.facecolor": "#fcfcfb",
        "axes.edgecolor": "#c3c2b7", "axes.labelcolor": "#52514e",
        "axes.titleweight": "bold", "axes.titlesize": 12, "axes.titlelocation": "left",
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": "#e1e0d9", "grid.linewidth": 0.6,
        "xtick.color": "#52514e", "ytick.color": "#52514e",
        "font.size": 10, "legend.frameon": False, "axes.axisbelow": True,
    })
    IMG.mkdir(exist_ok=True)


def guardar(fig, nombre):
    fig.savefig(IMG / f"{nombre}.png")
