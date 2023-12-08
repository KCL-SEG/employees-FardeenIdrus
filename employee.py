"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from contracts import SalaryContract, HourlyContract, ContractCommision, BonusCommision, Payroll

class Employee:
    def __init__(self, name, payroll):
        self.name = name
        self.payroll = payroll

    def get_pay(self):
        return self.payroll.get_amount()

    def __str__(self):
        return self.name+" "+self.payroll.get_text()
    
billie_payroll = Payroll(SalaryContract(4000), None)
billie = Employee('Billie', billie_payroll)

charlie_payroll = Payroll(HourlyContract(25,100), None)
charlie = Employee('Charlie',charlie_payroll)

renee_payroll = Payroll(SalaryContract(3000), ContractCommision(200,4))
renee = Employee('Renee',renee_payroll)

jan_payroll = Payroll(HourlyContract(25,150), ContractCommision(220,3))
jan = Employee('Jan', jan_payroll)

robbie_payroll = Payroll(SalaryContract(2000), BonusCommision(1500))
robbie = Employee('Robbie', robbie_payroll)

ariel_payroll = Payroll(HourlyContract(30,120), BonusCommision(600))
ariel = Employee('Ariel', ariel_payroll)

