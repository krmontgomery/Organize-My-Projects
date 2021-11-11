from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from datetime import datetime

class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title('Organize')
        self.build_widgets()
        self.run_application()

    def build_widgets(self):
        self.root.geometry('400x400')
        self.myLabel = Label(text="This is my text").pack()
        self.myprojects = Text

    def run_application(self):
        self.root.mainloop()

if __name__ == "__main__":
    Application()
    