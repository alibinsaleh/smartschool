"""Class to act as a container for mark attributes."""
from pydantic import BaseModel, field_validator, model_validator
from typing import List, Optional, Any
from datetime import datetime, date

class Mark(BaseModel):
    """
        Class: Mark
        Attributes: 
            id,assessment,mark,created_at,note
            id: Manditory string to hold mark's ID
            assessment: Manditory string to hold mark's category (theoretical and practical participations, projects, violations)
            mark: Manditory float to hold mark
            date_created: Autofilled attribute to hold the date in which the mark has been entered.
        
        Model Validator is used to check if id, assessment, and mark are entered before the object is instantiated.
    """
    id: str
    assessment: str 
    mark: float
    created_at: date
    note: str

    @model_validator(mode='before')
    @classmethod
    def manditory_fields(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if data['id'] == '':
                raise ValueError("ID must not be empty")
            if data['assessment'] == '':    
                raise ValueError ("Assessment must not be empty")
            if data['mark'] == '':
                raise ValueError ("Mark must not be empty")
        return data
    

