import datetime
import unittest
from unittest.mock import Mock
from entities.user import User
from entities.plantation import Plantation
from services.gardening_service import (
    GardeningService,
    UserNameInUseError,
    CredentialsTooShortError,
    LoginError,
    PlantNameTooShortError,
    NoPlantingAmountError,
    YieldDateOrYieldAmountError,
    YieldDateEarlyError
)


class UserRepoStub:
    def get_user(self, username):
        if username == "Exists":
            return User("Exists", "ExistPassword", False)
        return None

    def create(self, user):
        pass


plantation_repo_mock = Mock()


def create(plantation):
    return plantation


plantation_repo_mock.side_effect = create


class TestGardeningService(unittest.TestCase):
    def setUp(self):
        self._gardening_service = GardeningService(UserRepoStub(), plantation_repo_mock)

    def test_can_register_user_that_doesnt_exist(self):
        self.assertTrue(self._gardening_service.register_user("No such user", "Life"))

    def test_cant_register_user_that_does_exist(self):
        self.assertRaises(
            UserNameInUseError, self._gardening_service.register_user, "Exists", "Life"
        )

    def test_cant_register_user_with_too_short_credentials(self):
        self.assertRaises(
            CredentialsTooShortError, self._gardening_service.register_user, "Ex", "Li"
        )

    def test_can_login_existing_user_with_valid_password(self):
        self._gardening_service.login_user("Exists", "ExistPassword")
        self.assertEqual(self._gardening_service._user.username, "Exists")

    def test_cant_login_existing_user_with_incorrect_password(self):
        self.assertRaises(
            LoginError,
            self._gardening_service.login_user,
            "Exists",
            "NotExistsPassword",
        )

    def test_cant_login_nonexisting_user(self):
        self.assertRaises(
            LoginError,
            self._gardening_service.login_user,
            "DoesntExist",
            "NotExistsPassword",
        )

    def test_get_plantations_by_year_calls_repo_correctly(self):
        self._gardening_service.login_user("Exists", "ExistPassword")
        self._gardening_service.set_year("2021")
        self._gardening_service.get_plantations_by_year()
        plantation_repo_mock.get_by_user_and_year.assert_called_with(
            self._gardening_service._user, "2021"
        )

    def test_get_plantation_by_id_calls_repo_correctly(self):
        self._gardening_service.get_plantation_by_id("1")
        plantation_repo_mock.get_by_id.assert_called_with("1")

    def test_cant_create_plant_with_too_short_name(self):
        self.assertRaises(
            PlantNameTooShortError,
            self._gardening_service.create_plantation,
            "Tw",
            datetime.datetime.now(),
            "22kg",
            "Some info",
        )

    def test_cant_create_plant_without_amount_planted(self):
        self.assertRaises(
            NoPlantingAmountError,
            self._gardening_service.create_plantation,
            "Beetroot",
            datetime.datetime.now(),
            "",
            "Some info",
        )

    def test_will_create_new_plantation_if_all_info_correct(self):
        date = datetime.datetime.now()
        self._gardening_service.login_user("Exists", "ExistPassword")
        self._gardening_service.create_plantation("beetroot", date, "33kg", "some info")
        plantation_repo_mock.create.assert_called()

    def test_cant_update_plant_with_too_short_name(self):
        plantation = Plantation(
            "Exists", "Tw", datetime.datetime.now(), "33kg", "some info"
        )
        self.assertRaises(
            PlantNameTooShortError,
            self._gardening_service.update_plantation,
            plantation,
        )

    def test_cant_update_plant_without_amount_planted(self):
        plantation = Plantation(
            "Exists", "Reed", datetime.datetime.now(), "", "some info"
        )
        self.assertRaises(
            NoPlantingAmountError, self._gardening_service.update_plantation, plantation
        )

    def test_cant_update_plant_with_yield_amount_if_no_yield_date(self):
        plantation = Plantation(
            "Exists",
            "Reed",
            datetime.datetime.now(),
            "33kg",
            "some info",
            None,
            "330kg",
        )
        self.assertRaises(
            YieldDateOrYieldAmountError,
            self._gardening_service.update_plantation,
            plantation,
        )

    def test_cant_update_plant_with_yield_date_if_no_yield_amount_and_not_flagged_ok_to_leave_out_amount(
        self,
    ):
        plantation = Plantation(
            "Exists",
            "Reed",
            datetime.datetime.now(),
            "33kg",
            "some info",
            datetime.datetime.now(),
            "",
        )
        self.assertRaises(
            YieldDateOrYieldAmountError,
            self._gardening_service.update_plantation,
            plantation,
        )

    def test_cant_add_yield_date_that_is_before_yield_date(self):
        date = datetime.datetime.now()
        days = datetime.timedelta(5)
        date2 = date - days
        plantation = Plantation(
            "Exists",
            "Reed",
            date,
            "33kg",
            "some info",
            date2,
            "333kg",
        )
        self.assertRaises(
            YieldDateEarlyError,
            self._gardening_service.update_plantation,
            plantation,
        )
