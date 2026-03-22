import pytest
import psycopg2

def test_flask_app_exists():
    """Simple unit test for the Python app"""
    assert True  # In a real app you'd test routes

def test_postgres_connection():
    """Integration test that uses the Postgres sidecar"""
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="testuser",
        password="testpass",
        dbname="testdb"
    )
    cur = conn.cursor()
    cur.execute("SELECT 1")
    assert cur.fetchone()[0] == 1
    conn.close()