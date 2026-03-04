class Student:
    def __init__(self,institute_name,c_name,id,s_name,cgpa):
        self.institute_name=institute_name
        self.c_name=c_name
        self.id=id
        self.s_name=s_name
        self.cgpa=cgpa

    def display_info(self):
        print("-------------------------------")
        print("Institute Name :",self.institute_name)
        print("Class Name : ",self.c_name)
        print("Student ID : ",self.id)
        print("Student Name : ",self.s_name)
        print("CGPA : ",self.cgpa)
        print("-------------------------------")
        
    
s1=Student(
    input("Institute Name :"),
    input("Class Name :"),
    input("Enter Your id :"),
    input("Enter Your Name :"),
    input("Enter Your grade :")
)

s2=Student(
    input("Institute Name :"),
    input("Class Name :"),
    input("Enter Your id :"),
    input("Enter Your Name :"),
    input("Enter Your grade :")
)

s3=Student(
    input("Institute Name :"),
    input("Class Name :"),
    input("Enter Your id :"),
    input("Enter Your Name :"),
    input("Enter Your grade :")
)

s1.display_info()
s2.display_info()
s3.display_info()
