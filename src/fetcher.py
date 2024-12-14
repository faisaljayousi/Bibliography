import sqlite3 as sq


class ReferenceFetcher:
    def __init__(self, db_path="references.db"):
        self.db_path = db_path

    def fetch_references(self):
        """Fetch references from the SQLite database."""
        with sq.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT title, authors, topics, type, language, notes
                FROM references_tab
                """
            )
            return cursor.fetchall(), [desc[0] for desc in cursor.description]
