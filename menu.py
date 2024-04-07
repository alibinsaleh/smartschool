#!/usr/bin/env python3
"""Menu system for the followup application."""
import datetime
import sys
import os
import time
import json
from rich.table import Table
from rich import print
from student import Student
from data_processing import DataProcessing, Assessment, RecordBook
from dataframe_processing import StudentDF

sounds_path = './sounds/'

class Menu:
    def __init__(self):
        self.data_processing = DataProcessing()
        self.data_processing.load_students_from_file()
        self.data_processing.load_record_book()
        self.choices = {
		"1": self.new_student,
		"2": self.new_mark,
		"3": self.display_all_students,
                "4": self.display_classroom_students,
                "5": self.display_student_report,
                "6": self.draw_students_totals_pie_chart,
                "7": self.serialize_students,
		"8": self.quit
	}

    def display_menu(self):
        os.system(f"afplay {sounds_path}beep.wav")
        print("""
+++++++++++++++++++++++++++++
+ STUDENTS FOLLOW-UP SYSTEM +
+++++++++++++++++++++++++++++

1. New Student
2. New Mark
3. Display all students
4. Display a classroom students
5. Display a student report
6. Draw Students's totals pie chart
7. Serialize Students Data
8. Quit
	""")

    def run(self):
        """Display menu and respond to choices."""
        while True:
            #os.system('clear')
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    
    def new_student(self):
        os.system(f"afplay {sounds_path}button-15.wav")
        id = input('Enter student ID: ')
        if not self.data_processing.student_match(id):
            name = input('Enter student name: ')
            classroom = input('Enter classroom: ')
            address = 'Hofuf'
            mobile = '0549282891'
            date_created = datetime.date.today()
            try:
                self.data_processing.add_student(Student(id=id, name=name, classroom=classroom, address=address, mobile=mobile, date_created=date_created))
            except ValueError as e:
                print(e)
        else:
            print(f"Sorry, this ID <{id}> is already taken.")

    
    def new_mark(self):
        """Insert a mark for a student"""
        os.system(f"afplay {sounds_path}button-15.wav")
        print("***************************")
        print("*   Add Mark To Student   *")
        print("***************************")
        print()
        student_id = input("Enter student ID: ")
        # check if an id was provided
        if student_id:
            if self.data_processing.student_match(student_id):
                assessment = self.get_assessment_choice()
                mark = float(input("Enter Mark: "))
                date_created = datetime.datetime.today().date()
                note = input("Enter any note or <ENTER> for nothing: ")
                if not note:
                    note = 'n/a'
                record = RecordBook(student_id, assessment.name, mark, date_created, note)
                self.data_processing.add_mark_to_student(student_id, record)
            else:
                os.system(f"afplay {sounds_path}beep-10.wav")
                print(f"Sorry, a student with ({student_id}) is not registered.")
    
        else:
            os.system(f"afplay {sounds_path}button-14.wav")
            print("No ID was provided.")
        input("Press <ENTER> to continue ...")

    def display_all_students(self):
        """Prints all students in a formatted table."""
        os.system(f"afplay {sounds_path}button-15.wav")
        students = self.data_processing.get_students()

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

        for record in self.data_processing.record_book:
            if record.id == student_id:
                print(f"{record.assessment:<25} {record.mark:>5} {record.created_at:>20} {record.note}")

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

    
    def get_assessment_choice(self) -> str:
        assess_list = [Assessment.THEORITICAL_PARTICIPATION,
            Assessment.PRACTICAL_PARTICIPATION,
            Assessment.THEORITICAL_QUIZ,
            Assessment.PRACTICAL_QUIZ, 
            Assessment.PROJECTS,
            Assessment.VIOLATION]
        print("""Select an assessment category:
        1- THEORITICAL PARTICIPATION
        2- PRACTICAL PARTICIPATION
        3- THEORITICAL QUIZ
        4- PRACTICAL QUIZ
        5- PROJECTS
        6- VIOLATION """)
        choice = input(":")
        # check if a correct choice was provided.
        if choice:
            # convert choice to int
            choice = int(choice)
            if choice > 0 and choice < 7:
                return assess_list[choice-1]
        else:
            os.system(f"afplay {sounds_path}button-14.wav")
            print("No ID was provided.")
        return ''
    
    def draw_students_totals_pie_chart(self):
        students = StudentDF('students_data.csv')
        classroom = input("Enter classroom or <ENTER> to terminate: ")
        if classroom != '':
            students.draw_students_totals_pie_chart(int(classroom))


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
    
    def quit(self):
        os.system(f"afplay {sounds_path}button-1.wav")
        print("Thank you for using the FOLLOW-UP APPLICATION.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()

