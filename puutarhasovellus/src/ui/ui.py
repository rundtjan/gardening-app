from ui.login_view import LoginView
from ui.registration_view import RegistrationView

class UI:
    '''Master class for all UI:s
    '''
    def __init__(self, root):
        '''Constructor. 

        Args:
            root: the tkinter-root-object
        
        Also initializes a _current-variable that keeps track of and manipulizes which window the UI is showing.

        '''

        self._root = root
        self._current = None
        #self.userEntry = None
        #self.pwEntry = None
    
    def start(self):
        '''Function that starts the UI by showing the login-window
        '''
        self._show_login()

    def _hide_current(self):
        '''Function that hides any view that might be active
        '''
        if self._current:
            self._current.destroy()

        self._current = None
    
    def destroy(self):


    def _show_login(self):
        '''Function that shows the login window
        '''
        self._hide_current()
        self_current = LoginView(self._root, self._show_registration, self._show_mainview, self._show_adminview)

    def _show_registration(self):
        '''Function that shows the registration window
        '''
        self._hide_current()
        self_current = RegistrationView(self._root, self._show_login)
    
    def _handle_login(self, username, password):
        '''Function to handle login.

        Args:
            username: String.
            password: String.

        '''

        pass

    def _handle_registration(self):
        '''Function to show registration window.
        '''
        
        pass

        def _handle_login(self, username, password):
        '''Function to handle login.

        Args:
            username: String.
            password: String.

        '''

        pass


    def startold(self):
        userLabel = ttk.Label(master=self._root, text="Username")
        self.userEntry = ttk.Entry(master=self._root)
        passwordLabel = ttk.Label(master=self._root, text="Password")
        self.pwEntry = ttk.Entry(master=self._root)
        loginButton = ttk.Button(master=self._root, text="Login", command=self._handle_login)
        regButton = ttk.Button(master=self._root, text="Register", command=self._handle_register)
        userLabel.pack()
        self.userEntry.pack()
        passwordLabel.pack()
        self.pwEntry.pack()
        loginButton.pack()
        regButton.pack()

    def _handle_login(self):
        username = self.userEntry.get()
        password = self.pwEntry.get()
        print(f"Looks like {username} has password {password}")

    def _handle_register(self):
        print("So you want to register")
