def Grades(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 80:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks < 60:
        print("Grade F")


if __name__ == "__main__":
    Grades(55)
