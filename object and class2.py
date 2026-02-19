class student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll No", self.roll_no)
        print("Name", self.name)
        print("Marks", self.marks)


s1 = student(1, "Rahu", 89)
s1.display()
