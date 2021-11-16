from tkinter import ttk, StringVar, constants
from services.gardening_service import gardening_service, UserNameInUseError, CredentialsTooShortError

class RegistrationView:
    '''An object that creates the registration view
    '''

    def __init__(self, root, show_login):
        '''Constructor, not yet developed

        Args:
            root: the tkinter-root-object.
            show_login: function that shows login-window.
        '''

        self._root = root
        self._show_login = show_login
        self._frame = None
        self._user_entry = None
        self._pw_entry = None
        self._error_label_var = StringVar()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_registration(self):
        username = self._user_entry.get()
        password = self._pw_entry.get()
        try:
            gardening_service.register_user(username, password)
            self._show_login()
        except UserNameInUseError:
            self._error_label_var.set("The username already exists.")
        except CredentialsTooShortError:
            self._error_label_var.set("You need longer credentials.")
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Enter new credentials")
        error_label = ttk.Label(master=self._frame, textvariable=self._error_label_var, foreground="red")
        user_label = ttk.Label(master=self._frame, text="Username")
        self._user_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame, text="Password")
        self._pw_entry = ttk.Entry(master=self._frame)
        register_button = ttk.Button(master=self._frame, text="Register", command=self._handle_registration)
        show_login_button = ttk.Button(master=self._frame, text="Back to login", command=self._show_login)

        label.grid(row=0, column=0, padx=5, pady=5)
        error_label.grid(row=0, column=1, padx=5, pady=5)
        user_label.grid(row=1, column=0, padx=5, pady=5)
        self._user_entry.grid(row=1, column=1, padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._pw_entry.grid(row=2, column=1, padx=5, pady=5)
        register_button.grid(row=3, column=0, padx=5, pady=5)
        show_login_button.grid(row=3, column=1, padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1)