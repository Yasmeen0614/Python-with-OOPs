class Sample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def read(self):
        print(self.name)
        print(self.age)

s1 = Sample("KPRIT", 20)
s1.read()

s2 = Sample("abc", 21)
s2.read()
