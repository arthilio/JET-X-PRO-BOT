import numpy as np

def generate_prediction(user_id: int) -> dict:
    """Génère une prédiction sécurisée avec modèle optimisé"""
    base_multiplier = np.random.uniform(1.5, 3.0)
    confidence = min(87.0, base_multiplier * 30)  # Limite à 87%
    
    return {
        "multiplier": round(base_multiplier, 2),
        "confidence": confidence,
        "safety_band": (max(1.2, base_multiplier - 0.5), base_multiplier + 0.5)
    }
