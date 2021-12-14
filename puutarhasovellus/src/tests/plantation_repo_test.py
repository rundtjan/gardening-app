# pylint: skip-file

import unittest
import datetime
from repositories.plantation_repo import plantation_repo
from entities.plantation import Plantation
from entities.user import User

class TestPlantationRepo(unittest.TestCase):
    def setUp(self):
        self._plantation_repo = plantation_repo
        self._plantation_repo.delete_all()

    def test_that_can_create_plantation_and_then_get_it_by_user_and_year(self):
        user1 = User('Test User', 'Password', False)
        self._plantation_repo.create(Plantation(user1.username, 'Beetroot', datetime.datetime.now(), '22kg', 'Some info', None, None))
        plants = self._plantation_repo.get_by_user_and_year(user1, datetime.datetime.now().year)
        self.assertEqual(len(plants), 1)

    def test_that_can_update_plantation(self):
        user2 = User('Test User 2', 'Password', False)
        self._plantation_repo.create(Plantation(user2.username, 'Carrot', datetime.datetime.now(), '22kg', 'Some info', None, None))
        plantation = self._plantation_repo.get_by_user_and_year(user2, datetime.datetime.now().year)[0]
        plantation.set_info('The info changed')
        self._plantation_repo.update(plantation)
        plantation = self._plantation_repo.get_by_user_and_year(user2, datetime.datetime.now().year)[0]
        self.assertEqual(plantation.get_info(), 'The info changed')

    def test_can_get_plantation_by_id(self):
        user3 = User('Test User 3', 'Password', False)
        self._plantation_repo.create(Plantation(user3.username, 'Carrot', datetime.datetime.now(), '22kg', 'Some info', None, None))
        plantation = self._plantation_repo.get_by_user_and_year(user3, datetime.datetime.now().year)[0]
        plant_id = plantation.get_id()
        plantation2 = self._plantation_repo.get_by_id(plant_id)
        self.assertEqual(plantation.get_id(), plantation2.get_id())

    def test_can_delete_plantation(self):
        user4 = User('Test User 4', 'Password', False)
        self._plantation_repo.create(Plantation(user4.username, 'Carrot', datetime.datetime.now(), '22kg', 'Some info', None, None))
        plantations = self._plantation_repo.get_by_user_and_year(user4, datetime.datetime.now().year)
        self.assertEqual(len(plantations), 1)
        self._plantation_repo.delete(plantations[0])
        plantations2 = self._plantation_repo.get_by_user_and_year(user4, datetime.datetime.now().year)
        self.assertEqual(len(plantations2), 0)



        