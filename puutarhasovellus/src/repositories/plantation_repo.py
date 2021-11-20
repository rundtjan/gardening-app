from entities.plantation import Plantation
from db_connection import get_db_connection

class PlantationRepo:
    def __init__(self, conn):
        self._conn = conn

    def get_by_user(self, user):
        #contains a stub for building the ui
        list = [Plantation('beetroot', '12-5-2021', '2kg', '', user.username, '1'), Plantation('potatoes', '15-5-2021', '5kg', '', user.username, '2'), Plantation('onions', '28-5-2021', '0.5kg', '', user.username, '3')]
        return list

plantation_repo = PlantationRepo(get_db_connection())