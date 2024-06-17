#!/usr/bin/env python3

import csv
from fpdf import FPDF
from data_processing import DataProcessing

class PDF(FPDF):
    def header(self):
        self.set_font('Courier', 'B', 12)
        #self.cell(0, 10, 'Text to PDF Conversion', 0, 1, 'C')
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Courier', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Courier', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Courier', '', 11)  # Use a fixed-width font
        self.multi_cell(0, 2, body)  # Adjusted line height
        self.ln()


class Report:
    def __init__(self):
        self.data_processing = DataProcessing()
        self.data_processing.load_students_from_file()
        self.data_processing.load_marks_book()
        self.report_lines = []
        


    def student_grades_report(self, student_id):
        self.report_lines.clear()
        found = False
        student_data = None
        for student in self.data_processing.students:
            #print(student.id, student_id, student.id == student_id)
            if student.id == student_id:
                student_data = student
                found = True
                break
        #print(found)
        if found:
            marks = self.data_processing.marks_book
            if marks:
                self.report_lines.append(f"**************************** Student Grade Report **************************")
                self.report_lines.append(f" ")
                self.report_lines.append(f"""
==================== REPORT HEADER =======================
ID: {student_data.id}
Name: {student_data.name}
Classroom: {student_data.classroom}
Address: {student_data.address}
Mobile: {student_data.mobile}
Created At: {student_data.created_at}
	    """)
                self.report_lines.append(f" ")
                self.report_lines.append(f"=================== REPORT DETAILS =======================")
                self.report_lines.append(f" ")
                self.report_lines.append("ASSESSMENT TYPE".ljust(30) + " " + "MARK".ljust(10) + " " + "CREATED AT".ljust(20) + " " + "NOTE".ljust(100))    
                self.report_lines.append(f" ")
                for mark in marks:
                    if mark.id == student_id:
                        self.report_lines.append(mark.assessment.ljust(30) + ' ' +
                                                str(mark.mark).ljust(10) + ' ' + 
                                                str(mark.created_at).ljust(20) + ' ' +
                                                mark.note.ljust(100))

                self.report_lines.append(f" ")
                self.report_lines.append(f"************************** End of Student Grades  Report *******************")
                self.report_lines.append(f" ")
                self.report_lines.append(f"                           Copyright \u00A9  Ali Almohammed Saleh")
                with open('student_grades_report.txt', 'w') as outFile:
                    for line in self.report_lines:
                        outFile.write(line + '\n')
        else:
            print(f"Student with this ID: {student_id} is not found!")
    
    def students_list_report(self, classroom):
        self.report_lines.clear()
        self.report_lines.append(f"********************************************* Students  Report **********************************************")
        self.report_lines.append(f"                                               Classroom ( {classroom.upper()} )                             ")
        self.report_lines.append("=============================================================================================================")
        self.report_lines.append("Student #".ljust(10) + " " +
                                "Name".ljust(30) + " " +
                                "Classroom".ljust(9) + " " +   
                                "Address".ljust(30) + " " +                 
                                "Mobile #".ljust(15) + " " +            
                                "Created At".ljust(10))
        self.report_lines.append("=============================================================================================================")
        self.report_lines.append("                                                                                                        ")
        with open('students_data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                if classroom.upper() == 'ALL':
                    self.report_lines.append(line[0].rjust(10, '0') + ' ' + 
                                            line[1].ljust(30) + ' ' + 
                                            line[2].ljust(9) + ' ' + 
                                            line[3].ljust(30) + ' ' + 
                                            line[4].ljust(15) + ' ' + 
                                            line[5].ljust(10))
                else:
                    if line[2] == classroom:
                        self.report_lines.append(line[0].rjust(10, '0') + ' ' + 
                                                line[1].ljust(30) + ' ' + 
                                                line[2].ljust(9) + ' ' + 
                                                line[3].ljust(30) + ' ' + 
                                                line[4].ljust(15) + ' ' + 
                                                line[5].ljust(10))
                
        self.report_lines.append("=============================================================================================================")
        self.report_lines.append("                                                                                            ")
        self.report_lines.append(f"**************************************** End of Students List  Report **************************************")
        self.report_lines.append(f"                                      Copyright \u00A9  Ali Almohammed Saleh")
        with open('students_list_report.txt', 'w') as outFile:
            for line in self.report_lines:
                outFile.write(line + '\n')

def txt_to_pdf(txt_file, pdf_file):
    pdf = PDF(orientation='L', unit='mm', format='A4')  # Landscape mode
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    with open(txt_file, 'r') as file:
        for line in file:
            pdf.chapter_body(line)
    
    pdf.output(pdf_file)



def main():
    report = Report()
    #classroom = input('Enter Classroom: ')
    report.students_list_report('all')
    student_id = input("Enter Student ID: ")
    report.student_grades_report(student_id)
    
    txt_file = 'students_list_report.txt'  # Path to your text file
    pdf_file = 'students_list_report.pdf'   # Path where you want to save the PDF
    txt_to_pdf(txt_file, pdf_file)
    txt_file = 'student_grades_report.txt'  # Path to your text file
    pdf_file = 'student_grades_report.pdf'   # Path where you want to save the PDF
    txt_to_pdf(txt_file, pdf_file)

if __name__ == '__main__':
    main()
