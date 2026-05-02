import sqlite3
import os
from sqlalchemy import create_engine, text

DB_PATH = os.getenv("DB_PATH", "/app/phc.db")

def create_db():
    engine = create_engine(f"sqlite:///{DB_PATH}")

    # Créer les tables si elles n'existent pas
    with engine.connect() as conn:
        # Table workouts
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            duration REAL,
            calories REAL,
            date TEXT
        )
        """))

        # Table records
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            value REAL,
            unit TEXT,
            date TEXT
        )
        """))

        # Table users
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            name TEXT,
            password TEXT NOT NULL,
            email TEXT UNIQUE,
            role TEXT DEFAULT 'user'
        )
        """))

        # Ajouter un utilisateur admin par défaut (mot de passe: "admin")
        conn.execute(text("""
        INSERT OR IGNORE INTO users (username, name, password, email, role)
        VALUES ('admin', 'Administrateur', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW', 'admin@example.com', 'admin')
        """))

    print(f"✅ Base de données créée avec succès à {DB_PATH}")

if __name__ == "__main__":
    create_db()