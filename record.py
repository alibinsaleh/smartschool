#!/usr/bin/env python3
"""Record a student's performance mark according to command-line flags.
-p = participation
-v = violation
-q = quiz
-pr = practical
-s = search by student id
-sc = search by classroom
"""
import datetime
import argparse
import pandas as pd

followup_registar = pd.read_csv('followup_registar.csv')

def get_args():
    parser = argparse.ArgumentParser(
            description='Password maker',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i',
                        '--int',
                         metavar='int',
                         help='A mark integer',
                         type=int,
                         default=1)
    parser.add_argument('-id',
                        '--student_id',
                         metavar='str',
                         help='Student ID',
                         type=str,
                         default='')
    parser.add_argument('-c',
                        '--classroom',
                         metavar='str',
                         help='Classroom code like (101, 102, ..305)',
                         type=str,
                         default='')
    parser.add_argument('-p', help='Set participation  mark', action='store_true')
    parser.add_argument('-v', help='Set violation mark', action='store_true')
    parser.add_argument('-q', help='Set quiz mark', action='store_true')
    parser.add_argument('-pr', help='Set practical mark', action='store_true')
    parser.add_argument('-s', help='Search by student id', action='store_true')
    parser.add_argument('-sc', help='Search by classroom',action='store_true')
    return parser.parse_args()

def record_mark(flag):
    global followup_registar
    student_id = flag.student_id
    classroom = flag.classroom
    if flag.s:
        df = search_by_student_id(int(student_id))
        print(df)
    elif flag.sc:
        df = search_by_classroom(int(classroom))
        print(df)
    else:
        if flag.p:
            performance_type = 'Participation'
        if flag.q:
            performance_type = 'Quiz'
        if flag.v:
            performance_type = 'Violation'
        if flag.pr:
            performance_type = 'Practical'
        print(f"A mark inserted for this student (ID: {student_id}) as a {performance_type}.")
        temp_dic = {
            'id': student_id,
            'classroom': classroom,
            'type': performance_type,
            'mark': flag.int,
            'date_created': datetime.date.today(),
            'note': ''
        }
        temp = pd.DataFrame(temp_dic, index=[0])
        followup_registar = pd.concat([followup_registar, temp], ignore_index=True)
        print(followup_registar)
        followup_registar.to_csv('followup_registar.csv', index=False)

def search_by_student_id(student_id):
    global followup_registar
    return followup_registar[followup_registar['id'] == student_id]

def search_by_classroom(classroom):
    global followup_registar
    return followup_registar[followup_registar['classroom'] == classroom]

if __name__ == "__main__":
    args = get_args()
    record_mark(args)
    

