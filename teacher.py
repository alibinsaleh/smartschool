#!/usr/bin/env python3
from pydantic import BaseModel, EmailStr, validator, field_validator
from enum import Enum, auto
import datetime
import re


class Subject(Enum):
    MATH = auto()
    RELIGEON = auto()
    PHYSICS = auto()
    COMPUTER = auto()
    CHEMESTRY = auto()
    PHYSIOLOGY = auto()


class Teacher(BaseModel):
    id: str
    name: str
    dob: datetime.datetime
    email: EmailStr
    subject: Subject
    
    @field_validator('email')
    def validate_email(cls, value):
        # Replace with a more comprehensive regular expression for email validation
        pattern = r"^[^@]+@[^@]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, value):
            raise ValueError("Invalid email format")
        return value


if __name__ == "__main__":
    t = Teacher(id='1001', name='Ali Almohammed Saleh', dob=datetime.datetime.now(), email='alibinsaleh@gmail.com', subject=Subject.COMPUTER)
    print(t)

