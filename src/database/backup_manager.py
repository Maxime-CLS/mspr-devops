import os
import shutil
from datetime import datetime
from pathlib import Path

DB_PATH = os.getenv("DB_PATH", "/app/phc.db")
BACKUP_DIR = Path("/app/backups")

def ensure_backup_dir_exists():
    """Crée le dossier de backup s'il n'existe pas."""
    BACKUP_DIR.mkdir(exist_ok=True)

def backup_database():
    """Sauvegarde la base de données actuelle."""
    ensure_backup_dir_exists()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"phc_backup_{timestamp}.db"
    shutil.copy2(DB_PATH, backup_path)
    print(f"Backup créé : {backup_path}")

def restore_latest_backup():
    """Restaure la dernière sauvegarde disponible."""
    ensure_backup_dir_exists()
    backups = list(BACKUP_DIR.glob("phc_backup_*.db"))
    if not backups:
        print("Aucun backup disponible.")
        return False
    latest_backup = max(backups, key=os.path.getctime)
    shutil.copy2(latest_backup, DB_PATH)
    print(f"Base de données restaurée depuis : {latest_backup}")
    return True

def auto_backup_on_exit():
    """Enregistre un hook pour sauvegarder à la fermeture du programme."""
    import atexit
    atexit.register(backup_database)

def backup_database_periodically(interval_minutes=60):
    """Sauvegarde périodiquement la base de données."""
    import time
    import threading
    def backup_loop():
        while True:
            time.sleep(interval_minutes * 60)
            backup_database()
    thread = threading.Thread(target=backup_loop, daemon=True)
    thread.start()