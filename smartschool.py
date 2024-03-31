#!/usr/bin/env python3
"""Main program"""
import argparse
from school import School
from student import Student

def get_args():
    """Get comman-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('user')
    parser.add_argument('-u',
            '--username',
            help='Username to access special data processing, otherwise access regular processes.',
            metavar='str',
            type=str,
            default='')
    return  parser.parse_args()


if __name__ == "__main__":
    school = School()
    if get_args() == 'alibinsaleh':
        s1 = Student(1011, 'Ali Almohammed Saleh', 'Hofuf', '054-928-2891', 'Science 101')
        school.new_student(s1)
        print(s1)
    else:
        school.add_student(1011, 'Fahad Aldosari', 'Hofuf', '054-928-2891', 'Science 101')
        school.add_student(1012, 'Hani Saleh', 'Hofuf', '054-928-2891', 'Science 101')
        school.add_student(1013, 'Shaker Maker', 'Hofuf', '054-928-2891', 'Science 101')
    school.print_students_df()
    school.copy_students_to_list()
    school.print_students_list()
