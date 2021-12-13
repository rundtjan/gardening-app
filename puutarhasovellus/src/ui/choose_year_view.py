import datetime
from tkinter import ttk, constants
from services.gardening_service import gardening_service


class ChooseYearView:
    """An object that creates the loginview."""

    def __init__(self, root, show_mainview):
        """The constructor.

        Args:
            root: the tkinter-root-object.
            show_login: a function to show the login-window if user logs out
            show_plantation: a function to show the window to enter a new or edit a plantation
            show_adminview: a function to show the adminview is login is succesful for an admin
        """

        self._root = root
        self._show_mainview = show_mainview
        self._frame = None
        self._current_year = datetime.datetime.now().year

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _add_choose_button(self, year):
        ttk.Button(
            master=self._frame,
            text=str(year),
            width=50,
            command=lambda: self._choose_year(year),
        ).grid(column=0)

    def _initialize_year_buttons(self):

        for year in [
            self._current_year - 1,
            self._current_year - 2,
            self._current_year - 3,
            self._current_year - 4,
        ]:
            self._add_choose_button(year)

    def _choose_year(self, year):
        gardening_service.set_year(year)
        print("worked this far")
        self._show_mainview()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        add_button = ttk.Button(
            master=self._frame,
            text="Show current year",
            width=50,
            command=lambda: self._choose_year(self._current_year),
        )

        add_button.grid(row=0, column=0, padx=5, pady=5)

        self._initialize_year_buttons()

        self._root.grid_columnconfigure(0, weight=1)
