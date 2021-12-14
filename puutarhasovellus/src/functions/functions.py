import time
from tkinter import OptionMenu

def timestamp_from_date(date):
    if not date:
        return -1
    return int(time.mktime(date.timetuple()))

def create_date_menu(root, date, year_var, month_var, day_var):
    year = date.year
    month = date.month
    day = date.day
    years = range(year - 4, year)
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    days = []
    for i in range(1,32):
        days.append(i)
    year_var.set(year)
    month_var.set(month)
    day_var.set(day)
    dropdown_year = OptionMenu(root, year_var, *years)
    dropdown_month = OptionMenu(root, month_var, *months)
    dropdown_day = OptionMenu(root, day_var, *days)
    return {"day": dropdown_day, "month": dropdown_month, "year": dropdown_year}