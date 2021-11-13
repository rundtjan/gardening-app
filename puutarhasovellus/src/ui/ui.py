from tkinter import Tk, ttk

class UI:
    def __init__(self, root):
        self._root = root
        self.userEntry = None
        self.pwEntry = None

    def start(self):
        userLabel = ttk.Label(master=self._root, text="Username")
        self.userEntry = ttk.Entry(master=self._root)
        passwordLabel = ttk.Label(master=self._root, text="Password")
        self.pwEntry = ttk.Entry(master=self._root)
        loginButton = ttk.Button(master=self._root, text="Login", command=self._handle_login)
        regButton = ttk.Button(master=self._root, text="Register", command=self._handle_register)
        userLabel.pack()
        self.userEntry.pack()
        passwordLabel.pack()
        self.pwEntry.pack()
        loginButton.pack()
        regButton.pack()

    def _handle_login(self):
        username = self.userEntry.get()
        password = self.pwEntry.get()
        print(f"Looks like {username} has password {password}")

    def _handle_register(self):
        print("So you want to register")
