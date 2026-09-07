class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name)
        print(self.age)

sam1 = Student("abc", 12)
sam1.info()

sam2 = Student("abcd", 11)
sam2.info()
