class bank():
    Bank_name="State Bank of India"
    count=0
    interest=4
    mini=500
    nextnumber=1001
    def __init__(self,name,actype,initialdeposit,pin):
        if initialdeposit < bank.mini:
            raise ValueError(f"Minimum initial deposit should be ₹{bank.mini}")
        self.name=name
        self._acnumber=bank.nextnumber
        self._actype=actype
        self.__balance=initialdeposit
        self.__pin=pin
        bank.nextnumber+=1
        bank.count+=1


    @property
    def acountnumber(self):
        return self._acnumber

    
    @property
    def balance(self):
        return self.__balance

    
    def deposit(self,amount):
        if not self.is_valid_amount(amount):
            raise ValueError("invalid amount")
        self.__balance+=amount
        return self.__balance


    def withdraw(self,amount,pin):
        if not self.is_valid_amount(amount):
            raise ValueError("enter valid amount")
        if not self.__verify_pin(pin):
            raise ValueError("incorrect pin")
        if self.__balance-500<amount:
            raise ValueError("insufficient funds to maintain minimum balance")

        self.__balance-=amount
        return self.__balance


    def __verify_pin(self,pin):
        return pin==self.__pin


    def change_pin(self,old_pin,new_pin):
        if not self.__verify_pin(old_pin):
            raise ValueError("incorrect pin ")
        if len(str(new_pin))!=4 or isinstance(new_pin,str):
            raise ValueError("enter 4 digits number")
        self.__pin=new_pin


    def add_annual_interest(self):
        temp=self.__balance*bank.interest/100
        self.__balance+=temp
        return temp


    @classmethod
    def get_total_accounts(cls):
        return cls.count


    @staticmethod
    def is_valid_amount(amount):
        if amount>0:
            return True
        return False