class Student():
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

s1 = Student("s1",100)  # print(print(1))
#s1.print_score()
print(s1.print_score())
print(s1)
print(Student)
print(s1.get_grade())
