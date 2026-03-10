import sqlite3


class SalesAnalyzer:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_connection(self):
        return sqlite3.connect(self.db_path)

    def total_sales(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(total_amount) FROM sales")
        result = cursor.fetchone()[0]
        conn.close()
        return result

    def sales_by_region(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT region, SUM(total_amount)
            FROM sales
            GROUP BY region
            """
        )
        results = cursor.fetchall()
        conn.close()
        return results

    def best_selling_product(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT product, SUM(quantity)
            FROM sales
            GROUP BY product
            ORDER BY SUM(quantity) DESC
            LIMIT 1
            """
        )
        result = cursor.fetchone()
        conn.close()
        return result

    def monthly_sales(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT strftime('%Y-%m', order_date), SUM(total_amount)
            FROM sales
            GROUP BY strftime('%Y-%m', order_date)
            ORDER BY strftime('%Y-%m', order_date)
            """
        )
        results = cursor.fetchall()
        conn.close()
        return results
