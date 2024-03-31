#!/usr/bin/env python3
"""Student's Follow-up program to record marks of students performance during class."""
import pandas as pd

class Followup:
    """Class to manage students performances"""
    def __init__(self):
        """Initial Followup class attributes."""
        self.students = []
        self.followup_registar = pd.DataFrame(columns=['id', 'classroom', 'type', 'mark', 'date_created', 'note'])
        
    def insert_mark(self, performance_type, mark):
        pass
