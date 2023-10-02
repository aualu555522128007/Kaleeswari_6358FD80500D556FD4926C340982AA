# Define a function called sort_students
def sort_students(students):
  # Use the built-in sorted function to sort the list of students
  # Use a lambda function to specify the sorting key as the cgpa attribute
  # Use reverse=True to sort in descending order
  sorted_students = sorted(students, key=lambda student: student.cgpa, reverse=True)
  # Return the sorted list of students
  return sorted_students

# Define a class called Student to represent a student object
class Student:
  # Define the constructor method with name, roll_number, and cgpa as parameters
  def _init_(self, name, roll_number, cgpa):
    # Assign the parameters to the instance attributes
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

  # Define a string representation method for printing a student object
  def _str_(self):
    # Return a formatted string with the name, roll_number, and cgpa of the student
    return f"{self.name} ({self.roll_number}) - {self.cgpa}"

# Example list of student objects
students = [
  Student("Alice", "A001", 3.8),
  Student("Bob", "B002", 3.6),
  Student("Charlie", "C003", 3.9),
  Student("David", "D004", 3.7),
  Student("Eve", "E005", 3.5)
]

# Call the function and print the result
result = sort_students(students)
for student in result:
  print(student)