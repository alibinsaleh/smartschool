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
from mark import Mark
from data_processing import DataProcessing, Assessment
from dataframe_processing import StudentDF
from marks_management import MarksManagement
from students_management import StudentsManagement
from maintenance import Maintenance

sounds_path = './sounds/'

class Menu:
    def __init__(self):
        self.data_processing = DataProcessing()
        self.data_processing.load_students_from_file()
        self.data_processing.load_marks_book()
        self.choices = {
            "1": self.students_management,
            "2": self.marks_management,
            "3": self.maintenance,
            "8": self.quit
	    }

    def display_menu(self):
        os.system(f"afplay {sounds_path}beep.wav")
        print("""
+++++++++++++++++++++++++++++
+ STUDENTS FOLLOW-UP SYSTEM +
+++++++++++++++++++++++++++++

1. Students Management Menu
2. Marks Management Menu
3. Maintenance
8. Quit
	""")

    def run(self):
        """Display menu and respond to choices."""
        while True:
            os.system('clear')
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    
    def students_management(self):
        """Manage students like (add, edit, delete, etc.)"""
        StudentsManagement(self.data_processing).run()


    def marks_management(self):
        """Manage marks like (add, edit, delete, etc.)"""
        MarksManagement(self.data_processing).run()

    
#    def new_mark(self):
#        """Insert a mark for a student"""
#        os.system(f"afplay {sounds_path}button-15.wav")
#        print("***************************")
#        print("*   Add Mark To Student   *")
#        print("***************************")
#        print()
#        student_id = input("Enter student ID: ")
#        # check if an id was provided
#        if student_id:
#            if self.data_processing.student_match(student_id):
#                assessment = self.get_assessment_choice()
#                mark = float(input("Enter Mark: "))
#                date_created = datetime.datetime.today().date()
#                note = input("Enter any note or <ENTER> for nothing: ")
#                if not note:
#                    note = 'n/a'
#                mark = MarkBook(student_id, assessment.name, mark, date_created, note)
#                self.data_processing.add_mark_to_student(student_id, mark)
#            else:
#                os.system(f"afplay {sounds_path}beep-10.wav")
#                print(f"Sorry, a student with ({student_id}) is not registered.")
#    
#        else:
#            os.system(f"afplay {sounds_path}button-14.wav")
#            print("No ID was provided.")
#        input("Press <ENTER> to continue ...")
#
#    
#    def get_assessment_choice(self) -> str:
#        assess_list = [Assessment.THEORITICAL_PARTICIPATION,
#            Assessment.PRACTICAL_PARTICIPATION,
#            Assessment.THEORITICAL_QUIZ,
#            Assessment.PRACTICAL_QUIZ, 
#            Assessment.PROJECTS,
#            Assessment.VIOLATION]
#        print("""Select an assessment category:
#        1- THEORITICAL PARTICIPATION
#        2- PRACTICAL PARTICIPATION
#        3- THEORITICAL QUIZ
#        4- PRACTICAL QUIZ
#        5- PROJECTS
#        6- VIOLATION """)
#        choice = input(":")
#        # check if a correct choice was provided.
#        if choice:
#            # convert choice to int
#            choice = int(choice)
#            if choice > 0 and choice < 7:
#                return assess_list[choice-1]
#        else:
#            os.system(f"afplay {sounds_path}button-14.wav")
#            print("No ID was provided.")
#        return ''
    
    def maintenance(self):
        """Back up and restore data from files."""
        Maintenance().run()

    def quit(self):
        os.system(f"afplay {sounds_path}button-1.wav")
        print("Thank you for using the FOLLOW-UP APPLICATION.")
        sys.exit(0)

def main():
    Menu().run()

if __name__ == "__main__":
    main()

