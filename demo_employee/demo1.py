class Employee:
    company_name = None # Static Var
    company_location = None

    def __init__(self):
        self.emp_id = None #non Static Variable
        self.emp_name = None
        self.emp_loc = None
        self.emp_salary = None
        self.emp_performance = None

    @staticmethod
    def print_author_name():
        print("Author Name:", "Shefali")

    def display_emp_records(self):
        print(35 * "-")
        print("Emp_Id", self.emp_id)
        print("emp_name", self.emp_name)
        print("Emp Salary", self.emp_salary)
        print("company_name", Employee.company_name)
        print("Company Location", Employee.company_location)

    def calculate_bonus(self):

        if self.emp_performance == "A":
            self.get_updated_salary(10)
        elif self.emp_performance == "B":
            self.emp_salary = self.get_updated_salary(5)
            print(self.emp_name,self.emp_salary)
        elif self.emp_performance == "C":
            self.emp_salary = self.get_updated_salary(2)
        else:
            print("No Bonus")

    def get_updated_salary(self, bonus):
        self.emp_salary = self.emp_salary + (self.emp_salary * bonus) / 100
        return  self.emp_salary
