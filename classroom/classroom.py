class Person():
    def __init__(self, firstname, lastname):
        self.full_name = firstname + " " + lastname
    def getName(self):
        return self.full_name
        
class Student(Person):
    def __init__(self, firstname, lastname, subject_area):
        super(Student, self).__init__(firstname, lastname)
        self.subject_area = subject_area
        self.NameSubject = self.full_name + ", " + self.subject_area
    def printNameSubject(self):
        print(self.NameSubject)
    