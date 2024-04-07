#!/usr/bin/env python3
"""Data processing class."""
import pandas as pd
from typing import List
from dataclasses import dataclass
from enum import Enum, auto
from student import Student
import datetime
import csv


class Assessment(Enum):
    THEORITICAL_PARTICIPATION = auto()
    PRACTICAL_PARTICIPATION = auto()
    THEORITICAL_QUIZ = auto()
    PRACTICAL_QUIZ = auto()
    PROJECTS = auto()
    VIOLATION = auto()


@dataclass
class RecordBook:
    id: str
    assessment: str
    mark: float
    created_at:  datetime
    note: str

#@dataclass
#class Student:
#    id: str
#    name: str
#    classroom: str
#    address: str
#    mobile: str
#    date_created: datetime


class DataProcessing:
    def __init__(self):
        """Initialize class attributes."""
        self.students = []
        self.record_book = []
        #self.record_book = pd.DataFrame(columns=['id', 'name', 'assessment', 'mark', 'date_created', 'note'])

    def load_students_from_file(self) -> None:
        try:
            with open('students_data.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Discard the first row
                for row in reader:
                    #print(row[0])
                    student = Student(id=row[0], 
                            name=row[1],
                            classroom=row[2],
                            address=row[3],
                            mobile=row[4],
                            created_at=datetime.datetime.strptime(row[5], "%Y-%m-%d"))
                    self.students.append(student)
        except FileNotFoundError:
            print("File (students_data.csv) not found !")
        except Exception as e:  # Catch other potential exceptions
            print(f"An error occurred: {e}")
    
    def load_record_book(self) -> None:
        try:
            with open('record_book.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                # Read and discard the first row (header)
                next(reader)  # Discard the first row
                for row in reader:
                    #print(row[0])
                    record_row = RecordBook(id=row[0],
                                            assessment=row[1],
                                            mark=float(row[2]),
                                            created_at=row[3],
                                            note=row[4])
                    self.record_book.append(record_row)
        except FileNotFoundError:
            print("File (record_book.csv) not found !")
        except Exception as e: #Catch other potential exceptions
            print(f"An error occured: {e}")

    def get_students(self, filter=None) -> List:
        """Retrieve all or some students from the list of students"""
        if not filter:
            return self.students
        temp_students = []
        for student in self.students:
            if student.classroom == filter:
                temp_students.append(student)
        return temp_students

    
    def get_student_records(self, student_id: str) -> List:
        """Retrieve all student's marks from the record_book list"""
        student_records = []
        for record in self.record_book:
            if record.id == student_id:
                student_records.append(record)
        return student_records

    def save_student_to_file(self, student: Student) -> None:
        with open('students_data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([student.id, 
                            student.name, 
                            student.classroom,
                            student.address,
                            student.mobile,
                            student.created_at])

    def add_student(self, student: Student) -> None:
        if student:
            self.students.append(student)
            self.save_student_to_file(student)

    def student_match(self, student_id: str) -> bool:
        for student in self.students:
            if student.id == student_id:
                return True
        return False


    def save_mark_to_file(self, student_id, record: RecordBook) -> None:
        """Save mark of a student to the record book file."""
        with open('record_book.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([record.id,
                            record.assessment,
                            record.mark,
                            record.created_at,
                            record.note])

    def add_mark_to_student(self, student_id: str, record: RecordBook) -> None:
        """Add a mark to a student in the record book"""
        if self.student_match(student_id):
            self.record_book.append(record)
            self.save_mark_to_file(student_id, record)
        else:
            print("Sorry, student with this ID ({student_id}) is not found !")


def get_assessment_choice() -> str:
    assessment_list = [Assessment.THEORITICAL_PARTICIPATION,
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
    choice = int(input("?"))
    if choice > 0 and choice < 7:
        return assessment_list[choice-1]
    else:
        return ''


if __name__ == '__main__':
    test = DataProcessing()
    test.load_students_from_file()
    #classroom = input('Enter Classroom code (101-106, 201-206, 301-305): ')
    #if classroom in ['101', '102', '103', '104', '105', '106',
    #                '201', '202', '203', '204', '205',
    #                '301', '302', '303', '304', '305']:
    #    students = test.get_students(classroom)
    #    for student in students:
    #        print(student.name)
    #else:
    #    print(f"Sorry, classroom ({classroom}) is not in our classrooms.")

    test.load_record_book()

    ask = input('Do you want to add a student (Y/N)? ')
    if ask.upper() == 'Y':
        id = input('Enter student ID: ')
        name = input('Enter student name: ')
        classroom = input('Enter classroom: ')
        address = 'Hofuf'
        mobile = '0549282891'
        date_created = datetime.date.today()
        print(date_created)
        test.add_student(Student(id=id, name=name, classroom=classroom, address=address, mobile=mobile, date_created=date_created))
    
    ask = input("Want to add an assessment to a student (Y/N)? ")
    if ask.upper() == 'Y':
        id = input('Enter student ID: ')
        if test.student_match(id):
            assessment = get_assessment_choice()
            mark = float(input("Enter Mark: "))
            date_created = datetime.datetime.today().date()
            note = 'N/A'
            record = RecordBook(id, assessment.name, mark, date_created, note)
            test.add_mark_to_student(id, record)
            
    #if test.get_student_records('87728') != []:
    #    print('There are some records for this student')
    #    print(test.get_student_records('87728'))
    #else:
    #    print('This student has no records yet.')
