import time
import datetime
from tkinter import ttk, StringVar, constants
from tkcalendar import Calendar
from services.gardening_service import gardening_service, LoginError

class AddPlantationView:
    def __init__(self, root, show_mainview):
        self._root = root
        self._show_mainview = show_mainview
        self._frame = None
        self._error_label_var = StringVar()
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
        date = self._cal.get_date()
        timestring = "%m/%d/%y"
        #this is a fix for the calendar emitting data in different form on Linux:
        if len(date.split("/")[2]) == 4:
             timestring ="%d/%m/%Y"
        date = datetime.datetime.strptime(date, timestring)
        plant = self._plant_entry.get()
        amount_planted = self._amount_planted_entry.get()
        info = self._info_entry.get()
        try:
            gardening_service.create_plantation(plant, date, amount_planted, info)
            self._show_mainview()
        except Exception as error:
            self._error_label_var.set(str(error))

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Add a new plantation")
        error_label = ttk.Label(
            master=self._frame, textvariable=self._error_label_var, foreground="red")
        self._cal = Calendar(self._frame, selectmode = "day", year=self._date.year, month=self._date.month, day=self._date.day)
        plant_label = ttk.Label(master=self._frame, text="Which plant?")
        self._plant_entry = ttk.Entry(master=self._frame)
        amount_label = ttk.Label(master=self._frame, text="How much did you plant?")
        self._amount_planted_entry = ttk.Entry(master=self._frame, width=30)
        info_label = ttk.Label(master=self._frame, text="Any other relevant info?")
        self._info_entry = ttk.Entry(master=self._frame, width=30)


        add_button = ttk.Button(master=self._frame, text="Save", command=self._save_plantation)
        cancel_button = ttk.Button(master=self._frame, text="Cancel", width=30, command=self._show_mainview)
        
        label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self._cal.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        plant_label.grid(row=2, column=0, columnspan=2)
        self._plant_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        amount_label.grid(row=4, column=0, columnspan=2)
        self._amount_planted_entry.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        info_label.grid(row=6, column=0, columnspan=2)
        self._info_entry.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        error_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
        add_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))
        cancel_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky=(constants.E, constants.W))

        self._root.grid_columnconfigure(0, weight=1)
