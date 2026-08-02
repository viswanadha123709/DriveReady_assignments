from bankmanagementsystem import bank
def main():
    print("Bank:",bank.Bank_name)

    a1=bank("Ravi Kumar","Savings",5000,1234)
    a2=bank("Anita Sharma","Current",20000,5678)

    print(f"Account[{a1.acountnumber}] {a1.name} | {a1._actype} | Rs.{a1.balance:,.2f}")
    print(f"Account[{a2.acountnumber}] {a2.name} | {a2._actype} | Rs.{a2.balance:,.2f}")

    print("Total accounts:",bank.get_total_accounts())

    print("Deposit 2000 ->",a1.deposit(2000))
    print("Withdraw 1500 ->",a1.withdraw(1500,1234))

    interest=a1.add_annual_interest()
    print("Interest added:",interest)
    print("Balance now:",a1.balance)

    a1.change_pin(1234,4321)
    print("PIN changed successfully")

    print("Withdraw 500 ->",a1.withdraw(500,4321))

    try:
        a1.withdraw(1000,1111)
    except ValueError as e:
        print("Blocked (wrong PIN):",e)

    try:
        a1.withdraw(100000,4321)
    except ValueError as e:
        print("Blocked (below min):",e)

    try:
        a1.deposit(-100)
    except ValueError as e:
        print("Blocked (negative):",e)

    try:
        a1.balance=999999
    except AttributeError as e:
        print("Blocked (write balance):",e)


if __name__=="__main__":
    main()