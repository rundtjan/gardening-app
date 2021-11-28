import unittest
from repositories.user_repo import user_repo
from entities.user import User

class TestUserRepo(unittest.TestCase):
    def setUp(self):
        user_repo.delete_all()
        self.user_one = User('One', 'Gamma', False)
        self.user_two = User('Two', 'Kappa', False)

    def test_create(self):
        user_repo.create(self.user_one)
        allusers = user_repo.get_all()
        self.assertEqual(len(allusers), 1)
        self.assertEqual(allusers[0]['username'], 'One')

    def test_get_user_that_exists(self):
        user_repo.create(self.user_one)
        user = user_repo.get_user('One')
        self.assertEqual(user.password, 'Gamma')

    def test_get_user_that_doesnt_exist(self):
        user = user_repo.get_user('No such user')
        self.assertIsNone(user)

    def test_delete(self):
        user_repo.create(self.user_one)
        user_repo.create(self.user_two)
        allusers = user_repo.get_all()
        self.assertEqual(len(allusers), 2)
        user_repo.delete_all()
        allusers = user_repo.get_all()
        self.assertEqual(len(allusers), 0)
