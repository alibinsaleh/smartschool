"""
Author: Ali A. Almohammed Saleh
Program: maintenance.py
Purpose: Back up, restore and reset data.
"""
import datetime
import os
import csv
import json
import time
import shutil
from rich.table import Table
from rich import print
from student import Student
from data_processing import DataProcessing
from dataframe_processing import StudentDF

sounds_path = 'sounds/'
backups_path = 'backups/'

class Maintenance:
    def __init__(self):
        self.choices = {
            "1": self.backup_all_data,
            "2": self.restore_all_data,
            "3": self.reset_students_data,
            "4": self.reset_marks_data,
            "5": self.display_backup_history,
            "6": self.display_restore_history,
            "7": self.send_backup_restore_history,
            "8": self.back,
	}

    def display_menu(self):
        os.system(f"afplay {sounds_path}beep.wav")
        print("""
+++++++++++++++++++++++++++++++++++++++++
+  M A I N T E N A N C E       M E N U  +
+++++++++++++++++++++++++++++++++++++++++

1. Backup all data
2. Restore all data
3. Reset students data
4. Reset marks data
5. Display backup history
6. Display restore history
7. Send backup and restore history to email.
8. <- Back

	""")

    def run(self):
        """Display maintenance menu and respond to choices."""
        loop = True
        while loop:
            #os.system('clear')
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                loop = action()
            else:
                print("{0} is not a valid choice".format(choice))
                break

    def get_last_backup_number(self) -> int:
        """Get last backup number from backups history file."""
        current_date = time.strftime("%Y-%m-%d")
        # set the current_backup_number to zero just in case the backup history file does not exist.
        current_backup_number = 0
        # set the last_line to null just in case the file does not have any lines.
        last_line = ''
        try:
            # Open backups history csv file.
            with open(backups_path+'backups_history.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                # Read last line from file by looping through all lines to the end.
                for line in reader:
                    last_line = line
                if last_line != '':
                    # Store backup number from file into current_backup_number variable.
                    current_backup_number = int(last_line[1])
        except FileNotFoundError:
            print(f"Sorry, file '{backups_path}backups_history.csv' does not exist") 
            choice = input("Create it for you? (Y/N): ")
            if choice.upper() == 'Y':
                with open(backups_path+'backups_history.csv', 'w') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['date', 'backup_number'])
                    writer.writerow([current_date, current_backup_number])
        # Return current_backup_number
        return current_backup_number

    def update_backup_number(self, backup_number):
        current_date = time.strftime("%Y-%m-%d")
        myfile = backups_path + 'backups_history.csv'
        try:
            with open(myfile, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([current_date, backup_number])
                print("Successfully updated backup number")
        except FileNotFoundError:
            print(f"Sorry, file {myfile} does not exist!")
    
    def backup(self, source_file, next_backup_number):
        if source_file == 'students_data.csv':
            destination_file = backups_path + "students_backups/students_data_" + str(next_backup_number) + ".csv"
        elif source_file == 'marks_book.csv':
            destination_file = backups_path + "marks_backups/marks_book_" + str(next_backup_number) + ".csv"

        try:
            shutil.copyfile(source_file, destination_file)
            print(f"File copied successfully from {source_file} to {destination_file}")
        except IOError as e:
            print(f"Error copying file: {e}")

    def backup_all_data(self):
        # Create next_backup_number to be current_backup_number + 1
        next_backup_number = self.get_last_backup_number() + 1
        # Copy 'students_data.csv' to '/backups/students_backups/students_data_' + next_backup_number' + '.csv'
        self.backup('students_data.csv', next_backup_number)
        # Copy 'marks_data.csv' to '/backups/marks_backups/marks_data_' + next_backup_number' + '.csv'
        self.backup('marks_book.csv', next_backup_number)
        self.update_backup_number(next_backup_number)
        input("Press < ENTER > to continue ...")
        return True

    def restore(self, destination_file, last_backup_number):
        """General file restoration function"""
        if destination_file == 'students_data.csv':
            source_file = backups_path + "students_backups/students_data_" + str(last_backup_number) + ".csv"
        elif destination_file == 'marks_book.csv':
            source_file = backups_path + "marks_backups/marks_book_" + str(last_backup_number) + ".csv"

        try:
            shutil.copyfile(source_file, destination_file)
            print(f"File copied successfully from {source_file} to {destination_file}")
        except IOError as e:
            print(f"Error copying file: {e}")



    def restore_all_data(self):
        """Restore all data to main program folder"""
        # Get the last backup number 
        last_backup_number = self.get_last_backup_number()
        # Before proceeding to make the restoration, we need to make a cautionary data backup before proceeding to restore any data.
        # Make backups
        self.backup_all_data()
        # Now let the restoration process begins, WOW!!!
        # Restore 'students_data_{last_backup_number}.csv' to 'students_data.csv'
        self.restore('students_data.csv', last_backup_number)
        # Restore 'marks_data_{last_backup_number}.csv' to 'marks_data.csv'
        self.restore('marks_book.csv', last_backup_number)
        input("Press < ENTER > to continue ...")
        return True
    
    def reset_students_data(self):
        print("RESET STUDENTS DATA")
        input("Press < ENTER > to continue ...")
        return True

    def reset_marks_data(self):
        print("RESET MARKS DATA")
        input("Press < ENTER > to continue ...")
        return True

    def display_backup_history(self):
        """Prints all students in a formatted table."""
        print("DISPLAY BACKUP HISTORY")
        input("Press <ENTER> to continue...")
        return True

    
    def display_restore_history(self):
        print("DISPLAY RESTORE HISTORY")
        input("Press <ENTER> to continue...")
        return True

    def send_backup_restore_history(self):
        print("SEND BACKUP AND RESTORE HISTORY TO EMAIL:")
        input("Press <ENTER> to continue...")
        return True
	

    
    def back(self):
        return False
