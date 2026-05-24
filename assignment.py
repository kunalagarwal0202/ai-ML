class operations():

    def __init__(self, initialAmount, dataofyear, fdValue, select):
        self.balance=initialAmount
        self.year=dataofyear
        self.fd=fdValue
        self.selection=select
  

    def withdraw(self):
            amount=int(input("what is amount you would like to withderaw"))
            if(self.balance>=amount):
                  self.balance=self.balance-amount
                  print(f"amount withdrawn  current balcne is    {self.balance}")
            else:
                 print("insufeience balance")
            

    def deposit(self, amount):
         self.balance=self.balance+amount
         print("amount deposited")
          
    def fixed_deposit(self):
        pass


operationstest=operations(5000,2025,2000,10)


operationstest.withdraw()
operationstest.withdraw()

