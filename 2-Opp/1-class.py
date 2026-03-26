#Python built-in data types are:
print("bessan".__class__)
print((16).__class__)
print((3.14).__class__)
print([1, 2, 3].__class__)
print(True.__class__)


class Student:

    school = "We school";  #class attribute

    def __init__(self , name , gender , dept):
        self.name = name ;  #instance attribute
        self.gender = gender;
        self.dept = dept;

    def displayInfo(self):
        print(f"Name : {self.name} \nGender : {self.gender} \nDepartment : {self.dept}")

student1 = Student("bessan" , "female" , "Programming");
print(student1.school);
print(student1.name);
print(student1.gender);
print(student1.dept);

student1.displayInfo();

student1.name = "Rowan";
student1.displayInfo();

student2 = student1;
student2.displayInfo();

student3 = Student("Mohamed" , "male" , "Communication")
student3.displayInfo();



