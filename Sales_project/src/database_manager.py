import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        conn = self.create_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sales (
                order_id INTEGER PRIMARY KEY,
                order_date TEXT,
                customer_name TEXT,
                product TEXT,
                category TEXT,
                region TEXT,
                quantity INTEGER,
                unit_price REAL,
                total_amount REAL,
                payment_mode TEXT
            )
            """
        )

        conn.commit()
        conn.close()

    def insert_data(self, dataframe):
        conn = self.create_connection()
        dataframe.to_sql("sales", conn, if_exists="replace", index=False)
        conn.close()

    def fetch_all(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sales")
        rows = cursor.fetchall()
        conn.close()
        return rows
