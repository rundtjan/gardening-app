from tkinter import Tk
from ui.ui import UI
import sqlite3

def main():
    window = Tk()
    window.title('Gardening journal')
    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__ == "__main__":
    main()