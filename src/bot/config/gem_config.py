from datetime import timedelta
from dataclasses import dataclass

@dataclass
class GemTier:
    name: str
    level: int
    usd_price: float
    eur_price: float
    duration: timedelta
    color_code: str
    alt_payments: list

TIERS = [
    GemTier("Saphir", 1, 11.99, 12.51, timedelta(days=11), "#0F52BA", ["Crypto", "Virement"]),
    GemTier("Rubis", 2, 29.99, 31.25, timedelta(days=14), "#E0115F", ["Western Union"]),
    GemTier("Émeraude", 3, 49.99, 52.10, timedelta(days=16), "#50C878", []),
    GemTier("Alexandrite", 4, 79.99, 83.40, timedelta(days=18), "#598C7B", ["Chèque"]),
    GemTier("Opale Noire", 5, 129.99, 135.50, timedelta(days=19), "#0B1616", ["Portefeuille Électronique"]),
    GemTier("Jadéite Impériale", 6, 199.99, 208.45, timedelta(days=20), "#00A86B", ["Carte Prépayée"]),
    GemTier("Diamant Rouge", 7, 299.99, 312.75, timedelta(days=20), "#E25858", ["Métaux Précieux"])
]
