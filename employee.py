"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class salaryContract:
    def __init__(self,salary):
        self.salary= salary
        
    def getAmount(self):
        return self.salary
    
    def printText(self):
        return f'monthly salary of {self.salary}'
    
class hourlyContract:
    def __init__(self,rate,hours):
        self.rate = rate
        self.hours = hours
        
    def getAmount(self):
        return self.rate * self.hours
    
    def printText(self):
        return f'contract work of {self.hours} paid at {self.rate} per hour'
    
class contractCommision:
    def __init__(self, commissionAmount, numOfCommission):
        self.commision = commissionAmount
        self.numOfCommision = numOfCommission
        
    def getAmount(self):
        return self.commision * self.numOfCommision
    
    def printText(self):
        return f'total commision of {self.getAmount()}'
    
class Bonus:
    def __init__(self,bonusAmount):
        self.bonusAmount = bonusAmount
        
    def getAmount(self):
        return self.bonusAmount
    
    def printText(self):
        return f'recieved a bonus of {self.getAmount()}'
    
class EmployeeSalaries:
    def __init__(self,contract,commission):
        self.contract = contract
        self.commission = commission
        
    def getTotalPay(self):
        totalPay = 0
        if self.contact:
            totalPay += self.contact.getTotalPay()
        
        if self.commision:
            totalPay += self.contract.getTotalPay()
            
    def printCommisionText(self):
        if self.commision is None:
            return "no commission"
        return self.commission.printCommisionText()
    
    def printFullText(self):
        return f'{self.contract.printText()}{(" and "+self.printCommissionText()) if self.commision is not None else ""}. Their total pay is {self.getAmount()}.'
            
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')

