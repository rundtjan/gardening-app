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
            user_repo: an object containing methods to access and edit the user-data in the db.
            plantation_repo: an object containing methods to access and edit the plantation-data in the db.
        """
        self._user_repo = user_repo
        self._plantation_repo = plantation_repo
        self._user = None
        self._active_year = datetime.datetime.now().year

    def register_user(self, username, password, admin=False):
        """A method for adding a new user.

        Args:
            username: string, the username
            password: string, the password
            admin: boolean, default to false, wether the new user will be an admin or not.

        Raises:
            UserNameInUseError: if the username is already taken
            CredentialsTooShortError: if the username and/or password is shorter than 3 characters.

        Returns:
            True: if no errors were triggered.
        """
        if self._user_repo.get_user(username):
            raise UserNameInUseError("The username is already in use.")
        if len(username) < 3 or len(password) < 3:
            raise CredentialsTooShortError(
                "Both username and password need to be atleast 3 characters long."
            )

        self._user_repo.create(User(username, password, admin))
        return True

    def login_user(self, username, password):
        """A method that handles a login

        Args:
            username: string, the username
            password: string, the password

        Raises:
            LoginError: if the credentials are not valid.
        """
        user = self._user_repo.get_user(username)
        if user and user.password == password:
            self._user = user
        else:
            raise LoginError("Check your credentials")

    def get_plantations(self):
        """A method to get plantations stored by the active user"""
        return self._plantation_repo.get_by_user(self._user)

    def get_plantations_by_year(self):
        """A method that gets plantations stored by the active user during the active year."""
        return self._plantation_repo.get_by_user_and_year(self._user, self._active_year)

    def get_plantation_by_id(self, plant_id):
        """A method that gets the information for a certain plantation.

        Args:
            plant_id: id for the plantation to be fetched.
        """
        return self._plantation_repo.get_by_id(plant_id)

    def create_plantation(self, plant, date, amount_planted, info):
        """A method to create a new plantation.

        Args:
            plant: string, the name of the plant species.
            date: date, the date the plant was planted.
            amount_planted: string, info on the amount planted.
            info: string, whichever other info the user wishes to add.

        Raises:
            PlantNameTooShortError: if the plantname is shorter than 3 characters.
            NoPlantingAmountError: if there's no information on how much that was planted.
        """
        if len(plant) < 3:
            raise PlantNameTooShortError("The plantname is too short.")
        if len(amount_planted) == 0:
            raise NoPlantingAmountError("Please enter the amount planted.")
        plantation = Plantation(self._user.username, plant, date, amount_planted, info)
        self._plantation_repo.create(plantation)

    def update_plantation(self, plantation, just_yield_date=False):
        """A method to update information on a plant.

        Args:
            plantation: plantation-object, to be updated.
            just_yield_date: boolean, True if it's ok to store the info without yield amount.

        Raises:
            PlantNameTooShortError: if the plantname is shorter than 3 characters.
            NoPlantingAmountError: if information on the amount planted is missing.
            YieldDateOrYieldAmountError: if yield date or yield amount is missing and both are required.
        """
        if len(plantation.get_plant()) < 3:
            raise PlantNameTooShortError("The plantname is too short.")
        if len(plantation.get_amount_planted()) == 0:
            raise NoPlantingAmountError("Please enter the amount planted.")
        if plantation.get_amount_yield() and not plantation.get_yield_date():
            raise YieldDateOrYieldAmountError("Both yield date and amount needed.")
        if (
            plantation.get_yield_date()
            and not plantation.get_amount_yield()
            and not just_yield_date
        ):
            raise YieldDateOrYieldAmountError("Both yield date and amount needed.")
        self._plantation_repo.update(plantation)

    def delete_plantation(self, plantation):
        """A method to delete a plantation.

        Args:
            plantation: plantation-object to be deleted.
        """
        self._plantation_repo.delete(plantation)

    def set_year(self, year):
        """A method to set the active year.

        Args:
            year: int, year to be set.
        """
        self._active_year = year


gardening_service = GardeningService()
