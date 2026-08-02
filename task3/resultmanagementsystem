class Student:
    college_name="Aditya Institute of Technology"
    total_students=0
    PASS_MARK=35
    MAX_SUBJECTS=5

    def __init__(self,roll_number,name,branch):
        self.name=name
        self._roll_number=roll_number
        self._branch=branch
        self.__marks={}
        Student.total_students+=1

    @property
    def roll_number(self):
        return self._roll_number

    @property
    def average(self):
        if len(self.__marks)==0:
            return 0.0
        return sum(self.__marks.values())/len(self.__marks)

    @property
    def grade(self):
        avg=self.average
        if avg>=90:
            return "A+"
        elif avg>=75:
            return "A"
        elif avg>=60:
            return "B"
        elif avg>=Student.PASS_MARK:
            return "C"
        return "F"

    def add_marks(self,subject,mark):
        if not isinstance(mark,(int,float)):
            raise TypeError("Mark must be a number")
        if not Student.is_valid_mark(mark):
            raise ValueError(f"Mark must be between 0 and 100, got {mark}")
        if subject not in self.__marks and len(self.__marks)>=Student.MAX_SUBJECTS:
            raise ValueError("Maximum subjects exceeded")
        self.__marks[subject]=mark

    def get_marks(self):
        return dict(self.__marks)

    def has_passed(self):
        if len(self.__marks)==0:
            return False
        return all(i>=Student.PASS_MARK for i in self.__marks.values())

    def change_branch(self,new_branch):
        old=self._branch
        self._branch=new_branch
        return f"{self.name} moved from {old} to {new_branch}"

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    @staticmethod
    def is_valid_mark(mark):
        return isinstance(mark,(int,float)) and 0<=mark<=100

    def __str__(self):
        return f"Student[{self.roll_number}] {self.name} | {self._branch} | Avg:{self.average:.2f} | Grade:{self.grade}"
