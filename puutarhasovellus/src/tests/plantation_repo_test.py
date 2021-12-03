import unittest
from repositories.plantation_repo import plantation_repo
from entities.plantation import Plantation

class TestPlantationRepo(unittest.TestCase):
    def setUp(self):
        plantation_repo.delete_all()
        self.plantation_one = Plantation()
        self.plantation_two = Plantation()

    def test_create(self):
        user_repo.create(self.user_one)
        allusers = user_repo.get_all()
        self.assertEqual(len(allusers), 1)
        self.assertEqual(allusers[0]['username'], 'One')

    def test_get_plantation_that_exists(self):
        user_repo.create(self.user_one)
        user = user_repo.get_user('One')
        self.assertEqual(user.password, 'Gamma')

    def test_get_plantation_that_doesnt_exist(self):
        user = user_repo.get_user('No such user')
        self.assertIsNone(user)

    def test_update_plantation(self):
        pass

    def test_delete(self):
        user_repo.create(self.user_one)
        user_repo.create(self.user_two)
        allusers = user_repo.get_all()
        self.assertEqual(len(allusers), 2)
        user_repo.delete_all()
        allusers = user_repo.get_all()
        self.assertEqual(len(allusers), 0)
