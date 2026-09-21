class Student:
    name = "Yasmeen"
    roll_no = 101
    marks1 = 75
    marks2 = 80
    marks3 = 82

    def total_marks(self):
        total = self.marks1 + self.marks2 + self.marks3
        return total

    def average(self):
        avg = self.total_marks() / 3
        return avg

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Total Marks:", self.total_marks())
        print("Average:", self.average())
        print("Grade:", self.grade())
        
S = Student()
S.display()