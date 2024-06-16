#!/usr/bin/env python3

with open('students_data.csv', 'r') as f:
    lines = [line.strip() for line in f]
    for line in lines:
        print(line)


