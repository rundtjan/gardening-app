# pylint: skip-file

import datetime
from tkinter import ttk, StringVar, constants
from services.gardening_service import gardening_service


class EditPlantationView:
    '''A class that creates a view to edit the info of a plantation
    '''
    def __init__(
        self, root, show_mainview, plant_id, edit_date
    ):
        '''The constructor of the editplantation-class.

        Args:
            root: the tkinter-rootobject
            show_mainview: a function with which you open the mainview
            edit_planting_date: a function with which you open a calendar to edit the planting date
            edit_yield_date: a function with which you open a calendar to edit the yield date
            plant_id: int, the id of the plantation being edited
        '''
        self._root = root
        self._show_mainview = show_mainview
        self._edit_date = edit_date
        self._frame = None
        self._error_label_var = StringVar()
        self._plant_id = plant_id
        self._plantation = gardening_service.get_plantation_by_id(plant_id)
        self._plant_date = self._plantation.get_planting_date()
        self._plant_entry = None
        self._amount_planted_entry = None
        self._info_entry = None
        self._yield_entry = None
        self._cal = None
        self._date = datetime.datetime.now()
        self._row = 0
        self._delete_try = 0

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
        '''A method that saves the info that was entered into the form in the view
        '''
        self._plantation.set_plant(self._plant_entry.get())
        self._plantation.set_amount_planted(self._amount_planted_entry.get())
        self._plantation.set_info(self._info_entry.get())
        self._plantation.set_amount_yield(self._yield_entry.get())
        just_yield_date = False

        try:
            gardening_service.update_plantation(self._plantation, just_yield_date)
            self._show_mainview()
        except Exception as error:
            self._error_label_var.set(str(error))
    
    def _delete_plantation(self):
        '''A method that triggers a function to delete the plantation.
        '''
        if self._delete_try == 0:
            self._error_label_var.set("Click one more time to delete.")
            self._delete_try += 1
        else:
            gardening_service.delete_plantation(self._plantation)
            self._show_mainview()

    def _date_to_string(self, date):
        '''A method that creates a string representating a date

        Args:
            date: date, the date to be stringified.

        Returns:
            A string in the form dd/mm/year
        '''
        return str(date.day) + "/" + str(date.month) + "/" + str(date.year)

    def _create_entry(self, insert=None):
        '''A method that creates an inputfield.

        Args:
            insert: string, text to enter into the inputfield.

        Returns:
            An inputfield.
        '''
        entry = ttk.Entry(master=self._frame, width=50)
        if insert:
            entry.insert(0, insert)
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
            columnspan=2,
            padx=5,
            pady=5,
            sticky=(constants.E, constants.W),
        )
        self._row += 1

    def _initialize(self):
        '''A method that creates the elements of the view and adds them to the layoutgrid.
        '''
        self._frame = ttk.Frame(master=self._root)
        yield_date = self._plantation.get_yield_date()
        yield_date_button_text = ""
        if not yield_date:
            yield_date_button_text = "Add yield date"
        else:
            yield_date_button_text = "Edit yield date: " + self._date_to_string(
                yield_date
            )

        label = self._create_label("Edit the plantation")
        error_label = ttk.Label(
            master=self._frame, textvariable=self._error_label_var, foreground="red"
        )
        edit_planting_date_button = ttk.Button(
            master=self._frame,
            text="Edit planting date: " + self._date_to_string(self._plant_date),
            command=lambda: self._edit_date(self._plant_id, True),
        )
        plant_label = self._create_label("Which plant?")
        self._plant_entry = self._create_entry(self._plantation.get_plant())
        amount_label = self._create_label("How much did you plant?")
        self._amount_planted_entry = self._create_entry(
            self._plantation.get_amount_planted()
        )
        info_label = self._create_label("Any other relevant info?")
        self._info_entry = self._create_entry(self._plantation.get_info())
        edit_yield_date_button = ttk.Button(
            master=self._frame,
            text=yield_date_button_text,
            command=lambda: self._edit_date(self._plant_id, False),
        )
        yield_amount_label = self._create_label("How much yield?")
        self._yield_entry = self._create_entry(self._plantation.get_amount_yield())
        add_button = ttk.Button(
            master=self._frame, text="Save", command=self._save_plantation
        )
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._show_mainview
        )
        delete_button = ttk.Button(
            master=self._frame,
            text="Delete plantation",
            command=self._delete_plantation,
        )

        for element in [
            label,
            edit_planting_date_button,
            plant_label,
            self._plant_entry,
            amount_label,
            self._amount_planted_entry,
            info_label,
            self._info_entry,
            edit_yield_date_button,
            yield_amount_label,
            self._yield_entry,
            error_label,
            add_button,
            cancel_button,
            delete_button,
        ]:
            self._add_to_grid(element)

        self._root.grid_columnconfigure(0, weight=1)
