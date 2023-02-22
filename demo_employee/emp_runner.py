from demo_employee.demo1 import Employee

Employee.company_name = "Einfochips"
Employee.company_location = "Ahmedabad"

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp1.emp_name = "John"
emp2.emp_name = "Peter"
emp3.emp_name = "Kelly"

emp1.emp_salary = 9000
emp2.emp_salary = 8000
emp3.emp_salary = 10000

emp1.emp_performance = "A"
emp2.emp_performance = "B"
emp3.emp_performance = "D"



emp1.calculate_bonus()
emp2.calculate_bonus()
emp3.calculate_bonus()

emp1.display_emp_records()
emp2.display_emp_records()
emp3.display_emp_records()
