#!/usr/bin/env python3
"""GUI version of my smartschool (aka, students followup system)"""
import tkinter
from tkinter import ttk
from tkinter import messagebox
from student import Student
from typing import List
import csv

# Category options
category_options = [
    "Theoretical Participation",
    "Practical Participation",
    "Theoretical Quiz",
    "Practical Quiz",
    "Projects",
    "Violation"
]

def get_students_list() -> List:
    classroom_list = []
    with open('students_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            classroom_list.append(row)
    return classroom_list

def get_classroom_list(classroom) -> List:
    classroom_list = []
    with open('students_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[2] == str(classroom):
                classroom_list.append(row)
    return classroom_list

def load_classroom_list():
    """ Load - all or by classroom - students data into table (tree) """
    classroom = classroom_entry.get()
    tree.delete(*tree.get_children())
    if classroom == '':
        classroom_list = get_students_list()
    else:
        classroom_list = get_classroom_list(classroom)

    for row in classroom_list:
        student_id = row[0]
        name = row[1]
        classroom = row[2]
        address = row[3]
        mobile = row[4]
        tree.insert('',0, values=[student_id, name, classroom, address, mobile])



# Function to handle dropdown selection and entry retrieval
def handle_category_selection(event):
    selected_category = category_var.get()
    # (Optional) Enable/disable entry field based on selection (e.g., disable for "Violation")
    if selected_category == "Violation":
        value_entry.config(state='disabled')  # Disable entry for Violation
    else:
        value_entry.config(state='normal')  # Enable entry for other categories

def display_marks_entry_window(data):
    # Create a new window (Toplevel)
    marks_entry_window = tkinter.Toplevel(main_window)
    marks_entry_window.title("Marks Entry Window")
    
    frame = tkinter.Frame(marks_entry_window)
    frame.pack(padx=20, pady=10)

    student_frame = tkinter.LabelFrame(frame, text="Student's Data")
    student_frame.grid(row=0, column=0, columnspan=3, sticky='nsew')

    marks_frame = tkinter.LabelFrame(frame, text="Student's Followup Marks")
    marks_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')
    
    # Create labels and display data (assuming data structure)
    student_label1 = tkinter.Label(student_frame, text=f"Name: {data[1]}")
    classroom_label2 = tkinter.Label(student_frame, text=f"Classroom: {data[2]}")
    # ... (Add more labels for other data points)

    # Arrange labels using grid (or pack)
    student_label1.grid(row=1, column=0, sticky='w')
    classroom_label2.grid(row=2, column=0, sticky='w')
    
    # -------------------- Category Selection and Value Entry -------------------
    

    # Selected category variable (StringVar)
    category_var = tkinter.StringVar(frame)
    category_var.set(category_options[0])  # Set default selection

    # Dropdown menu for category selection
    category_dropdown = tkinter.OptionMenu(marks_frame, category_var, *category_options)
    category_dropdown.grid(row=0, column=0)

    # Entry field for value
    value_entry = tkinter.Entry(marks_frame, width=10, bd=2)
    value_entry.grid(row=0, column=1)

    # Bind the dropdown selection event
    category_dropdown.bind('<<ComboboxSelected>>', handle_category_selection)

    # -------------------- Submit Button --------------------
    submit_button = tkinter.Button(frame, text="Submit Marks", command=lambda: submit_marks_data(data, category_var.get(), value_entry.get()))
    submit_button.grid(row=2, column=0, columnspan=3, pady=10)  # Adjust row if needed

    # (Optional) Add functionality to the submit button (submit_marks_data function)

    # Make the window visible
    marks_entry_window.mainloop()



def on_tree_click(event):
    # Get the clicked item IID
    #clicked_item = tree.focus()
    # Get click coordinates relative to the Treeview
    x = event.x
    y = event.y

    # Use coordinates to retrieve the item under the click
    clicked_item = tree.identify('item', x, y)
    # Check if a valid item is clicked (not empty space in the Treeview)
    if clicked_item:
        # Get all data associated with the clicked item
        item_data = tree.item(clicked_item, 'values')
        # Update the label text with specific data (assuming student name is in the first column)
        student_name = item_data[1]  # Access data based on column index
        selected_student_label.config(text=f"Selected Student: {student_name}")
        display_marks_entry_window(item_data)
    else:
        # Handle clicks on empty space (optional)
        pass  # Or display a message like "No row clicked"



main_window = tkinter.Tk()
main_window.title("Students Followup System")

frame = tkinter.Frame(main_window)
frame.pack(padx=20, pady=10)

header = tkinter.Label(frame, text="Classroom Students List")
header.grid(row=0, column=1)

# TreeView
columns = ('id', 'name', 'classroom', 'address', 'mobile')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('id', text='Student Gov. ID')
tree.heading('name', text='Student Name')
tree.heading('classroom', text='Classroom')
tree.heading('address', text="Address")
tree.heading('mobile', text="Mobile #")
tree.column('id', width=100)
tree.column('name', width=200)
tree.column('classroom', width=60)
tree.column('address', width=250)
tree.column('mobile', width=100)
tree.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky='nsew')
# Bind the click event to the Treeview
#tree.bind('<Button-1>', on_tree_click)
tree.bind('<Double-1>', on_tree_click)

# Create the vertical scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tkinter.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)  # Link scrollbar to Treeview
# Arrange widgets using grid
scrollbar.grid(row=1, column=3, sticky='nsew')

# label to display selected student
selected_student_label = tkinter.Label(frame, text='No Student Selected')
selected_student_label.grid(row=2, column=0, columnspan=3, sticky='nsew')

# classroom entry
classroom_entry = tkinter.Entry(frame)
classroom_entry.grid(row=3, column=0)

# Button
btn_load_classroom_list = tkinter.Button(frame, text="Load ClassRoom Students List", command=load_classroom_list)
btn_load_classroom_list.grid(row=3, column=1, columnspan=3, padx=20, pady=10)


main_window.mainloop()
