
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
            (user,username, user.password, user.admin)
        )

        self._conn.commit()

        return None
    
    def delete_all(self, user):
        '''Function to delete all db-entries.
        '''

        cursor = self._comm.cursor()

        cursor.execute('delete from users')

        self._comm.commit()