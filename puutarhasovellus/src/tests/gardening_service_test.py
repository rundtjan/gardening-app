import unittest
from entities.user import User
from services.gardening_service import (GardeningService, UserNameInUseError,
                                        CredentialsTooShortError, LoginError)


class UserRepoStub:
    def get_user(self, username):
        if username == "Exists":
            return User('Exists', 'ExistPassword', False)
        return None

    def create(self, user):
        pass


class PlantationRepoStub:
    def get_by_user(user):
        return user.username


class TestGardeningService(unittest.TestCase):
    def setUp(self):
        self._gardening_service = GardeningService(
            UserRepoStub(), PlantationRepoStub)

    def test_can_register_user_that_doesnt_exist(self):
        self.assertTrue(self._gardening_service.register_user(
            'No such user', 'Life'))

    def test_cant_register_user_that_does_exist(self):
        self.assertRaises(
            UserNameInUseError, self._gardening_service.register_user, 'Exists', 'Life')

    def test_cant_register_user_with_too_short_credentials(self):
        self.assertRaises(CredentialsTooShortError,
                          self._gardening_service.register_user, 'Ex', 'Li')

    def test_can_login_existing_user_with_valid_password(self):
        self._gardening_service.login_user('Exists', 'ExistPassword')
        self.assertEqual(self._gardening_service._user.username, 'Exists')

    def test_cant_login_existing_user_with_incorrect_password(self):
        self.assertRaises(
            LoginError, self._gardening_service.login_user, 'Exists', 'NotExistsPassword')

    def test_cant_login_nonexisting_user(self):
        self.assertRaises(LoginError, self._gardening_service.login_user,
                          'DoesntExist', 'NotExistsPassword')

    def test_can_get_plantations(self):
        self._gardening_service.login_user('Exists', 'ExistPassword')
        self.assertEqual(self._gardening_service.get_plantations(), 'Exists')