class Student:
    school_name = None
    school_add = None

    def __init__(self, stud_id= None, stud_name= None, stud_mailid=None, stud_perce=None):
        self.stud_id = stud_id #non Static Variable
        self.stud_name = stud_name
        self.stud_mailid = stud_mailid
        self.stud_perce = stud_perce
        print(self.stud_id)

    def get_stud_Name(self):
        return  self.stud_name

    @property
    def get_stud_perce(self):
        return f"Hi, {self.stud_name}, your percentage is {self.stud_perce}%"

    @staticmethod
    def getSchool():
        return  school_name