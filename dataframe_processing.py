"""
Author: Ali A. Almohammed Saleh
Program: dataframe_processing.py
Purpose: A module to handle data as data frames using pandas.
"""
import pandas as pd
import matplotlib.pyplot as plt

class DF:
    """ Data Frame to handle student and mark classes as data frames"""
    def __init__(self, csvfile):
        # self.students_df = pd.DataFrame(columns=['student_id', 'name', 'dob', 'address', 'mobile', 'classroom'])
        self.df = pd.read_csv(csvfile)

    def get_students_dataframe(self):
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

def main():
    students = DF('students_data.csv')
    marks = DF('record_book.csv')
    print(students.get_students_dataframe())
    students_category_count = students.count_by_filter('classroom')
    print(students_category_count)
    students.draw_pie_chart(students_category_count)
    marks_category_count = marks.count_by_filter('assessment')
    print(marks.get_students_dataframe())
    marks.draw_pie_chart(marks_category_count)

main()
