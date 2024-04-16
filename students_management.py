"""
Author: Ali A. Almohammed Saleh
Program: students_management.py
Purpose: Display a menu related to students, like adding, editing, deleting, etc.
"""
import datetime
import os
import json
from rich.table import Table
from rich import print
from student import Student
from data_processing import DataProcessing
from dataframe_processing import StudentDF

sounds_path = './sounds/'

class StudentsManagement:
    def __init__(self):
        self.data_processing = DataProcessing()
        self.data_processing.load_students_from_file()
        self.data_processing.load_marks_book()
        self.choices = {
            "1": self.add_student,
            "2": self.edit_student,
            "3": self.delete_student,
            "4": self.display_all_students,
            "5": self.display_classroom_students,
            "6": self.display_student_report,
            "7": self.draw_students_totals_pie_chart,
            "8": self.serialize_students,
            "9": self.back
	}

    def display_menu(self):
        os.system(f"afplay {sounds_path}beep.wav")
        print("""
++++++++++++++++++++++++++++++
+  STUDENTS MANAGEMENT MENU  +
++++++++++++++++++++++++++++++

1. Add Student
2. Edit Student
3. Delete Student
4. Display all students
5. Display classroom students
6. Display student report
7. Draw Students's totals pie chart
8. Serialize Students Data
9. <- Back
	""")

    def run(self):
        """Display students management menu and respond to choices."""
        loop = True
        while loop:
            #os.system('clear')
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                loop = action()
            else:
                print("{0} is not a valid choice".format(choice))
                break

    def add_student(self):
        id = input('Enter student ID: ')
        if not self.data_processing.student_match(id):
            name = input('Enter student name: ')
            classroom = input('Enter classroom: ')
            address = 'Hofuf'
            mobile = '0549282891'
            created_at = datetime.date.today()
            try:
                self.data_processing.add_student(Student(id=id, name=name, classroom=classroom, address=address, mobile=mobile, created_at=created_at))
            except ValueError as e:
                print(e)
        else:
            print(f"Sorry, this ID <{id}> is already taken.")
        return True

    def edit_student(self):
        student_id = input("Enter student ID: ")
        # check if an id was provided
        if student_id:
            found = False
            changed = False
            for student in self.data_processing.students:
                if student.id == student_id:
                    found = True
                    idx = self.data_processing.students.index(student)
                    print(f"Current Name: {student.name}")
                    new_name = input('Enter new student name or < ENTER > to keep it: ')
                    if new_name:
                        name = new_name
                        changed = True
                    else:
                        name = student.name
                    print(f"Current Classroom: {student.classroom}")
                    new_classroom = input('Enter new classroom or < ENTER > to keep it: ')
                    if new_classroom:
                        classroom = new_classroom
                        changed = True
                    else:
                        classroom = student.classroom
                    address = 'Hofuf'
                    mobile = '0549282891'
                    created_at = datetime.date.today()
                    if changed:
                        try:
                            self.data_processing.students[idx] = Student(id=student_id, name=name, classroom=classroom, address=address, mobile=mobile, created_at=created_at)
                            self.data_processing.save_all_students_to_file(self.data_processing.students)
                            print(f"Student with this ID < {student_id} > is successfully updated.")
                            break
                        except ValueError as e:
                            print(e)
                    else:
                        print(f"Sorry, no changes on student's data.")
            if not found:
                print(f"Sorry, student with this ID < {student_id} > is not found!")
        else:
            print("Sorry, no student ID is provided!")
        
        input("Press < ENTER > to continue ...")
        return True

    def delete_student(self):
        pass
        return True
    
    
    

    def display_all_students(self):
        """Prints all students in a formatted table."""
        os.system(f"afplay {sounds_path}button-15.wav")
        students = self.data_processing.get_students()
        if len(students) > 0:
            # Find maximum lengths for each column
            id_length = max(len(str(student.id)) for student in students) + 1
            name_length = max(len(student.name) for student in students) + 1
            classroom_length = max(len(student.classroom) for student in students) + 1
        # --------------------  Printing report without using rich module's print --------------
        # Print table header
        
        #print(f"{'ID':<{id_length}} {'Name':<{name_length}} {'Classroom':<{classroom_length}}")
        #print("-" * (id_length + name_length + classroom_length + 4))

        # Print each student data in a formatted row
        #for student in students:
        #    print(f"{student.id:{id_length}} {student.name:{name_length}} {student.classroom:{classroom_length}}")
        #--------------------- END of normal way to print report without using rich module -------

        # Print the same students data - as above - using rich module's print and table
        table = Table(title="All Students List", show_header=True)
        table.add_column("ID", style="green", justify="left")
        table.add_column("Name", style="magenta", justify="left")
        table.add_column("Classroom", justify="right")

        for student in students:
            table.add_row(student.id, student.name, student.classroom)

        print(table)

        # Optional: Prompt to continue (if needed)
        input("Press <ENTER> to continue...")

        return True
    
    def display_classroom_students(self):
        os.system(f"afplay {sounds_path}button-15.wav")
        classroom = input("Enter classroom (Ex. 101, 201..etc.): ")
        students = self.data_processing.get_students(classroom)
        # Print classroom  students list using rich module's print and table classes
        table = Table(title="Classroom {classroom} Students List", show_header=True)
        table.add_column("ID", style="green", justify="left")
        table.add_column("Name", style="magenta", justify="left")
        table.add_column("Classroom", justify="right")
        for student in students:
            table.add_row(student.id, student.name, student.classroom)
        print(table)
        # Optional: Prompt to continue (if needed)
        input("Press <ENTER> to continue...")
        return True

    def print_report_header(self, student):
        print(f"""
==================== REPORT HEADER =======================
ID: {student.id}
Name: {student.name}
Classroom: {student.classroom}
Address: {student.address}
Mobile: {student.mobile}
Created At: {student.created_at}
	    """)
	

    def print_report_details(self, student_id):
        """Prints the report details for a specific student."""

        print("======================= REPORT DETAILS ====================")
        print()

        print(f"{'Assessment':<25} {'Mark':>5} {'Created At':>20} {'Note'}")
        print("-" * (25 + 5 + 20 + len("Note") + 6))  # Calculate total separator length

        for mark in self.data_processing.marks_book:
            if mark.id == student_id:
                print(f"{mark.assessment:<25} {mark.mark:>5} {mark.created_at:>20} {mark.note}")

        print()
        print("======================= END OF REPORT ====================")

    def display_student_report(self):
        os.system(f"afplay {sounds_path}button-15.wav")
        student_id = input("Enter student ID: ")
        found_student = False
        for student in self.data_processing.students:
            if student.id == student_id:
                found_student = True
                self.print_report_header(student)
                break
        if found_student:
            self.print_report_details(student_id)
        else:
            print(f"Sorry, student with this id ({student_id}) is not found.")
        input("Press <ENTER> to continue...")
        return True

    def draw_students_totals_pie_chart(self):
        students = StudentDF('students_data.csv')
        classroom = input("Enter classroom or <ENTER> to terminate: ")
        if classroom != '':
            students.draw_students_totals_pie_chart(int(classroom))
        return True

    def serialize_students(self):
        """Serialize students personal data into JSON format"""
        students_data = []
        for student in self.data_processing.students:
            student_dict = {
                'id': student.id,
                'name': student.name,
                'address': student.address,
                'mobile': student.mobile,
                'classroom': student.classroom
            }
            students_data.append(student_dict)
        # Create a dictionary with the desired name as the key and student data as the value
        data = {
            "students": students_data  # 'students' is the chosen name
        }

        # Dump the list of dictionaries to a JSON file (optional)
        with open("students_data.json", "w") as outfile:
            json.dump(data, outfile, indent=4)  # Add indent for readability

        # Or, print the JSON string to the console
        print(json.dumps(data, indent=4))
        input("Press <ENTER> to continue ...")
        return True
    
    def back(self):
        return False
