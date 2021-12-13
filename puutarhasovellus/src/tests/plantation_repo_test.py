# pylint: skip-file

import unittest
from repositories.plantation_repo import plantation_repo
from entities.plantation import Plantation

class TestPlantationRepo(unittest.TestCase):
    def setUp(self):
        plantation_repo.delete_all()
        self.plantation_one = Plantation()
        self.plantation_two = Plantation()
        