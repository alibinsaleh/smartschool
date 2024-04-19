from docxtpl import DocxTemplate
from student import Student
from typing import List
import csv

def get_classroom_list(classroom) -> List:
    classroom_list = []
    with open('students_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            classroom_list.append(row)
    return classroom_list
    
doc = DocxTemplate("classroom_list_template.docx")

classroom_list = get_classroom_list(101)

doc.render({"classroom": "201",
            "classroom_list": classroom_list})
doc.save("classroom_list.docx")
