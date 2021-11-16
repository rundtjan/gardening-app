from entities.user import User
from repositories.user_repo import user_repo as default_user_repo

class UserNameInUseError(Exception):
    pass

class CredentialsTooShortError(Exception):
    pass

class GardeningService:
    '''A class that handles the logic of the gardening application.
    '''
    def __init__(self, user_repo=default_user_repo):
        '''The constructor for the service.

            Args:
                user_repo=an object containing methods to access and edit the user-data in the db.
        '''
        self._user_repo = user_repo
        self._user = None

    def register_user(self, username, password, admin=False):
        if self._user_repo.get_user(username):
            raise UserNameInUseError("The username is already in use.")
        elif len(username) < 3 or len(password) < 3:
            raise CredentialsTooShortError("Both username and password need to be atleast 3 characters long.")
        else:
            self._user_repo.create(User(username, password, admin))
            return True
    
gardening_service = GardeningService()