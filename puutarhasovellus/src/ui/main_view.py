from tkinter import ttk, StringVar, constants
from services.gardening_service import gardening_service, LoginError


class MainView:
    '''An object that creates the loginview.
    '''

    def __init__(self, root, show_login, show_plantation, show_adminview):
        '''The constructor.

        Args:
            root: the tkinter-root-object.
            show_login: a function to show the login-window if user logs out
            show_plantation: a function to show the window to enter a new or edit a plantation
            show_adminview: a function to show the adminview is login is succesful for an admin
        '''

        self._root = root
        self._show_login = show_login
        self._show_plantation = show_plantation
        self._show_adminview = show_adminview
        self._frame = None
        #self._user_entry = None
        #self._pw_entry = None
        self._error_label_var = StringVar()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_plant_rows(self):
        plantations = gardening_service.get_plantations()
        for plant in plantations:
            #ttk.Label(master=self._frame, text=str(plant)).grid(column=0)
            ttk.Button(master=self._frame, text=str(
                plant), command=lambda: self._edit_plantation(plant.get_id())).grid(column=0)

    def _edit_plantation(self, plant_id):
        self._show_plantation(plant_id)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Add or edit plantation")
        error_label = ttk.Label(
            master=self._frame, textvariable=self._error_label_var, foreground="red")

        label.grid(row=0, column=0, padx=5, pady=5)
        error_label.grid(row=0, column=1, padx=5, pady=5)

        self._initialize_plant_rows()

        #login_button.grid(row=3, column=0, padx=5, pady=5)
        #register_button.grid(row=3, column=1, padx=5, pady=5)

        self._root.grid_columnconfigure(0, weight=1)
