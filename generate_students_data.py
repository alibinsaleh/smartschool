import random
import string
from datetime import datetime, timedelta
import csv

def random_string(length):
  """Generates a random string of the specified length."""
  return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def random_name(first_names, last_names):
  """Generates a random name using provided lists."""
  return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_phone_number():
  """Generates a random phone number in +1 format."""
  area_code = f"{random.randint(210, 916)}"
  prefix = f"{random.randint(100, 999)}"
  line_number = f"{random.randint(1000, 9999)}"
  return f"+1 {area_code}-{prefix}-{line_number}"

def random_address(street_names, suffixes):
  """Generates a random address with street name and suffix."""
  house_number = random.randint(100, 999)
  street_name = random.choice(street_names)
  suffix = random.choice(suffixes)
  return f"{house_number} {street_name} {suffix}"

def random_date(days_back=30):
  """Generates a random date within the past days_back days."""
  start_date = datetime.today() - timedelta(days=days_back)
  end_date = datetime.today()
  random_delta = timedelta(days=random.randint(0, days_back))
  return (start_date + random_delta).strftime("%Y-%m-%d")

def generate_student_data():
  """Generates a single row of random student data."""
  first_names = ["Emma", "Olivia", "Ava", "Sophia", "Isabella", "Charlotte", "Mia", "Amelia", "Evelyn", "Abigail"]
  last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Hernandez", "Lopez"]
  street_names = ["Maple", "Oak", "Pine", "Elm", "Birch", "Willow", "Poplar", "Cedar", "Hickory", "Locust"]
  suffixes = ["St", "Ave", "Rd", "Ln", "Way", "Blvd", "Pl", "Cir", "Trl", "Pkwy"]

  return (
      str(random.randint(10000, 99999)),  # Random ID (5 digits)
      random_name(first_names, last_names),
      random.choice(["101", "102", "201", "202", "301", "302"]),  # Random classroom
      random_address(street_names, suffixes),
      random_phone_number(),
      random_date(),
  )

# Generate 100 rows of random student data
data = [generate_student_data() for _ in range(100)]

# Write data to a CSV file (change 'student_data.csv' to your desired filename)
with open('students_data.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['id', 'name', 'classroom', 'address', 'mobile', 'date_created'])  # Header row
  writer.writerows(data)

print("100 rows of random student data written to student_data.csv")
