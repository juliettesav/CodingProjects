class Student: 
    def __init__(self, name, grades):
        self.name = name 
        self.grades = grades 

    def avg_grade(self):
        avg = sum(self.grades) / len(self.grades)
        return avg

    def add_grade(self):
        new_grade = int(input("Add New Grade: "))
        self.grades.append(new_grade)
        return new_grade

'''
    def high(self):
        pass 

    def low(self):
        pass
'''

my_grades = Student("Juliette", [90, 100, 75, 100])

print(my_grades.avg_grade())
print(my_grades.add_grade())
print(my_grades.grades)