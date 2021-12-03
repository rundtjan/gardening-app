import datetime
from entities.plantation import Plantation
from db_connection import get_db_connection

def row_to_plantation(row):
    return Plantation(row[1], row[2], toDate(row[3]), row[4], row[5], row[6], row[7], row[0])

def toDate(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

class PlantationRepo:
    def __init__(self, conn):
        self._conn = conn

    def get_by_user(self, user):
        
        cursor = self._conn.cursor()

        cursor.execute(
            'select * from plantations WHERE username=? ORDER BY planting_date DESC', (user.username,)
        )

        rows = cursor.fetchall()
        
        return list(map(row_to_plantation, rows))

    def get_by_id(self, plant_id):

        cursor = self._conn.cursor()

        cursor.execute(
            'select * from plantations WHERE plant_id=?', (plant_id,)
        )

        row = cursor.fetchone()

        return row_to_plantation(row)

    def create(self, plantation):
        cursor = self._conn.cursor()

        cursor.execute(
            'insert into plantations (username, plant, planting_date, amount_planted, info, yield_date, amount_yield) values (?,?,?,?,?,?,?)',
            plantation.get_tuple()
        )

        self._conn.commit()

    def update(self, plantation):
        cursor = self._conn.cursor()

        cursor.execute(
            'UPDATE plantations SET username=?, plant=?, planting_date=?, amount_planted=?, info=?, yield_date=?, amount_yield=? WHERE plant_id=?',
            plantation.get_tuple() + (plantation.get_id(),)
        )

        self._conn.commit()

    def delete_all(self, plantation):#for tests
        cursor = self._conn.cursor()

        cursor.execute(
            'DELETE from plantations;'
        )

        self._conn.commit()


plantation_repo = PlantationRepo(get_db_connection())
