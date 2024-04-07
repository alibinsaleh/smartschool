"""Class to hold student personal data."""
from pydantic import BaseModel, field_validator, model_validator
from typing import List, Optional, Any
from datetime import datetime, date

class Student(BaseModel):
    """
        Class: Student
        Attributes: 
            id: Manditory string to hold student's ID
            name: Manditory string to hold student's full name
            classroom: Manditory string to hold student's classroom
            address: Optional to hold student's address
            mobile: Optional to hold student's mobile phone number
            date_created: Autofilled attribute to hold the date in which the student has been registered.
        
        Model Validator is used to check if id, name and classroom are entered before the object is instantiated.
    """
    id: str
    name: str 
    classroom: str
    address: Optional[str]
    mobile: Optional[str]
    created_at: date

    @model_validator(mode='before')
    @classmethod
    def manditory_fields(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if data['id'] == '':
                raise ValueError("ID must not be empty")
            if data['name'] == '':    
                raise ValueError ("Name must not be empty")
            if data['classroom'] == '':
                raise ValueError ("Classroom must not be empty")
        return data

    #@field_validator('id')
    #@classmethod
    #def id_must_not_be_empty(cls, v: str) -> str:
    #    if v == '':
    #        raise ValueError("ID must not be empty")
    #    return v

    #@field_validator('name')
    #@classmethod
    #def name_must_not_be_empty(cls, v: str) -> str:
    #    if v == '':
    #        raise ValueError ("Name must not be empty")
    #    return v.title()

    #@field_validator('classroom')
    #@classmethod
    #def classroom_must_not_be_empty(cls, v: str) -> str:
    #    if v == '':
    #        raise ValueError ("Classroom must not be empty")
    #    return v
