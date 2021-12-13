import datetime
import time
import unittest
from functions.functions import timestamp_from_date

class TestFunctions(unittest.TestCase):
    def test_that_returns_minus_one_if_no_date(self):
        self.assertEqual(-1, timestamp_from_date(None))
    
    def test_that_returns_timestamp_if_date_is_present(self):
        date = datetime.datetime.now()
        timestamp = int(time.mktime(date.timetuple()))
        self.assertEqual(timestamp, timestamp_from_date(date))