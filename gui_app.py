#!/usr/bin/env python3
import tkinter as tk
import subprocess
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
                command=self.open_second_window)
        second_window_button.pack()
        self.create_pdf_listbox()
        pdf_button = tk.Button(self.main_window, text="Open Report", command=self.open_report)
        pdf_button.pack()
        
    def create_pdf_listbox(self):
        self.pdf_listbox = tk.Listbox(self.main_window, height=3, width=30)
        self.pdf_listbox.pack()
        self.pdf_listbox.insert(tk.END, 'students_list_report')
        self.pdf_listbox.insert(tk.END, 'student_grades_report')
        self.pdf_listbox.insert(tk.END, 'normal_text_file')
    
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

    def open_report(self):
        selected_report = self.pdf_listbox.get(self.pdf_listbox.curselection())
        pdf_path = selected_report + ".pdf"
        # Open the PDF file with the default application
        subprocess.run(["open", pdf_path])

    def start_app(self):
        Menu().run()
    
def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
