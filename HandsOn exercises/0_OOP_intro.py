# Define a class
class Student:
    # Class attribute
    university = "Politecnico di Milano"

    # Special method
    def __init__(self, name, age, course):
        self.nome  = name
        self.anni  = age
        self.corso = course

    # Class method
    def describe_me(self):
        print("Name: {}, Age: {}, Course: {}".format(self.nome, self.anni, self.corso))

    # Special method
    def __str__(self) -> str:
        return "{} is {} years old and is enrolled in {}".format(self.nome, self.anni, self.corso)

# Instantiate an object of class Student
stud1 = Student("Andrea", 24, "Neuroengineering")

# Call some methods
stud1.describe_me()
print(stud1) # note that the .__str__ method is called with a print function


# Let's create a child class
class LabStudent(Student):

    def __init__(self, name, age, grade, course="LTEB"):
        super().__init__(name, age, course)
        self.voto = grade

    def __str__(self):
        return "{} is a LTEB student who got {} at the exam".format(self.nome, self.voto) #<-- we can override the parent method and define a new version of it

stud2 = LabStudent("Davide", 27, 30) # note that we don't need to pass the last argument, course, since it is defaulted inside the class definition

stud2.describe_me()
print(stud2)

