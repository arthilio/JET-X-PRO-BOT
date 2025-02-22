import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, connection_str: str):
        self.conn = psycopg2.connect(connection_str)
        
    def create_user(self, user_id: int):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (telegram_id, balance, risk_level) 
                VALUES (%s, 0.00, 1)
                ON CONFLICT DO NOTHING
            """, (user_id,))
        self.conn.commit()
