class User:
    '''System user.

    Attributes:
        username: String.
        password: String.

    '''

    def __init__(self, username, password, admin):
        '''Constructor

        Args:
            username: string, no restrictions.
            password: string, no restrictions.
            status: boolean, False if regular user, True if adminuser.
        
        '''
        self.username = username
        self.password = password
        self.admin = admin

    def __str__(self):
        return f"{self.username}"