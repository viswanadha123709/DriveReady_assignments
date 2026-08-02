from resultmanagementsystem import *
def main():
    print("College:",Student.college_name)

    s1=Student(101,"Ravi Kumar","CSE")
    s2=Student(102,"Anita Sharma","ECE")

    print("Total students:",Student.get_total_students())

    s1.add_marks("Maths",92)
    s1.add_marks("Physics",88)
    s1.add_marks("Chemistry",76)

    s2.add_marks("Maths",40)
    s2.add_marks("Physics",35)

    print(s1)
    print(s2)

    print("s1 marks\t:",s1.get_marks())
    print("s1 passed\t:",s1.has_passed())
    print("s2 passed\t:",s2.has_passed())

    print(s1.change_branch("IT"))

    print("is_valid_mark(105):",Student.is_valid_mark(105))

    try:
        s1.add_marks("English",150)
    except ValueError as e:
        print("Blocked (mark 150):",e)

    try:
        s1.average=99
    except AttributeError as e:
        print("Blocked (write average):",e)

    try:
        s1.roll_number=999
    except AttributeError as e:
        print("Blocked (write roll):",e)

    marks=s1.get_marks()
    print("Returned copy:",marks)

    marks["Maths"]=0

    print("Modified copy:",marks)
    print("Original:",s1.get_marks())

    print("protected\t:",s1._branch)
    print("private\t\t:",s1.get_marks())


if __name__=="__main__":
    main()
