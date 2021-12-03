from db_connection import get_db_connection

def drop_all(conn):
    cursor = conn.cursor()

    cursor.execute('''
        drop table if exists users
    ''')

    cursor.execute('''
            drop table if exists plantations
    ''')

    conn.commit()

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''
        create table users(
            username text primary key,
            password text,
            admin boolean
        );
    ''')

    cursor.execute('''
        create table plantations(
            plant_id INTEGER PRIMARY KEY,
            username text,
            plant text,
            planting_date int,
            amount_planted text,
            info text,
            yield_date int,
            amount_yield text
        );
    ''')

    conn.commit()

def init_db():
    conn = get_db_connection()
    drop_all(conn)
    create_tables(conn)

if __name__ == "__main__":
    init_db()
