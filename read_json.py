#!/usr/bin/env python3
import json
import requests
from rich import print
from pydantic import BaseModel, field_validator

class Student(BaseModel):
    id: str
    name: str
    classroom: str
    address: str

    @field_validator('id')
    def check_id_length(cls, value):
        if len(value) < 3:
            raise ValueError("ID should be 10 digits long.")
        return value
    
    @field_validator('name')
    def check_name_length(cls, value):
        if len(value) > 20:
            raise ValueError("Name should not exceeds 20 characters long.")
        return value


def get_data():
    try:
        with open('students_data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Sorry, file is not found!")
    return data['students']


def main():
    students = get_data()
    s = [Student(**student) for student in students]
    print(s)

if __name__ == "__main__":
    main() 
