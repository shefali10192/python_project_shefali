from student_package.student_module import Student

stu1 = Student(101, "peter", "perter@gmail.com",80)
stu2 = Student(121, "peter1", "perter2@gmail.com",70)
stu3 = Student(stud_mailid="perter3ss@gmail.com",stud_perce=90)

#
# stu1.stud_mailid = "jack@gmail.com"
# stu2.stud_mailid =  "peter@gmail.com"
# stu3.stud_mailid =  "joh@gmail.com"
#
# print(stu1.stud_mailid)
# print(stu2.stud_mailid)
# print(stu3.stud_mailid)


print(stu1.get_stud_Name())
print(stu1.get_stud_perce   )



