class Student:
    name = "KPRIT"
    age = 15

    def read(self):
        print("Reading")
    def write(self):
        print("Writing")

s1 = Student()
s2 = Student()
s3 = Student()

print(s1.name)
print(s1.age)

s1.read()
