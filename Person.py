class Person:
    def __init__(self,firstname,lastname):
       self.firstname= firstname
       self.lastname = lastname
#b. Create a "Student" class which inherits from the "Person" class,
# takes the subject area as an additional argument to the constructor and define a method that prints the full name
# and the subject area of the student.

class Student(Person):
    def __init__(self,firstname,lastname,subject):
        super().__init__(firstname,lastname) #or Person.__init__(self,firstname,lastname)
        self.subject = subject
        self.fullname = firstname + " " + lastname
    def printNameSubject(self):
        print("%s %s" % (self.fullname, self.subject))



me = Student('Benedikt','Daurer','physics')
me.printNameSubject()