from entities.user import User
from db_connection import get_db_connection

class UserRepo:
    '''Class that handles db-functions concerning users.
    '''

    def __init__(self, conn):
        '''Constructor.

        Args:
            conn: databaseconnection
        '''

        self._conn = conn

    def create(self, user):
        '''Function for adding a new user.

        Args:
            user: user to add as user-object.

        Returns:
            At the moment returns None.
        '''

        cursor = self._conn.cursor()

        cursor.execute(
            'insert into users (username, password, admin) values (?,?,?)',
            (user.username, user.password, user.admin)
        )

        self._conn.commit()

    def get_all(self):
        '''Function for getting all users.

        Returns all users'''

        cursor = self._conn.cursor()

        cursor.execute(
            'select * from users'
        )

        rows = cursor.fetchall()

        return list(rows)

    def get_user(self, username):
        '''Function for finding a user.

        Args:
            username: String.

        Returns:
            Returns a user-object or None.
        '''

        cursor = self._conn.cursor()

        cursor.execute(
            'select * from users where username=:username',
            {'username': username}
        )

        row = cursor.fetchone()

        if row:
            return User(row[0], row[1], row[2])

        return None

    def delete_all(self):
        '''Function to delete all db-entries.
        '''

        cursor = self._conn.cursor()

        cursor.execute('delete from users')

        self._conn.commit()

user_repo = UserRepo(get_db_connection())
