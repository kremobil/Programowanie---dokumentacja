class Student:
  def __init__(self, name:str, grades:tuple):
    self.name = name
    self.grades = grades

  def avarge_grade(self):
    return sum(self.grades) / len(self.grades)

student = Student("Rolf", (56,99,43,68,88))
student2 = Student("Hoper", (90,87,43,68,88))

print(student.name, student.avarge_grade())
print(student2.grades, student2.avarge_grade())