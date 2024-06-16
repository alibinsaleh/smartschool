#!/usr/bin/env python3

def convert():
    with open('students_data.csv', 'r') as inFile, open('students_data_cobol_structure.dat', 'w') as outFile:
        read = inFile.readlines()
        for in_row in read:
            out_row = "" 
            temp_list = in_row.split(',')
            out_row += temp_list[0].ljust(10) + ' '
            out_row += temp_list[1].ljust(30) + ' '
            out_row += temp_list[2].ljust(3)  + ' '
            out_row += temp_list[3].ljust(30) + ' '
            out_row += temp_list[4].ljust(15) + ' '
            out_row += temp_list[5].ljust(10) 
            outFile.write(out_row)
            

def main():
    convert()

if __name__ == '__main__':
    main()
