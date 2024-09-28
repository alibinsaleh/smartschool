from teacher import Teacher, Subject
from rich.table import Table
from rich import print
import csv

def _make_list_enum(mylist: list[str]):
        enum_list = []
        for item in mylist:
            subject_str = item.strip()
            if subject_str in Subject.__members__:
                enum_list.append(Subject[subject_str])
            
        return enum_list


class TeacherManagement:
    def __init__(self):
        self.teachers = []
        self.load_teachers_data_from_file()

    def load_teachers_data_from_file(self):
        try:
            with open('teachers_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
                data = csv.reader(csvfile, quotechar='"', delimiter=',')
                header = next(data)
                
                for row in data:
                    subjects_list = _make_list_enum(row[5].split(','))
                    teacher = Teacher(
                        id=row[0],
                        name=row[1],
                        dob=row[2],
                        email=row[3],
                        address=row[4],
                        subjects=subjects_list,
                        created_at=row[6],
                    )
                    self.teachers.append(teacher)
                    
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_teachers(self) -> None:
        # Print classroom  students list using rich module's print and table classes
        table = Table(title="Teachers List", show_header=True)
        table.add_column("ID", style="green", justify="left")
        table.add_column("Name", style="magenta", justify="left")
        table.add_column("DOB", justify="right")
        table.add_column("Email", justify="right")
        table.add_column("Address", justify="right")
        table.add_column("Subject", justify="right")
        table.add_column("Created At", justify="right")
        for teacher in self.teachers:
            # make list of enum items as a list of strings. 
            subjects = [str(sub.name) for sub in teacher.subjects]
            # convert list to string separated with commas.
            subjects = ', '.join(subjects) 
            table.add_row(teacher.id, 
                          teacher.name, 
                          str(teacher.dob.strftime('%Y-%m-%d')), 
                          teacher.email, 
                          teacher.address,
                          subjects,
                          str(teacher.created_at.strftime('%Y-%m-%d')))
        print(table)

     


if __name__ == '__main__':
    t = TeacherManagement()
    t.display_teachers()