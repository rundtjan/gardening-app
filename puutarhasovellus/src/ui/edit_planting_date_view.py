# pylint: skip-file

import datetime
from tkinter import ttk, StringVar, constants
from tkcalendar import Calendar
from services.gardening_service import gardening_service


class EditPlantingDateView:
    def __init__(self, root, _show_edit_plantation, plant_id):
        self._root = root
        self._show_edit_plantation = _show_edit_plantation
        self._frame = None
        self._error_label_var = StringVar()
        self._plant_id = plant_id
        self._plantation = gardening_service.get_plantation_by_id(plant_id)
        self._plant_date = self._plantation.get_planting_date()
        self._cal = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _edit_planting_date(self):
        date = self._cal.get_date()
        timestring = "%m/%d/%y"
        # this is a fix for the calendar emitting data in different form on Linux:
        if len(date.split("/")[2]) == 4:
            timestring = "%d/%m/%Y"
        date = datetime.datetime.strptime(date, timestring)
        self._plantation.set_planting_date(date)
        gardening_service.update_plantation(self._plantation)
        self._show_edit_plantation(self._plant_id)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        plant_cal_label = ttk.Label(master=self._frame, text="Edit planting date:")
        self._cal = Calendar(
            self._frame,
            selectmode="day",
            year=self._plant_date.year,
            month=self._plant_date.month,
            day=self._plant_date.day,
        )
        edit_planting_date_button = ttk.Button(
            master=self._frame, text="Save", command=self._edit_planting_date
        )
        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            width=30,
            command=lambda: self._show_edit_plantation(self._plant_id),
        )

        plant_cal_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self._cal.grid(row=1, column=0, columnspan=2)
        edit_planting_date_button.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
            sticky=(constants.E, constants.W),
        )
        cancel_button.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
            sticky=(constants.E, constants.W),
        )

        self._root.grid_columnconfigure(0, weight=1)
