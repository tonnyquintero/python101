class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! im a person")
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.studen_id = student_id

    def greet(self):
        super().greet()
        print(f"Hello, my id de estudiante es: {self.studen_id}")

estudiante1 = Student("Ana", 21, "s123")
estudiante1.greet()

#Palabra super heredada por niveles
class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

student = Student("Carlos", 21, "S54321")
student.introduce() 