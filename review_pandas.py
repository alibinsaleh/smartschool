#!/usr/bin/env python3
"""
Authour: Ali A. Almohammed Saleh
Purpose: Create New Sudents and save them into dataframe.
Program: review_pandas.py
Date Created: 05/04/2024
"""
import random
from dataclasses import dataclass
import pandas as pd
from faker import Faker


@dataclass
class StudentData:
    """Student data class"""
    student_id: int
    name: str
    dob: str
    address: str
    mobile: str


class Student:
    """ Main Student class to manipulate student data
        (id, name, date of birth, address, mobile)
        from StudentData class
    """
    def __init__(self):
        """Initialize student's class attributes."""
        self.students_df = pd.DataFrame(columns=[
            'student_id',
            'name',
            'dob',
            'address',
            'mobile'])

    def new_student(self, student: StudentData):
        """Create a new student"""
        student_dict = {
            'student_id': student.student_id,
            'name': student.name,
            'dob': student.dob,
            'address': student.address,
            'mobile': student.mobile
        }
        temp_df = pd.DataFrame(student_dict, index=[0])
        self.students_df = pd.concat([self.students_df, temp_df],
                                     ignore_index=True)

    def get_df(self):
        """Returns students dataframe"""
        return self.students_df


def main():
    """Make jazz noize here"""
    fake = Faker()

    # Generate DataFrame with random customer data
    data = {'student_id': [fake.random.randint(1001, 1111) for _ in range(10)],
            'name': [fake.name() for _ in range(10)],
            'dob': [fake.date() for _ in range(10)],
            'address': [fake.address() for _ in range(10)],
            'mobile': [fake.phone_number() for _ in range(10)]}
    # find the longes address
    lengths = [len(x) for x in data['address']]
    print(data['address'][lengths.index(max(lengths))])
    s = Student()
    for i in range(10):
        sd = StudentData(data['student_id'][i],
                         data['name'][i],
                         data['dob'][i],
                         data['address'][i],
                         data['mobile'][i])
        s.new_student(sd)
    print(s.get_df())


if __name__ == "__main__":
    main()
