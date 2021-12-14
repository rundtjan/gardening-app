# pylint: skip-file

import datetime
from tkinter import ttk, StringVar, constants, OptionMenu, IntVar
from services.gardening_service import gardening_service
from functions.functions import create_date_menu


class EditDateView:
    """A class that creates a view where one can edit a planting date."""

    def __init__(self, root, _show_edit_plantation, plant_id, planting_date):
        self._root = root
        self._show_edit_plantation = _show_edit_plantation
        self._frame = None
        self._error_label_var = StringVar()
        self._plant_id = plant_id
        self._plantation = gardening_service.get_plantation_by_id(plant_id)
        self._planting_date = planting_date
        if self._planting_date:
            self._date = self._plantation.get_planting_date()
        else:
            self._date = self._plantation.get_yield_date()
        if not self._date:
            self._date = datetime.datetime.now()
        self._day = IntVar()
        self._month = IntVar()
        self._year = IntVar()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _edit_date(self):
        try:
            date = datetime.datetime(
                year=int(self._year.get()),
                month=int(self._month.get()),
                day=int(self._day.get()),
            )
            if self._planting_date:
                self._plantation.set_planting_date(date)
                gardening_service.update_plantation(self._plantation)
            else:
                self._plantation.set_yield_date(date)
                just_yield_date = True
                gardening_service.update_plantation(self._plantation, just_yield_date)
            self._show_edit_plantation(self._plant_id)
        except Exception as error:
            self._error_label_var.set(str(error))

    def _create_date_menu(self, date, year_var, month_var, day_var):
        year = date.year
        month = date.month
        day = date.day
        years = range(year - 4, year)
        months = range(1, 12)
        days = []
        for i in range(1,32):
            days.append(i)
        year_var.set(year)
        month_var.set(month)
        day_var.set(day)
        dropdown_year = OptionMenu(self._frame, year_var, *years)
        dropdown_month = OptionMenu(self._frame, month_var, *months)
        dropdown_day = OptionMenu(self._frame, day_var, *days)
        return {"day": dropdown_day, "month": dropdown_month, "year": dropdown_year}

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        date_text = "planting"
        if not self._planting_date:
            date_text = "yield"
        plant_cal_label = ttk.Label(
            master=self._frame, text="Edit " + date_text + " date (day/month/year):"
        )
        dropdowns = create_date_menu(self._frame, self._date, self._year, self._month, self._day)

        edit_planting_date_button = ttk.Button(
            master=self._frame, text="Save", command=self._edit_date
        )
        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            width=30,
            command=lambda: self._show_edit_plantation(self._plant_id),
        )

        plant_cal_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        dropdowns["day"].grid(row=1, column=0)
        dropdowns["month"].grid(row=1, column=1)
        dropdowns["year"].grid(row=1, column=2)
        error_label = ttk.Label(
            master=self._frame, textvariable=self._error_label_var, foreground="red"
        )
        error_label.grid(
            row=3,
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            sticky=(constants.E, constants.W),
        )
        edit_planting_date_button.grid(
            row=4,
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            sticky=(constants.E, constants.W),
        )
        cancel_button.grid(
            row=5,
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            sticky=(constants.E, constants.W),
        )

        # self._root.grid_columnconfigure(0, weight=1)
