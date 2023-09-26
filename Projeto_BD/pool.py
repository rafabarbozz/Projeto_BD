import psycopg_pool

DB_CONFIG = "dbname=projetoBD user=postgres password=12345"

pool = psycopg_pool.ConnectionPool(conninfo=DB_CONFIG)