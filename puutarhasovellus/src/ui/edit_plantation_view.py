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
        self._cal = None
        self._date = datetime.datetime.now()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _save_plantation(self):
        self._plantation.set_plant(self._plant_entry.get())
        self._plantation.set_amount_planted(self._amount_planted_entry.get())
        self._plantation.set_info(self._info_entry.get())
        
        try:
            gardening_service.update_plantation(self._plantation)
            self._show_mainview()
        except Exception as error:
            self._error_label_var.set(str(error))

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Edit the plantation")
        error_label = ttk.Label(
            master=self._frame, textvariable=self._error_label_var, foreground="red")
        edit_planting_date_button = ttk.Button(master=self._frame, text="Edit planting date: " + str(self._plant_date.day) + "/" + str(self._plant_date.month) + "/" + str(self._plant_date.year), command=lambda: self._edit_planting_date(self._plant_id))
        plant_label = ttk.Label(master=self._frame, text="Which plant?")
        self._plant_entry = ttk.Entry(master=self._frame)
        self._plant_entry.insert(0, self._plantation.get_plant())
        amount_label = ttk.Label(master=self._frame, text="How much did you plant?")
        self._amount_planted_entry = ttk.Entry(master=self._frame, width=30)
        self._amount_planted_entry.insert(0, self._plantation.get_amount_planted())
        info_label = ttk.Label(master=self._frame, text="Any other relevant info?")
        self._info_entry = ttk.Entry(master=self._frame, width=30)
        self._info_entry.insert(0, self._plantation.get_info())
        edit_yield_date_button = ttk.Button(master=self._frame, text="Edit yield date (coming up)", command=lambda: self._edit_yield_date(self._plant_id))
        add_button = ttk.Button(master=self._frame, text="Save", command=self._save_plantation)
        cancel_button = ttk.Button(master=self._frame, text="Cancel", width=30, command=self._show_mainview)
        
        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        edit_planting_date_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        plant_label.grid(row=3, column=0, columnspan=2)
        self._plant_entry.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        amount_label.grid(row=5, column=0, columnspan=2)
        self._amount_planted_entry.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        info_label.grid(row=7, column=0, columnspan=2)
        self._info_entry.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        edit_yield_date_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        error_label.grid(row=10, column=1, padx=5, pady=5)
        add_button.grid(row=11, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        cancel_button.grid(row=12, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))

        self._root.grid_columnconfigure(0, weight=1)
