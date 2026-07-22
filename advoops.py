class bank:
    def __init__(self, id, accountBalance,accountName ):
        self.accountId=id
        self.accountBalance=accountBalance
        self.accountName=accountName
    
    def deposit(self, depositAmount):
        if (depositAmount>0):
            self.accountBalance=self.accountBalance+depositAmount
            #self.accountBalance +=depositAmount
            print("amount deposited, thank you")
        else:
            print("please provide a valid deposit amount")

    def withdraw(self, amount):
        if(amount>0 and  self.accountBalance>amount):
            self.accountBalance=self.accountBalance-amount
            print("amount withdrawn, thank you")

    def checkBalance(self):
        print(f"your current balance is {self.accountBalance}")

    
class hdfcBank(bank):
    def fixedDeposit(self, depositAmount):
        print(f"your fixed deposit has been created for the amount{depositAmount}")


class sbiBank(bank):
    def homeLoan(self, loanAmount):
        print(f"loan amount sanctioned {loanAmount}")
        self.accountBalance=self.accountBalance+loanAmount
        self.checkBalance()


newCustomer=hdfcBank("8978",15000,"ram")
newCustomer.deposit(400)
newCustomer.checkBalance()
newCustomer.fixedDeposit(50000)

customer=sbiBank("2345",500000,"teja")
customer.homeLoan(80000)





