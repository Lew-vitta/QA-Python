#In a new Python file, create a class of students.

#It should contain the following attributes: name, age, and class with default value "student".

#It should also contain a method which takes in 3 test scores and prints the students average test score.

class Students:
    def __init__(self, name, age, subject="student"):
        self.name = name
        self.age = age
        self.subject = subject
        

    def grade_calculator(self, input):
        total_score = 0
        for i in range(0,3):            
            total_score += input[i] 
        total_score = total_score/3
        return total_score

Jane = Students("Jane", "22", "science")
print(getattr(Jane, "subject"))

student=[]


student_name = (str(input("What is your name? ")))

student.append(float(input("What is your first exam score? (/100) ")))
student.append(float(input("What is your Assesment score? (/100) ")))
student.append(float(input("What is your Exam score? (/100) ")))

print(Students.grade_calculator(student_name, student))





class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

John = Student("John", "21")
Jane = Student("Jane", "22")

print(getattr(John, "age"))