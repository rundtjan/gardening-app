# pylint: skip-file

from tkinter import ttk, StringVar, constants
from services.gardening_service import gardening_service, LoginError


class LoginView:
    '''An object that creates the loginview.
    '''

    def __init__(self, root, show_registration, show_mainview, show_adminview):
        '''The constructor.

        Args:
            root: the tkinter-root-object.
            show_mainview: a function to show the mainview if login is successful
            show_registration: a function to swith to the registration window
            show_adminview: a function to show the adminview is login is succesful for an admin
        '''

        self._root = root
        self._show_registration = show_registration
        self._show_mainview = show_mainview
        self._show_adminview = show_adminview
        self._frame = None
        self._user_entry = None
        self._pw_entry = None
        self._error_label_var = StringVar()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_login(self):
        username = self._user_entry.get()
        password = self._pw_entry.get()
        try:
            gardening_service.login_user(username, password)
            self._show_mainview()
        except LoginError:
            self._error_label_var.set("Check your credentials.")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Enter credentials")
        error_label = ttk.Label(master=self._frame,
                                textvariable=self._error_label_var, foreground="red")
        user_label = ttk.Label(master=self._frame, text="Username")
        self._user_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame, text="Password")
        self._pw_entry = ttk.Entry(master=self._frame)
        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._handle_login)
        register_button = ttk.Button(
            master=self._frame, text="Register", command=self._show_registration)

        label.grid(row=0, column=0, padx=5, pady=5)
        error_label.grid(row=0, column=1, padx=5, pady=5)
        user_label.grid(row=1, column=0, padx=5, pady=5)
        self._user_entry.grid(row=1, column=1, padx=5, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._pw_entry.grid(row=2, column=1, padx=5, pady=5)
        login_button.grid(row=3, column=0, padx=5, pady=5)
        register_button.grid(row=3, column=1, padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1)
