import time
import datetime
from tkinter import ttk, StringVar, constants
from tkcalendar import Calendar
from services.gardening_service import gardening_service, LoginError


class EditPlantationView:
    def __init__(self, root, show_mainview, edit_planting_date, edit_yield_date, plant_id):
        self._root = root
        self._show_mainview = show_mainview
        self._edit_planting_date = edit_planting_date
        self._edit_yield_date = edit_yield_date
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

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _save_plantation(self):
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

    def _date_to_string(self, date):
        return str(date.day) + "/" + str(date.month) + "/" + str(date.year)

    def _create_entry(self, insert=None):
        entry = ttk.Entry(master=self._frame, width=50)
        if insert:
            entry.insert(0, insert)
        return entry

    def _create_label(self, text):
        return ttk.Label(master=self._frame, text=text)

    def _add_to_grid(self, element):
        element.grid(row=self._row, column=0, columnspan=2, padx=5,
                     pady=5, sticky=(constants.E, constants.W))
        self._row += 1

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        yield_date = self._plantation.get_yield_date()
        yield_date_button_text = ""
        if not yield_date:
            yield_date_button_text = "Add yield date"
        else:
            yield_date_button_text = "Edit yield date: " + \
                self._date_to_string(yield_date)

        label = self._create_label("Edit the plantation")
        error_label = ttk.Label(
            master=self._frame, textvariable=self._error_label_var, foreground="red")
        edit_planting_date_button = ttk.Button(master=self._frame, text="Edit planting date: " + self._date_to_string(
            self._plant_date), command=lambda: self._edit_planting_date(self._plant_id))
        plant_label = self._create_label("Which plant?")
        self._plant_entry = self._create_entry(self._plantation.get_plant())
        amount_label = self._create_label("How much did you plant?")
        self._amount_planted_entry = self._create_entry(
            self._plantation.get_amount_planted())
        info_label = self._create_label("Any other relevant info?")
        self._info_entry = self._create_entry(self._plantation.get_info())
        edit_yield_date_button = ttk.Button(
            master=self._frame, text=yield_date_button_text, command=lambda: self._edit_yield_date(self._plant_id))
        yield_amount_label = self._create_label("How much yield?")
        self._yield_entry = self._create_entry(self._plantation.get_amount_yield())
        add_button = ttk.Button(
            master=self._frame, text="Save", command=self._save_plantation)
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", width=30, command=self._show_mainview)

        for element in [label,
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
                        cancel_button]:
            self._add_to_grid(element)

        self._root.grid_columnconfigure(0, weight=1)
