from datetime import datetime, timedelta
from utils.database import Database

class RiskManager:
    DAILY_LOSS_LIMIT = 15000  # 15 000 FCFA
    
    def __init__(self):
        self.db = Database()

    def check_risk(self, user_id: int) -> bool:
        """Vérifie si l'utilisateur dépasse les limites de risque"""
        daily_loss = self.db.get_daily_loss(user_id)
        return daily_loss < self.DAILY_LOSS_LIMIT
