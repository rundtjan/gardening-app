import datetime
from entities.user import User
from entities.plantation import Plantation
from repositories.user_repo import user_repo as default_user_repo
from repositories.plantation_repo import plantation_repo as default_plantation_repo


class UserNameInUseError(Exception):
    pass


class CredentialsTooShortError(Exception):
    pass


class LoginError(Exception):
    pass


class PlantNameTooShortError(Exception):
    pass


class NoPlantingAmountError(Exception):
    pass


class YieldDateOrYieldAmountError(Exception):
    pass


class GardeningService:
    """A class that handles the logic of the gardening application."""

    def __init__(
        self, user_repo=default_user_repo, plantation_repo=default_plantation_repo
    ):
        """The constructor for the service.

        Args:
            user_repo=an object containing methods to access and edit the user-data in the db.
        """
        self._user_repo = user_repo
        self._plantation_repo = plantation_repo
        self._user = None
        self._active_year = datetime.datetime.now().year

    def register_user(self, username, password, admin=False):
        if self._user_repo.get_user(username):
            raise UserNameInUseError("The username is already in use.")
        if len(username) < 3 or len(password) < 3:
            raise CredentialsTooShortError(
                "Both username and password need to be atleast 3 characters long."
            )

        self._user_repo.create(User(username, password, admin))
        return True

    def login_user(self, username, password):
        user = self._user_repo.get_user(username)
        if user and user.password == password:
            self._user = user
        else:
            raise LoginError("Check your credentials")

    def get_plantations(self):
        return self._plantation_repo.get_by_user(self._user)

    def get_plantations_by_year(self):
        return self._plantation_repo.get_by_user_and_year(self._user, self._active_year)

    def get_plantation_by_id(self, plant_id):
        return self._plantation_repo.get_by_id(plant_id)

    def create_plantation(self, plant, date, amount_planted, info):
        if len(plant) < 3:
            raise PlantNameTooShortError("The plantname is too short.")
        if len(amount_planted) == 0:
            raise NoPlantingAmountError("Please enter the amount planted.")
        plantation = Plantation(self._user.username, plant, date, amount_planted, info)
        self._plantation_repo.create(plantation)

    def update_plantation(self, plantation, just_yield_date=False):
        if len(plantation.get_plant()) < 3:
            raise PlantNameTooShortError("The plantname is too short.")
        if len(plantation.get_amount_planted()) == 0:
            raise NoPlantingAmountError("Please enter the amount planted.")
        if len(plantation.get_amount_planted()) > 0 and not plantation.get_yield_date():
            raise YieldDateOrYieldAmountError("Both yield date and amount needed.")
        if (
            plantation.get_yield_date()
            and not plantation.get_amount_yield()
            and not just_yield_date
        ):
            raise YieldDateOrYieldAmountError("Both yield date and amount needed.")
        self._plantation_repo.update(plantation)

    def delete_plantation(self, plantation):
        self._plantation_repo.delete(plantation)

    def set_year(self, year):
        self._active_year = year


gardening_service = GardeningService()
