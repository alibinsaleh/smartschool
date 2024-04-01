#!/usr/bin/env python3
"""Searching json data for a match."""
import json
from rich import print
from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    id: str
    name: str
    address: str
    mobile: str
    classroom: str

def get_data():
    try:
        with open('students_data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found!")
    return data['students']

def student_match(student_id: str) -> List:
    students = get_data()
    found_students = []
    for student in students:
        if student_id in student['id']:
            found_students.append(student)
    if len(found_students) > 0:
        return found_students
    else:
        return 'Not Found'


def main():
    students = get_data()
    s = [Student(**student) for student in students]
    print(s)

if __name__ == "__main__":
    main()
    student_id = input("Enter student id to search for: ")
    found = student_match(student_id)
    print(found)
