"""Q2. Create a class Employee with attributes name and company_name = "TechCorp".
Add a class method change_company(cls, new_name) to update the company name for all employees.
Demonstrate how this change affects all instances."""

class employee:
    company_name = "TECHCORP"
    def __init__(self,name,):
        self.name=name
    @classmethod
    def change_company(cls,new_company):
        cls.company_name = new_company

emp1 = employee("James")
emp2 = employee("durga")
print(emp1.name,emp1.company_name)
print(emp2.name,emp2.company_name)

employee.change_company("cvcorp")
print(emp1.name,emp1.company_name)
