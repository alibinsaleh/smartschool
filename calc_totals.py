import pandas as pd

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('marks_book.csv')

# Step 2: Group by 'student_id' and 'assessment_type' and sum the 'mark'
total_marks = df.groupby(['id', 'assessment'])['mark'].sum().reset_index()
#student_total = df[df['id'] == 10001]['mark'].sum()
student_total = total_marks[total_marks['id'] == 10001]
print(student_total)
# Step 3: Display the result
print(total_marks)
marks_dic = {
    'THEORETICAL PARTICIPATION': 12        
}
# Optionally, save the result to a new CSV file
total_marks.to_csv('output_marks_book.csv', index=False)

