from tkinter import ttk, StringVar, constans
from services.gardening_service import gardening_service

class LoginView:
    def __init__(self, root, show_mainview, show_registration, show_adminview):
        self._root = root
        self._show_mainview = show_mainview
        self._show_registration = show_registration
        self._show_adminview = show_adminview
        #continue filling up all variables and then self.initialize()
