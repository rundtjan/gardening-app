from tkinter import ttk, StringVar, constants
from services.gardening_service import gardening_service


class MainView:
    """A class that creates the mainview."""

    def __init__(
        self,
        root,
        show_login,
        add_plantation,
        show_edit_plantation,
        show_adminview,
        show_choose_year,
    ):
        """The constructor.

        Args:
            root: the tkinter-root-object.
            show_login: a function to show the login-window if user logs out
            add_plantation: a function to show the window to add a new plantation
            show_edit_plantation: a function to show the window to edit a plantation
            show_adminview: a function to show the adminview is login is succesful for an admin
        """

        self._root = root
        self._show_login = show_login
        self._add_plantation = add_plantation
        self._show_edit_plantation = show_edit_plantation
        self._show_adminview = show_adminview
        self._show_choose_year = show_choose_year
        self._frame = None
        self._error_label_var = StringVar()

        self._initialize()

    def pack(self):
        '''A method that creates the view when all elements are added to it.
        '''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''A method that closes the view.
        '''
        self._frame.destroy()

    def _add_edit_button(self, plantation):
        '''A method that creates a button for choosing a plantation to edit
        
        Args:
            plantation: the plantation to open for editing if the button is pressed 
        '''
        ttk.Button(
            master=self._frame,
            text=str(plantation),
            width=50,
            command=lambda: self._edit_plantation(plantation.get_id()),
        ).grid(column=0)

    def _initialize_plant_rows(self):
        '''A method that adds buttons for plantations that can be edited
        '''
        plantations = gardening_service.get_plantations_by_year()
        if len(plantations) > 0:
            label = ttk.Label(master=self._frame, text="Edit or review plantations:")
            label.grid(row=3, column=0, padx=5, pady=5)

        for plant in plantations:
            self._add_edit_button(plant)

    def _edit_plantation(self, plant_id):
        '''A method that opens the editing-window for a plantation.

        Args:
            plant_id: id of the plantation to be edited.
        '''
        self._show_edit_plantation(plant_id)

    def _initialize(self):
        '''A method that creates the elements of the view and adds them to the layoutgrid.
        '''
        self._frame = ttk.Frame(master=self._root)
        add_button = ttk.Button(
            master=self._frame,
            text="Add new plantation",
            width=50,
            command=self._add_plantation,
        )
        choose_button = ttk.Button(
            master=self._frame,
            text="Show other year",
            width=50,
            command=self._show_choose_year,
        )

        add_button.grid(row=0, column=0, padx=5, pady=5)
        choose_button.grid(row=1, column=0, padx=5, pady=5)

        self._initialize_plant_rows()

        self._root.grid_columnconfigure(0, weight=1)
