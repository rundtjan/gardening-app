from tkinter import ttk, StringVar, constants
from services.gardening_service import gardening_service, LoginError


class MainView:
    '''An object that creates the loginview.
    '''

    def __init__(self, root, show_login, add_plantation, show_edit_plantation, show_adminview):
        '''The constructor.

        Args:
            root: the tkinter-root-object.
            show_login: a function to show the login-window if user logs out
            show_plantation: a function to show the window to enter a new or edit a plantation
            show_adminview: a function to show the adminview is login is succesful for an admin
        '''

        self._root = root
        self._show_login = show_login
        self._add_plantation = add_plantation
        self._show_edit_plantation = show_edit_plantation
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

    def _add_edit_button(self, plant):
        ttk.Button(master=self._frame, text=str(plant), width=50, command=lambda: self._edit_plantation(plant.get_id())).grid(column=0)

    def _initialize_plant_rows(self):
        plantations = gardening_service.get_plantations()
        if len(plantations) > 0:
            label = ttk.Label(master=self._frame, text="Edit or review plantations:")
            label.grid(row=1, column=0, padx=5, pady=5)

        for plant in plantations:
            self._add_edit_button(plant)

    def _edit_plantation(self, plant_id):
        self._show_edit_plantation(plant_id)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        add_button = ttk.Button(master=self._frame, text="Add new plantation", width=50, command=self._add_plantation)
        
        add_button.grid(row=0, column=0, padx=5, pady=5)

        self._initialize_plant_rows()

        self._root.grid_columnconfigure(0, weight=1)
