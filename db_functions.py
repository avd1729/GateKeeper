from db.sqlite_manager import SQLiteManager

manager = SQLiteManager()
conn = manager.get_conn()
cur = conn.cursor()

def add_api(api_key, user_id):
    cur.execute("""
        INSERT INTO API_KEYS (key, user_id) VALUES (?, ?)
    """, (api_key, user_id))