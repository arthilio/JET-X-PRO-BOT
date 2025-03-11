from dataclasses import dataclass
from datetime import timedelta

@dataclass
class GemPlan:
    name: str
    level: int
    price_usd: float
    price_eur: float
    duration: timedelta
    color_hex: str
    alternative_payments: list

PLANS = [
    GemPlan(
        name="Saphir",
        level=1,
        price_usd=11.99,
        price_eur=12.51,
        duration=timedelta(days=11),
        color_hex="#0F52BA",
        alternative_payments=["Virement Bancaire", "Crypto"]
    ),
    GemPlan(
        name="Rubis",
        level=2,
        price_usd=29.99,
        price_eur=31.25,
        duration=timedelta(days=14),
        color_hex="#E0115F",
        alternative_payments=["Western Union"]
    ),
    # ... Ajouter les 5 autres niveaux selon le même modèle
]
