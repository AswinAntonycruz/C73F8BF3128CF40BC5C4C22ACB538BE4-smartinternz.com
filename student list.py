class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
  return sorted_students




students = [
  student("Gowtham", "A121", 8.8),
  student("cibi", "A122", 6.9),
  student("Sanjay", "A123",5.6),
  student("vishwa", "A124", 9.9),
  student("honest","A125",7.0) 
]

sorted_students = sort_students(students)

for student in sorted_students:
   print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number, student.cgpa))