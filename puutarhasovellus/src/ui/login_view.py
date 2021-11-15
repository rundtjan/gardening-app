from tkinter import ttk, StringVar, constants
from services.gardening_service import gardening_service

class LoginView:
    '''An object that creates the loginview.
    '''

    def __init__(self, root, show_mainview, show_registration, show_adminview):
        '''The constructor.

        Args:
            root: the tkinter-root-object.
            show_mainview: a function to show the mainview if login is successful
            show_registration: a function to swith to the registration window
            show_adminview: a function to show the adminview is login is succesful for an admin
        '''

        self._root = root
        self._show_mainview = show_mainview
        self._show_registration = show_registration
        self._show_adminview = show_adminview
        self._frame = None
        self._user_entry = None
        self._pw_entry = None
        #continue filling up all variables and then self.initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_login(self):
        username = self._user_entry.get()
        password = self._pw_entry.get()
        print(f"Looks like {username} has password {password}")
