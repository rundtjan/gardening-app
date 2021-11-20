class Plantation:

    def __init__(self, plant, planting_date, amount_planted, info, user, plantation_id=None, yield_date=None, amount_yield=None):
        self._plant = plant
        self._planting_date = planting_date
        self._amount_planted = amount_planted
        self._yield_date = yield_date
        self._amount_yield = amount_yield
        self._user = user
        self._id = plantation_id

    def __str__(self):
        return f"Planted: {self._plant}, date: {self._planting_date}"