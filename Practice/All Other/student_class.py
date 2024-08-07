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

    def high_low(self):
        highest = max(self.grades)  # Find the highest grade
        lowest = min(self.grades)   # Find the lowest grade
        return highest, lowest

my_grades = Student("Juliette", [90, 100, 75, 100])

print(f"Your overall average grade is {my_grades.avg_grade()}.")
my_grades.add_grade()
print(my_grades.grades)

highest, lowest = my_grades.high_low()  # Unpack the returned values
print(f"Your highest grade is {highest}.")
print(f"Your lowset grade is {lowest}.")