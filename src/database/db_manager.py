from sqlalchemy import create_engine, text
import pandas as pd
import os

# Chemin local pour SQLite
DB_PATH = os.getenv("DB_PATH", "phc.db")
engine = create_engine(f"sqlite:///{DB_PATH}")

def get_workouts():
    """Récupère tous les workouts depuis la base de données."""
    return pd.read_sql("SELECT * FROM workouts", engine)

def get_records():
    """Récupère tous les records depuis la base de données."""
    return pd.read_sql("SELECT * FROM records", engine)

def add_workout(data: dict):
    """Ajoute un workout à la base de données."""
    with engine.connect() as conn:
        conn.execute(
            text("""
            INSERT INTO workouts (user_id, type, duration, calories, date)
            VALUES (:user_id, :type, :duration, :calories, :date)
            """),
            data
        )
        conn.commit()

def add_record(data: dict):
    """Ajoute un record à la base de données."""
    with engine.connect() as conn:
        conn.execute(
            text("""
            INSERT INTO records (user_id, type, value, unit, date)
            VALUES (:user_id, :type, :value, :unit, :date)
            """),
            data
        )
        conn.commit()