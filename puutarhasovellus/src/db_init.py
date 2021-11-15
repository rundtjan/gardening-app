from db_connection import get_db_connection

def drop_all(conn):
    cursor = conn.cursor()

    cursor.execute('''
        drop table if exists users
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
        insert into users (username, password, admin)
        values ('test', 'pass', false)
    ''')

    conn.commit()

def init_db():
    conn = get_db_connection()
    drop_all(conn)
    create_tables(conn)

if __name__ == "__main__":
    init_db()
