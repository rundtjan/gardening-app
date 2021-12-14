# pylint: skip-file

import datetime
from tkinter import ttk, StringVar, constants, IntVar
from tkcalendar import Calendar
from services.gardening_service import gardening_service
from functions.functions import create_date_menu


class AddPlantationView:
    '''A class that creates a view to add new plantations
    '''
    def __init__(self, root, show_mainview):
        '''The constructor of the view-class.

        Args:
            root: the tkinter-rootobject
            show_mainview: a function, with which you open the mainview
        '''
        self._root = root
        self._show_mainview = show_mainview
        self._frame = None
        self._error_label_var = StringVar()
        self._plant_entry = None
        self._amount_planted_entry = None
        self._info_entry = None
        self._cal = None
        self._date = datetime.datetime.now()
        self._row = 0
        self._day = IntVar()
        self._month = IntVar()
        self._year = IntVar()

        self._initialize()

    def pack(self):
        '''A method that creates the view when all elements are added to it.
        '''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''A method that closes the view.
        '''
        self._frame.destroy()

    def _save_plantation(self):
        '''A method that saves the info the user has entered into the form in the view.
        '''
        try:
            date = datetime.datetime(
                year=int(self._year.get()),
                month=int(self._month.get()),
                day=int(self._day.get()),
            )
        except Exception as error:
            self._error_label_var.set(str(error))
            return
        plant = self._plant_entry.get()
        amount_planted = self._amount_planted_entry.get()
        info = self._info_entry.get()
        try:
            gardening_service.create_plantation(plant, date, amount_planted, info)
            self._show_mainview()
        except Exception as error:
            self._error_label_var.set(str(error))

    def _create_entry(self):
        '''A method that creates an inputfield.

        Returns:
            An inputfield.
        '''
        entry = ttk.Entry(master=self._frame, width=50)
        return entry

    def _create_label(self, text):
        '''A method that creates a label.
        
        Args:
            text: String, the text to enter into the label.

        Returns:
            A label.
        '''
        return ttk.Label(master=self._frame, text=text)

    def _add_to_grid(self, element):
        '''A method that adds elements to the layoutgrid of the view.
        
        Args:
            element: an element of the view.
        '''
        element.grid(
            row=self._row,
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            sticky=(constants.E, constants.W),
        )
        self._row += 1

    def _initialize(self):
        '''A method that creates the elements of the view and adds them to the layoutgrid.
        '''
        self._frame = ttk.Frame(master=self._root)
        label = self._create_label("Add a new plantation")
        error_label = ttk.Label(
            master=self._frame, textvariable=self._error_label_var, foreground="red"
        )
        plant_cal_label = ttk.Label(
            master=self._frame, text="Enter date (day/month/year):"
        )
        dropdowns = create_date_menu(self._frame, self._date, self._year, self._month, self._day)
        plant_label = self._create_label("Which plant?")
        self._plant_entry = self._create_entry()
        amount_label = self._create_label("How much did you plant?")
        self._amount_planted_entry = self._create_entry()
        info_label = self._create_label("Any other relevant info?")
        self._info_entry = self._create_entry()
        error_label = ttk.Label(
            master=self._frame, textvariable=self._error_label_var, foreground="red"
        )

        add_button = ttk.Button(
            master=self._frame, text="Save", command=self._save_plantation
        )
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", width=30, command=self._show_mainview
        )

        for element in [label, plant_cal_label]:
            self._add_to_grid(element)

        dropdowns['day'].grid(row=2, column=0)
        dropdowns['month'].grid(row=2, column=1)
        dropdowns['year'].grid(row=2, column=2)

        self._row += 1

        for element in [
            plant_label,
            self._plant_entry,
            amount_label,
            self._amount_planted_entry,
            info_label,
            self._info_entry,
            error_label,
            add_button,
            cancel_button,
        ]:
            self._add_to_grid(element)

        self._root.grid_columnconfigure(0, weight=1)
