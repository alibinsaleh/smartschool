#!/usr/bin/env python3
import sqlite3
import csv
from typing import List

class DB:
    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def read_csv_file(self, file_name) -> List:
        rows = []
        with open(file_name, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            for line in csv_reader:
                rows.append(line)
        return rows
    
    def insert_from_file_into_sql(self, csvfile) -> None:
        # Create a table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            classroom TEXT,
            address TEXT,
            mobile TEXT,
            created_at DATE
            )
            ''')
    
        students_list = self.read_csv_file(csvfile)
        for student in students_list:
            print(f"Copying student: {student[1]} ...")
            sql = f"""
                INSERT INTO students 
                (id, name, classroom, address, mobile, created_at) 
                VALUES (?,?,?,?,?,?) 
            """
            self.cursor.execute(sql, (student[0], student[1], student[2], 
                student[3], student[4], student[5]))

    def select_records(self) -> None:
        sql = "SELECT * FROM students"
        for row in self.cursor.execute(sql):
            print(row)




def main() -> None:
    db = DB('students.db')
    db.insert_from_file_into_sql('students_data.csv')
    db.select_records()

if __name__ == "__main__":
    main()
