import sqlite3
from datetime import datetime

# Fonction pour se connecter à la base de données SQLite
def connect_db():
    conn = sqlite3.connect('users.db')
    return conn

# Fonction pour initialiser la base de données
def init_db():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        telegram_id TEXT NOT NULL,
        start_date TEXT NOT NULL,
        coupons_left INTEGER NOT NULL,
        total_days INTEGER NOT NULL,
        payment_status TEXT NOT NULL DEFAULT 'pending'  -- Statut de paiement
    )''')
    conn.commit()
    conn.close()

# Fonction pour enregistrer un utilisateur
def add_user(telegram_id):
    conn = connect_db()
    c = conn.cursor()
    
    # Ajouter un utilisateur avec 10 coupons gratuits
    today = datetime.today().date().isoformat()
    c.execute('''
    INSERT INTO users (telegram_id, start_date, coupons_left, total_days)
    VALUES (?, ?, ?, ?)
    ''', (telegram_id, today, 10, 0))
    
    conn.commit()
    conn.close()

# Fonction pour obtenir les informations de l'utilisateur
def get_user(telegram_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE telegram_id = ?', (telegram_id,))
    user = c.fetchone()
    conn.close()
    return user

# Fonction pour mettre à jour les coupons d'un utilisateur
def update_coupons(telegram_id, coupons_left):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
    UPDATE users
    SET coupons_left = ?
    WHERE telegram_id = ?
    ''', (coupons_left, telegram_id))
    
    conn.commit()
    conn.close()

# Fonction pour valider le paiement manuellement
def validate_payment(telegram_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
    UPDATE users
    SET payment_status = 'validated'
    WHERE telegram_id = ?
    ''', (telegram_id,))
    
    conn.commit()
    conn.close()

# Fonction pour vérifier l'éligibilité aux coupons gratuits ou payants
def check_coupon_eligibility(telegram_id):
    user = get_user(telegram_id)
    
    if user is None:
        # Si l'utilisateur n'existe pas, l'ajouter avec 10 coupons gratuits
        add_user(telegram_id)
        return True, 10  # Nouveau utilisateur, coupons gratuits
    
    start_date = user[2]
    coupons_left = user[3]
    total_days = user[4]
    payment_status = user[5]
    
    # Si l'utilisateur est encore dans les 3 jours gratuits
    days_since_start = (datetime.today() - datetime.fromisoformat(start_date)).days
    if days_since_start < 3:
        return True, coupons_left
    else:
        # Les coupons sont payants après 3 jours
        return False, payment_status, coupons_left
