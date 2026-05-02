import bcrypt
import sqlite3
from sqlalchemy import create_engine, text
import os

DB_PATH = os.getenv("DB_PATH", "/app/phc.db")
engine = create_engine(f"sqlite:///{DB_PATH}")

def hash_password(password: str) -> str:
    """Hache un mot de passe avec bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(stored_password: str, provided_password: str) -> bool:
    """Vérifie un mot de passe haché."""
    return bcrypt.checkpw(provided_password.encode(), stored_password.encode())

def get_user_by_username(username: str):
    """Récupère un utilisateur depuis la base de données."""
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users WHERE username = :username"), {"username": username})
        return result.mappings().first()

def add_user(username: str, name: str, password: str, email: str) -> bool:
    """Ajoute un nouvel utilisateur à la base de données."""
    hashed_password = hash_password(password)
    try:
        with engine.connect() as conn:
            conn.execute(
                text("""
                INSERT INTO users (username, name, password, email)
                VALUES (:username, :name, :password, :email)
                """),
                {"username": username, "name": name, "password": hashed_password, "email": email}
            )
            conn.commit()
            return True
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
        return False

def authenticate(username: str, password: str) -> bool:
    """Authentifie un utilisateur."""
    user = get_user_by_username(username)
    if user and verify_password(user["password"], password):
        return True
    return False