#!/usr/bin/env python
import pandas as pd
import csv

"""School class to manage school's entities"""
class School:
	def __init__(self):
		self.students = []

	def load_students_from_file(self):
		with open('data.csv', 'r') as csvfile:
			reader = csv.reader(csvfile)
			for r in reader:
				print(r)


"""Student class to process student personal data."""
class Student:
	def __init__(self, id, name, classroom, address, mobile):
		self.id = id
		self.name = name
		self.classroom = classroom
		self.address = address
		self.mobile = mobile
		self.df = pd.DataFrame(columns=['id', 'name', 'classroom', 'address', 'mobile'])


	def add_student_to_dataframe(self, id, name, classroom, address, mobile):
		temp = pd.DataFrame({'id': id,
				'name': name,
				'classroom': classroom,
				'address': address,
				'mobile': mobile}, index=[0])
		
		self.df = pd.concat([self.df, temp], ignore_index=True)

	def print_df(self):
		print(self.df)
	
			
	def print_details(self):
		"""Print student's details on screen"""
		print(f"ID: {self.id}")
		print(f"Name: {self.name}")
		print(f"Classroom: {self.classroom}")
		print(f"Address: {self.address}")
		print(f"mobile: {self.mobile}")


if __name__ == "__main__":
	s1 = Student(1, "Ali", "201", "Hofuf", "054000000")
	s1.print_details()
	s1.add_student_to_dataframe(2, 'Abbass', '202', 'Dammam', '05411111')
	s1.print_df()

	school = School()
	school.load_students_from_file()

