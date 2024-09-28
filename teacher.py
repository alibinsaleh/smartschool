#!/usr/bin/env python3
import datetime
import re
from typing import List, Optional
from pydantic import BaseModel, EmailStr, validator, field_validator
from enum import Enum, auto



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
    address: str
    subjects: List[Subject] | Optional[Subject]
    created_at: Optional[datetime.datetime] = datetime.date.today()
    
    @field_validator('email')
    def validate_email(cls, value):
        # Replace with a more comprehensive regular expression for email validation
        pattern = r"^[^@]+@[^@]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, value):
            raise ValueError("Invalid email format")
        return value


# if __name__ == "__main__":
#     t = Teacher(id='1001', name='Ali Almohammed Saleh', dob=datetime.date.today(), email='alibinsaleh@gmail.com', subject=[Subject.COMPUTER, Subject.MATH])
#     print(t)

