"""""'Build a Loan class that:
*Has a common interest rate for all loans.
*Each object stores borrower name and principal.
*Calculates total payable amount.
*Provides a function to update the interest rate.
*Provides a static function to check loan eligibility (e.g., salary > certain threshold).
Demonstrate:
1.Creating multiple loan accounts.
2.Updating interest rates.
3.Checking eligibility and total repayment for borrowers.'"""

class Loan:
    intrest_rate=20
    salary=20000
    def __init__(self,name,salary,principal):
        self.name=name
        self.salary=salary
        self.principal=principal

    def Final_amount(self):
        return self.principal+Loan.intrest_rate

    @classmethod
    def update_intrest(cls,new_rate):
        cls.intrest_rate=new_rate

    @staticmethod
    def loan_elgible(salary):
        if salary>20000:
            return "you are elgible "
        else:
            return "not elgible"

m1=Loan(name="durga",salary=30000,principal=10000)
m2=Loan(name="sai",salary=10000,principal=5000)
print(m1.name,m1.principal,m1.salary)
print(m2.name,m2.principal,m2.salary)
print(m1.loan_elgible(m1.salary))
print(m2.loan_elgible(m2.salary))
Loan.update_intrest(50)
print(m1.name,m1.Final_amount())
print(m2.name,m2.Final_amount())
