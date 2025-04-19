import mysql.connector
import pandas as pd
from sqlalchemy import create_engine


def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root123', 
        database='IMDB'
    )

def get_engine():
    return create_engine("mysql+mysqlconnector://root:root123@localhost/IMDB")

# Load CSV data into MySQL
def create_and_load_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            genres TEXT,
            runtime FLOAT,
            release_date DATE,
            vote_average FLOAT,
            vote_count INT,
            revenue BIGINT,
            budget BIGINT
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM movies")
    if cursor.fetchone()[0] == 0:
        df = pd.read_csv('data/tmdb_5000_movies.csv')
        df = df[['title', 'genres', 'runtime', 'release_date', 'vote_average', 'vote_count', 'revenue', 'budget']]
        df = df.dropna()
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
        df = df.dropna()

        for _, row in df.iterrows():
                release_date = row['release_date'].date() if pd.notnull(row['release_date']) else None
                cursor.execute("""
        INSERT INTO movies (title, genres, runtime, release_date, vote_average, vote_count, revenue, budget)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['title'], row['genres'], row['runtime'], release_date,
        row['vote_average'], row['vote_count'], row['revenue'], row['budget']
    ))

        conn.commit()
    conn.close()

# CRUD operations
def view_all_movies():
    engine = get_engine()
    return pd.read_sql("SELECT * FROM movies", con=engine)

def search_movie_by_name(name):
    engine = get_engine()
    return pd.read_sql("SELECT * FROM movies WHERE LOWER(title) LIKE %s", con=engine, params=(f"%{name.lower()}%",))

def delete_movie_by_title(title):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE LOWER(title) = %s", (title.lower(),))
    conn.commit()
    conn.close()
