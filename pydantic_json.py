#!/usr/bin/env python3
"""Read students data from JSON file and search for a student by his ID"""
import json
from rich import print as rich_print
from pydantic import BaseModel


class Student(BaseModel):
    """Hold student personal data"""
    id: int
    name: str
    mobile: str


def get_data():
    """Get json data from file"""
    # Path to your JSON file (replace with the actual path)
    file_path = "students_data.json"
    # Open the file in read mode
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            # Load the JSON data into a Python object
            # (usually a dictionary or list)
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: JSON file '{file_path}' not found.")
    return data["students"]


def main():
    """Make jazz noise here"""
    students = get_data()
    print(type(students))
    for student in students:
        s = Student(**student)
        # print(s) # print as json
        rich_print(s.model_dump())  # print as dictionary


if __name__ == "__main__":
    main()
