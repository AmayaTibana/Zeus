# class User:
#   def __init__(self, uname, pword):
#     self.username = uname
#     self.password = pword

# account = User('sophia','mypass')
# print(account.username)
# print(account.password)
# account.username = 'python'
# print(account.username)
# print(account.password)

import datetime 
 
class User:
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword
 
    self.activeUser = True #new variable with True as default value
    self.numOfLogins = 0 #new variable with 0 as default value 
    self.dateJoined = datetime.date.today() #new variable using the datetime module
    self.whatever = "Whatever"
account = User('sophia','mypass')
print(account.username)
print(account.password)
print(account.activeUser)
print(account.numOfLogins)
print(account.dateJoined)
print(account.whatever)