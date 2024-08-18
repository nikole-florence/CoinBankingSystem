#Nikole Florence
#Bank System using coin denominations

#create bank system class with a dictionary to hold user accounts
class BankSystem:
    def __init__(self):
        self.users = {}
        
#functions to create an account and authenticate the user
    def createAccount(self, username, password):
        if username in self.users:
            print("Username not available. Please choose another one.")
            return False
        
        self.users[username] = {'password': password, 'account': {1:0, 5:0, 10:0, 25:0}}
        print(f"Account created for {username}.")
        return True
    
    def authenticateUser(self, username, password):
        user = self.users.get(username)
        if user and user['password'] == password:
            print("Successful.")
            return True
        
        print("Invalid username or password")
        return False
    
#functions to deposit and withdraw money
    def depositMoney(self, username, coins):
        if username not in self.users:
            print("User not found. Please try again.")
            return
        
        for denomination, count in coins.items():
            if denomination in self.users[username]['account']:
                self.users[username]['account'][denomination] += count
            else:
                print(f"Denomination {denomination} not recognized.")
                
    def withdrawMoney(self, username, amount):
        if username not in self.users:
            print("User not found. Please try again.")
            return None
  
#if the amount requested is higher than the amount available, message is returned
        account = self.users[username]['account']
        if self.totalBalance(username) < amount:
            print("Insufficent funds.")
            return None
        
        withdrawl = {1: 0, 5: 0, 10: 0, 25: 0}
        for denomination in sorted(account.keys(), reverse=True):
            while amount >= denomination and account[denomination] > 0:
                amount -= denomination
                account[denomination] -= 1
                withdrawl[denomination] += 1
      
#if denomination amount requested is unavailable, message is returned
        if amount > 0:
            print("Cannot provide exact amount.")
            for denomination, count in withdrawl.items():
                account[denomination] += count
            return None
        return withdrawl
    
#functions to show total balance of the user and display that balance
    def totalBalance(self, username):
        if username not in self.users:
            print("User not found. Please try again.")
            return 0
        
        account = self.users[username]['account']
        totalAmount = sum(denomination * count for denomination, count in account.items())
        return totalAmount
    
    def displayBalance(self, username):
        if username not in self.users:
            print("User not found. Please try again.")
            return
        
        account = self.users[username]['account']
        print(f"Account balance for {username}:")
        for denomination, count in account.items():
            print(f"{denomination} cent: {count} coins")
        print(f"Total balance: {self.totalBalance(username)} cents")
   
#bank system is called into action
bank = BankSystem()
    
bank.createAccount("user123", "password123")
    
if bank.authenticateUser("user123", "password123"):
    bank.depositMoney("user123", {1: 15, 5: 20, 10: 12, 25: 18})
    bank.displayBalance("user123")
        
if bank.authenticateUser("user123", "password123"):
    withdrawnCoins = bank.withdrawMoney("user123", 50)
    if withdrawnCoins:
        print("Withdrawn coins:")
        for denomination, count in withdrawnCoins.items():
            print(f"{denomination} cent: {count} coins")
            bank.displayBalance("user123")
        