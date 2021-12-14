# pylint: skip-file

from ui.login_view import LoginView
from ui.registration_view import RegistrationView
from ui.main_view import MainView
from ui.add_plantation_view import AddPlantationView
from ui.edit_plantation_view import EditPlantationView
from ui.choose_year_view import ChooseYearView
from ui.edit_date_view2 import EditDateView


class UI:
    """Master class for all UI:s"""

    def __init__(self, root):
        """Constructor.

        Args:
            root: the tkinter-root-object

        Also initializes a _current-variable that keeps track of and manipulizes which window the UI is showing.

        """

        self._root = root
        self._current = None

    def start(self):
        """Function that starts the UI by showing the login-window"""
        self._show_login()

    def _hide_current(self):
        """Function that hides any view that might be active"""
        if self._current:
            self._current.destroy()

        self._current = None

    def _show_login(self):
        """Function that shows the login window"""
        self._hide_current()
        self._current = LoginView(
            self._root,
            self._show_registration,
            self._show_mainview,
            self._show_adminview,
        )
        self._current.pack()

    def _show_registration(self):
        """Function that shows the registration window"""
        self._hide_current()
        self._current = RegistrationView(self._root, self._show_login)
        self._current.pack()

    def _show_mainview(self):
        """Function that shows the mainview window"""
        self._hide_current()
        self._current = MainView(
            self._root,
            self._show_login,
            self._add_plantation,
            self._show_edit_plantation,
            self._show_adminview,
            self._show_choose_year,
        )
        self._current.pack()

    def _show_adminview(self):
        """Function that shows the admin window"""
        pass

    def _add_plantation(self):
        '''A method that shows the view to add a new plantation'''
        self._hide_current()
        self._current = AddPlantationView(self._root, self._show_mainview)
        self._current.pack()

    def _show_edit_plantation(self, plant_id):
        '''A method that shows the view to edit a plantation
        
        Args:
            plant_id: the id of the plantation to be edited
        '''
        self._hide_current()
        self._current = EditPlantationView(
            self._root,
            self._show_mainview,
            plant_id,
            self._edit_date
        )
        self._current.pack()

    def _show_choose_year(self):
        '''A method that shows the view to choose which year to see info from'''
        self._hide_current()
        self._current = ChooseYearView(self._root, self._show_mainview)
        self._current.pack()

    def _edit_date(self, plant_id, planting_date):
        '''A method that shows the view to edit a date
        
        Args:
            plant_id: id of the plantation to add/edit a date to/on
            planting_date: boolean, True if planting-date, False if yield date.
        '''
        self._hide_current()
        self._current = EditDateView(self._root, self._show_edit_plantation, plant_id, planting_date)
        self._current.pack()
