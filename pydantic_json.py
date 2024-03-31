#!/usr/bin/env python3
import requests
import json
from rich import print
from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    mobile: str

def get_data():
    # Path to your JSON file (replace with the actual path)
    file_path = "students_data.json"
    # Open the file in read mode
    try:
        with open(file_path, "r") as json_file:
            # Load the JSON data into a Python object (usually a dictionary or list)
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: JSON file '{file_path}' not found.")
    return data["students"]


def main():
    students = get_data()
    print(type(students))
    for student in students:
        s = Student(**student)
        # print(s) # print as json
        print(s.model_dump()) # print as dictionary
        
if __name__ == "__main__":
    main()
