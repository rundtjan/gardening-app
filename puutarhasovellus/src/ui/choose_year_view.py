import datetime
from tkinter import ttk, constants
from services.gardening_service import gardening_service


class ChooseYearView:
    """A class that creates a view where one can choose a year."""

    def __init__(self, root, show_mainview):
        """The constructor.

        Args:
            root: the tkinter-root-object.
            show_mainview: a function which opens the mainview-window.
        """

        self._root = root
        self._show_mainview = show_mainview
        self._frame = None
        self._current_year = datetime.datetime.now().year

        self._initialize()

    def pack(self):
        '''A method that creates the view when all elements are added to it.
        '''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''A method that closes the view.
        '''
        self._frame.destroy()

    def _add_choose_button(self, year):
        '''A method which creates a button and adds it to the layoutgrid.
        
        Args:
            year: int, which year to show on the button
        '''
        ttk.Button(
            master=self._frame,
            text=str(year),
            width=50,
            command=lambda: self._choose_year(year),
        ).grid(column=0)

    def _initialize_year_buttons(self):
        '''A method which uses the _add_choose_button to creates buttons
        '''
        for year in [
            self._current_year - 1,
            self._current_year - 2,
            self._current_year - 3,
            self._current_year - 4,
        ]:
            self._add_choose_button(year)

    def _choose_year(self, year):
        '''A method that chooses active year and opens the mainview

        Args:
            year: int, which year to show.
        '''
        gardening_service.set_year(year)
        self._show_mainview()

    def _initialize(self):
        '''A method that creates the elements of the view and adds them to the layoutgrid.
        '''
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
