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
        all = user_repo.get_all()
        self.assertEqual(len(all), 1)
        self.assertEqual(all[0]['username'], 'One')

    def test_delete(self):
        user_repo.create(self.user_one)
        user_repo.create(self.user_two)
        all = user_repo.get_all()
        self.assertEqual(len(all), 2)
        user_repo.delete_all()
        all = user_repo.get_all()
        self.assertEqual(len(all), 0)
    
    def test_get_user_that_exists(self):
        user_repo.create(self.user_one)
        user = user_repo.get_user('One')
        self.assertEqual(user.password, 'Gamma')
    
    def test_get_user_that_doesnt_exist(self):
        user = user_repo.get_user('No such user')
        self.assertIsNone(user)