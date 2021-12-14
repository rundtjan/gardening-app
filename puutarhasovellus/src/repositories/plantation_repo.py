import datetime
from entities.plantation import Plantation
from db_connection import get_db_connection
from functions.functions import timestamp_from_date


def row_to_plantation(row):
    """A function that turns rows of db-data to plantation-objects

    Args:
        row: row from the sqlite-database.

    Returns:
        plantation-object.
    """
    if row[6] == "":
        return Plantation(
            row[1], row[2], to_date(row[3]), row[4], row[5], row[6], row[7], row[0]
        )
    return Plantation(
        row[1], row[2], to_date(row[3]), row[4], row[5], to_date(row[6]), row[7], row[0]
    )


def to_date(timestamp):
    """Method to turn a timestamp into a date.

    Args:
        timestamp: int, unix-timestamp.

    Returns:
        date.
    """
    if timestamp == -1:
        return None
    return datetime.datetime.fromtimestamp(timestamp)


def to_timestamp(datestring):
    """Method to turn a datestring into a unix timestamp.

    Args:
        datestring: a string describing a date dd/mm/yyyy

    Returns:
        A unix timestamp as an int.
    """
    timestring = "%m/%d/%Y"
    date = datetime.datetime.strptime(datestring, timestring)
    return timestamp_from_date(date)


def get_year_timestamps(year):
    """A method that creates timestamps for the start and end of a year.

    Args:
        year: int, the year to get the timestamps for.

    Returns:
        A dict containing a timestamp for both the start and end of the year.
    """
    start = to_timestamp("1/1/" + str(year))
    end = to_timestamp("12/31/" + str(year))
    return {"start": start, "end": end}


class PlantationRepo:
    """A class that handles the db-operations for the plantations."""

    def __init__(self, conn):
        """The constructor for the class.

        Args:
            conn: a connection to a sqlite-db.
        """
        self._conn = conn

    def get_by_user(self, user):
        """A method that gets plantations created by a certain user.

        Args:
            user: user-object to get the plantations for.

        Returns:
            A list of plantation-objects.
        """

        cursor = self._conn.cursor()

        cursor.execute(
            "select * from plantations WHERE username=? ORDER BY planting_date DESC",
            (user.username,),
        )

        rows = cursor.fetchall()

        return list(map(row_to_plantation, rows))

    def get_by_user_and_year(self, user, year):
        """A method that gets plantations created by a certain user for a certain year.

        Args:
            user: user-object to get the plantations for.
            year: int, the year of interest.

        Returns:
            A list of plantations.
        """

        year = get_year_timestamps(year)

        cursor = self._conn.cursor()

        cursor.execute(
            "select * from plantations WHERE username=? AND planting_date>? AND planting_date<? ORDER BY planting_date DESC",
            (user.username, year["start"], year["end"]),
        )

        rows = cursor.fetchall()

        return list(map(row_to_plantation, rows))

    def get_by_id(self, plant_id):
        """A method to get info for one plantation.

        Args:
            plant_id: id for the plantation of interest.

        Returns:
            A plantation-object.
        """

        cursor = self._conn.cursor()

        cursor.execute("select * from plantations WHERE plant_id=?", (plant_id,))

        row = cursor.fetchone()

        return row_to_plantation(row)

    def create(self, plantation):
        """A method to store a plantation in the db.

        Args:
            plantation: plantation-object to store.
        """
        cursor = self._conn.cursor()

        cursor.execute(
            "insert into plantations (username, plant, planting_date, amount_planted, info, yield_date, amount_yield) values (?,?,?,?,?,?,?)",
            plantation.get_tuple(),
        )

        self._conn.commit()

    def update(self, plantation):
        """A method to update a plantation in the db.

        Args:
            plantation: plantation-object to be updated.
        """
        cursor = self._conn.cursor()

        cursor.execute(
            "UPDATE plantations SET username=?, plant=?, planting_date=?, amount_planted=?, info=?, yield_date=?, amount_yield=? WHERE plant_id=?",
            plantation.get_tuple() + (plantation.get_id(),),
        )

        self._conn.commit()

    def delete(self, plantation):
        """A method to delete a plantation from the db.

        Args:
            plantation: plantation-object to delete.
        """
        cursor = self._conn.cursor()

        cursor.execute(
            "DELETE from plantations WHERE plant_id=?;", (plantation.get_id(),)
        )

        self._conn.commit()

    def delete_all(self):  # for tests
        """A method to delete all plantations, for testing."""
        cursor = self._conn.cursor()

        cursor.execute("DELETE from plantations;")

        self._conn.commit()


plantation_repo = PlantationRepo(get_db_connection())
