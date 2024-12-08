import psycopg2

def test_connection():
    conn = psycopg2.connect(
        dbname="mockdb",
        user="user",
        password="password",
        host="mock-database",
        port="5432"
    )
    assert True