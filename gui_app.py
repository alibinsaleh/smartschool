#!/usr/bin/env python3
import tkinter as tk
from menu import Menu
from data_processing import DataProcessing

class App:
    def __init__(self, window):
        self.data_processing = DataProcessing()
        self.data_processing.load_students_from_file()
        self.main_window = window
        self.main_window.title("Main Window")
        self.create_widgets()

    def create_widgets(self):
        button = tk.Button(self.main_window, text="START APPLICATION", command=self.start_app)
        button.pack()
        second_window_button = tk.Button(self.main_window, 
                text="Second Window", 
                command=self.open_second_window).pack()

    def open_second_window(self):
        second_window = tk.Toplevel(self.main_window)
        #second_window.size("600X600")
        second_window.title("Second Window")
        students = self.data_processing.get_students()
        listbox = tk.Listbox(second_window, height=10, width=50)
        listbox.pack()
        for student in students:
            item = student.id.ljust(10) + ' ' + student.name.ljust(30) + ' ' +  student.classroom
            listbox.insert(tk.END, item)


    def start_app(self):
        Menu().run()
    
def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
