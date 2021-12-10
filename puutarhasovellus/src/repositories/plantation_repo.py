import datetime
from entities.plantation import Plantation
from db_connection import get_db_connection
from functions.functions import timestamp_from_date

def row_to_plantation(row):
    if row[6] == "":
        return Plantation(row[1], row[2], toDate(row[3]), row[4], row[5], row[6], row[7], row[0])
    return Plantation(row[1], row[2], toDate(row[3]), row[4], row[5], toDate(row[6]), row[7], row[0])

def toDate(timestamp):
    if timestamp == -1:
        return None
    return datetime.datetime.fromtimestamp(timestamp)

def toTimestamp(datestring):
    timestring = "%m/%d/%Y"
    date = datetime.datetime.strptime(datestring, timestring)
    return timestamp_from_date(date)

def getYearTimestamps(year):
    start = toTimestamp("1/1/" + str(year))
    end = toTimestamp("12/31/" + str(year))
    return {'start':start,'end':end}

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

    def get_by_user_and_year(self, user, year):

        year = getYearTimestamps(year)    

        cursor = self._conn.cursor()

        cursor.execute(
            'select * from plantations WHERE username=? AND planting_date>? AND planting_date<? ORDER BY planting_date DESC', (user.username,year['start'],year['end'])
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
