#!/usr/bin/env python3
import csv
import pandas as pd
from student import Student

class School:
    def __init__(self):
        """Initialize class attributes."""
        self.students = []
        self.students_df = pd.read_csv('students_data.csv')
        #self.students_df = pd.DataFrame(
        #        columns=['id', 'name', 'address', 'mobile', 'classroom'])

    def copy_students_to_list(self):
        for index, row in self.students_df.iterrows():
            self.students.append(Student(
                row['id'], 
                row['name'], 
                row['address'], 
                row['mobile'], 
                row['classroom']))

    def print_students_list(self):
        for student in self.students:
            print(student)

    def new_student(self, student):
        """Add new student to students dataframe."""
        temp_df = pd.DataFrame({
                'id': student.id,
                'name': student.name,
                'address': student.address,
                'mobile': student.mobile,
                'classroom': student.classroom
            }, index=[0])
        self.students_df = pd.concat([self.students_df, temp_df], ignore_index=True)
        # add this student to students list
        self.students.append(student)

    def add_student(self, id, name, address=None, mobile=None, classroom=None):
        """Add new student to students dataframe."""
        temp_df = pd.DataFrame({
                'id': id,
                'name': name,
                'address': address,
                'mobile': mobile,
                'classroom': classroom
            }, index=[0])
        self.students_df = pd.concat([self.students_df, temp_df], ignore_index=True)


    def print_students_df(self):
        print(self.students_df)
