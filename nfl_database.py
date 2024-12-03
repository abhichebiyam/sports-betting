import sqlite3

class NFL_Database:

    def __init__(self):
        pass

    def create_tables(self):
        # Connect to SQLite database (or create one if it doesn't exist)
        conn = sqlite3.connect("matchups.db")
        cursor = conn.cursor()

        # Create Teams table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE 
        )
        """)

        # Create Matchups table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Matchups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team1_id INTEGER NOT NULL,
            team2_id INTEGER NOT NULL,
            odds_team1 REAL,
            odds_team2 REAL,
            FOREIGN KEY (team1_id) REFERENCES Teams(id),
            FOREIGN KEY (team2_id) REFERENCES Teams(id)
        )
        """)

        # Commit changes and close connection
        conn.commit()
        conn.close()
    
    def insert_team(conn, team_name):
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO Teams (name) VALUES (?)", (team_name,))
        conn.commit()

