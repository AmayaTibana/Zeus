
import datetime 
class User:
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword
 
    self.activeUser = True
    self.numOfLogins = 0
    self.dateJoined = datetime.date.today()
  
  #display number of logins
  def show_num_logins(self):
    return self.username + " logged in " + str(self.numOfLogins) + " times."
 
  #increase number of logins
  def logged_in(self):
    self.numOfLogins = self.numOfLogins + 1
 
  #logging into the user account
  def login(self, uname, pword):
    if (self.username == uname and self.password == pword):
      print("Login successful")
      self.logged_in()
    else:
      print("Incorrect username and password combination.")

      
account = User('sophia','mypass')
 
account.login('sophia','mypass')
account.login('sophia','wrongpassword')
account.login('sophia','mypass')
account.login('sophia','mypass')
account.login('sophia','wrongpassword')
 
print(account.show_num_logins())