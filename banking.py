#Antoine Bonnet

import datetime

#User enters their different banks
print("Welcome to your online banking system!")

#Store accounts in dictionary, with unique key = account ID, value = BankAccount
myAccounts = {}

# Create a log file "MyAccounts.txt, where each entry has date, time and description of every transaction on all accounts
# Each entry (line) in the log file is of the format: Date&time   Account ID  Transaction Type  Amount   Balance
fp = open("MyAccounts.txt", "r+") # overwrite
fp.truncate(0)
fp.close()

# definition of Bank 
class BankAccount:
   def __init__(self, accID, bankname, accType, balance, lastAccess):
        self.accID = accID
        self.bankname = bankname
        self.accType = accType
        self.balance = balance 
        self.lastAccess = lastAccess 

# ADD A NEW BANK ACCOUNT
def createAccount():
   accID = input("Enter your bank ID: ")
   if (accID in myAccounts):
      print("There is already another account with the same ID. Please try again")
      return
   bankname = input("Enter the bank name: ")
   accType = input("Enter the account type: ")
   balance = round(float(input("Enter the account balance: ")),2)
   time = datetime.datetime.now().replace(microsecond=0)
   newAcc = BankAccount(accID, bankname, accType, balance, time)
   myAccounts[accID] = newAcc
   
   entry = [str(time), accID, "Account creation", str(balance), str(balance)]
   fp = open("MyAccounts.txt", "a")
   fp.write("\t".join(entry))
   fp.close()

   return newAcc

# PRINT INFO OF AN ACCOUNT
def printInfo(self):
   print("Account ID :",self.accID)
   print("Bank name :", self.bankname)
   print("Account type :", self.accType)
   print("Balance :", self.balance)
   print("LastAccess :", self.lastAccess) 
   
# 1 - WITHDRAW AMOUNT FROM ACCT
def withdrawal(self):
   amount = round(float(input("Enter the amount of money you would like to withdrawl from this account: ")), 2)
   if (amount > self.balance):
      print("The amount entered was greater than the account balance. Action impossible")
      return 

   self.balance -= amount

   #print("You now have",self.balance,"$ remaining in this account.")
   
   time = datetime.datetime.now().replace(microsecond=0)
   
   entry = [str(time), self.accID, "Withdrawal", str(amount), str(self.balance)]
   fp = open("MyAccounts.txt", "a")
   fp.write("\t".join(entry))
   fp.close()
   
   self.lastAccess = time

# 2 - DEPOSIT AMOUNT TO ACCT
def deposit(self):
   amount = round(float(input("Enter the amount of money you are depositing to this account: ")),2)
   self.balance += amount

   #print("You now have" ,self.balance, "$ in this account.")
    
   time = datetime.datetime.now().replace(microsecond=0)
    
   entry = [str(time), self.accID, "Deposit", str(amount), str(self.balance)]
   fp = open("MyAccounts.txt", "a")
   fp.write("\t".join(entry))
   fp.close()
   
   self.lastAccess = time

# 3 - Transfer an amount between accounts.
def transfer(self, other):
   amount = round(float(input("Enter the amount you would like to transfer : ")),2)
   if (amount > self.balance):
      print("The amount entered was greater than the first account's balance. Action impossible")
      return
   
   self.balance -= amount
   other.balance += amount

   #print ("You now have", self.balance, "$ and", other.balance, "$ remaining in each account.")
   
   time = datetime.datetime.now().replace(microsecond=0)
   entry1 = [str(time), self.accID, "Transfer withdrawal", str(amount), str(self.balance)]
   entry2 = [str(time), other.accID, "Transfer deposit", str(amount), str(other.balance)]             

   fp = open("MyAccounts.txt", "a")
   fp.write("\t".join(entry1))
   fp.write("\t".join(entry2))
   fp.close()
   
   self.lastAccess = time
   other.lastAccess = time
                  
                 
# 4 - Compare the balance of 2 accounts

def compare(self, other):
   if self.balance > other.balance:
      print("The first account has a greater balance of", self.balance, "$, while the second account has a lower balance of", other.balance,"$.")
   else:
      print("The second account has a greater balance of", other.balance, "$, while the first account has a lower balance of", self.balance,"$.")
      
# 5 - DELETE A BANK ACCOUNT
def delAccount(self):
   ans=input("You are about to delete the account. Are you sure you would like to proceed? Type yes or no")
   if ans == 'yes':
      del yourAccounts[self.id]
      print('deleted.')
   elif ans == 'no':
      print("Account not deleted.")

# 6 - Print the balance of a given account
def balance(self):
   print("You currently have", self.balance, "$ in this account.")
   
# 7 - Print the log file.
def printLog():
   fp = open("MyAccounts.txt", "r")
   content = fp.read()
   print(content)
     
    
    
        
            
        
        
