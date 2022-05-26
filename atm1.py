class Atm() :
        def __init__(self ,atm_card_number , pin_number , cashWithdrawed , CashDeposited ) :
                    self.atm_card_number = atm_card_number
                    self.pin_number = pin_number
                    self.cashWithdrawed = cashWithdrawed
                    self.CashDeposited = CashDeposited
                  
        def printDetails(self) :
            print(self.atm_card_number)
            print(self.pin_number)
            print(self.cashWithdrawed)
            print(self.CashDeposited)
            
    
def main() :
    atmCardNumber = input("enter Atm Card Number: ")
    pinNumber = input("enter Pin Number: ")
    CashDepositedMoney = input("Enter Deposited Amount: ")
    cashWithdrawedMoney = input("Enter Withdrawed Money: ")
   

    details=Atm("Atm no." + atmCardNumber, "Pin " + pinNumber , "+RS." + CashDepositedMoney , "-Rs." + cashWithdrawedMoney )
    
   
    details.printDetails()
           
    
main()

