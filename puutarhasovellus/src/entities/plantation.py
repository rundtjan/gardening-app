import time

class Plantation:

    def __init__(self, username, plant, planting_date, amount_planted, info, yield_date=None, amount_yield=None, plantation_id=None):
        self._plant = plant
        self._planting_date = planting_date
        self._amount_planted = amount_planted
        self._info = info
        self._yield_date = yield_date
        self._amount_yield = amount_yield
        self._username = username
        self._id = plantation_id

    def get_id(self):
        return self._id
    
    def get_plant(self):
        return self._plant
    
    def get_planting_date(self):
        return self._planting_date

    def get_amount_planted(self):
        return self._amount_planted

    def get_info(self):
        return self._info

    def get_yield_date(self):
        return self._yield_date

    def get_amount_yield(self):
        return self._amount_yield

    def set_plant(self, plant):
        self._plant = plant
    
    def set_planting_date(self, planting_date):
        self._planting_date = planting_date

    def set_amount_planted(self, amount_planted):
        self._amount_planted = amount_planted

    def set_info(self, info):
        self._info = info

    def set_yield_date(self, yield_date):
        self._yield_date = yield_date

    def set_amount_yield(self, amount_yield):
        self._amount_yield = amount_yield

    def _timestamp_from_date(self, date):
        if date == "":
            return ""
        return int(time.mktime(date.timetuple()))

    def get_tuple(self):
        return (self._username, self._plant, self._timestamp_from_date(self._planting_date), self._amount_planted, self._info, self._timestamp_from_date(self._yield_date), self._amount_yield)

    def __str__(self):
        return f"Planted: {self._plant}, {self._planting_date.day}/{self._planting_date.month}/{self._planting_date.year}"
