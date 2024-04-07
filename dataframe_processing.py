"""
Author: Ali A. Almohammed Saleh
Program: dataframe_processing.py
Purpose: A module to handle data as data frames using pandas.
"""
import pandas as pd
import matplotlib.pyplot as plt
from rich import print

class DF:
    """ Data Frame to handle student and mark classes as data frames"""
    def __init__(self, csvfile):
        # self.students_df = pd.DataFrame(columns=['student_id', 'name', 'dob', 'address', 'mobile', 'classroom'])
        self.df = pd.read_csv(csvfile)

    def get_dataframe(self):
        return self.df

    def group_by_filter(self, column):
        if column in self.df:
            return self.df.groupby(column)
        return pd.DataFrame()

    def draw_pie_chart(self, category_size):
        # Prepare pie chart data (category labels and counts)
        pie_chart_data = category_size.values  # Get counts as NumPy array
        pie_chart_labels = category_size.index.to_numpy()  # Get category labels as NumPy array
        # Create the pie chart
        plt.figure(figsize=(6, 6))  # Adjust figure size as desired
        plt.pie(pie_chart_data, labels=pie_chart_labels, autopct="%1.1f%%")  # Add percentages
        plt.title("Distribution of Categories")
        plt.show()
    
    def count_by_filter(self, column):
        if column in self.df:
            return self.df.groupby(column).size()
        return pd.DataFrame()


class MarkDF(DF):
    def __init__(self, marksFile):
        super().__init__(marksFile)


class StudentDF(DF):
    def __init__(self, studentsFile):
        super().__init__(studentsFile)
        self.marks_df = MarkDF('record_book.csv').get_dataframe()
        self.students_totals_df = self.get_students_totals_df()
    
    def get_students_totals_df(self):
        totals_df = pd.DataFrame(columns=['id', 'name', 'classroom', 'total'])
        for index, row in self.df.iterrows():
            # find student in the marks data frame
            student_id_in_marks = self.marks_df[self.marks_df['id'] == row['id']]
            if (not student_id_in_marks.empty):
                total = self.marks_df.groupby('id')['mark'].sum()
                totals_dict = {
                        'id': row['id'], 
                        'name': row['name'], 
                        'classroom': row['classroom'],
                        'total': total[row['id']]
                }
                temp_df = pd.DataFrame(totals_dict, index=[0])
                totals_df  = pd.concat([totals_df, temp_df], ignore_index=True)
        #print(self.students_totals)
        #for key, value in self.students_totals.items():
        #    print(key, value)
        return totals_df

    def get_totals(self):
        return self.students_totals_df

    def draw_students_totals_pie_chart(self, classroom):
        classroom_df = self.students_totals_df[self.students_totals_df['classroom'] == classroom]
        if not classroom_df.empty:
            names = classroom_df['name']
            totals = classroom_df['total']
            # Create the pie chart
            plt.figure(figsize=(10, 8))  # Adjust figure size as desired
            plt.pie(totals, labels=names, autopct="%1.1f%%")  # Add percentages
            plt.title("Distribution of Students's Total Marks")
            plt.show()
        else:
            print(f"Sorry, classroom <{classroom}> is not found.")


def main():
    students = StudentDF('students_data.csv')
    marks = DF('record_book.csv')
    print(students.get_totals())
    #students_category_count = students.count_by_filter('classroom')
    #print(students_category_count)
    classroom = input("Enter classroom or <ENTER> to terminate: ")
    if classroom != '':
        students.draw_students_totals_pie_chart(int(classroom))
    else:
        print("bye")
    #marks_category_count = marks.count_by_filter('assessment')
    #print(marks.get_dataframe())
    #marks.draw_pie_chart(marks_category_count)

main()
