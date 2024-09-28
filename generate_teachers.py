#!/usr/bin/env python3

import csv
import random
from datetime import datetime, timedelta, date
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from enum import Enum, auto
from faker import Faker

# Enum for Subjects
class Subject(Enum):
    MATH = auto()
    RELIGION = auto()
    PHYSICS = auto()
    COMPUTER = auto()
    CHEMISTRY = auto()
    PHYSIOLOGY = auto()

# Teacher model
class Teacher(BaseModel):
    id: str
    name: str
    dob: datetime
    email: EmailStr
    address: str
    subject: Optional[List[Subject]] = None
    created_at: Optional[date] = date.today()

# Initialize Faker for generating random data
fake = Faker()

# Function to generate random subjects for each teacher
def get_random_subjects():
    subjects = list(Subject)
    return random.sample(subjects, k=random.randint(1, 3))  # Each teacher will have 1 to 3 subjects

# Function to generate random teachers
def generate_teachers(n=25):
    teachers = []
    for i in range(1, n + 1):
        teacher = Teacher(
            id=f"T{i:04}",  # Teacher ID like T0001, T0002, etc.
            name=fake.name(),
            dob=fake.date_of_birth(minimum_age=25, maximum_age=60),  # Random DOB between ages 25 and 60
            email=fake.email(),
            address=fake.address(),
            subject=get_random_subjects(),
            created_at=fake.date_this_decade()
        )
        teachers.append(teacher)
    return teachers

# Generate data for 25 teachers
teachers = generate_teachers()

# Write to CSV file
csv_filename = "teachers_data.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["ID", "Name", "DOB", "Email", "Address", "Subjects", "Created At"])
    
    # Write teacher data
    for teacher in teachers:
        writer.writerow([
            teacher.id,
            teacher.name,
            teacher.dob.strftime('%Y-%m-%d'),  # Format date as YYYY-MM-DD
            teacher.email,
            teacher.address,
            ', '.join([subject.name for subject in teacher.subject]),  # Join multiple subjects
            teacher.created_at.strftime('%Y-%m-%d')  # Format created_at date
        ])

print(f"CSV file '{csv_filename}' has been created.")
