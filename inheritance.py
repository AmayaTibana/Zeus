import datetime

class Member:
    expiry_days = 365

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

        self.expiry_date = datetime.date.today() + datetime.timedelta(days = self.expiry_days)

    def show_expiry(self):
       return f'{self.first_name} {self.last_name} expires on {self.expiry_date}'
    
    def show_status(self):
       return f'{self.first_name}{self.last_name} is a Member'

class Admin(Member):
  expiry_days = 365 * 100
 
  def __init__(self, first, last, secret):
    super().__init__(first,last)
    self.secret_code = secret

    def show_status(self):
       return f'{self.first_name}{self.last_name} is a Admin'
    
class User(Member):
   pass
    # def show_status(self):
    #    return f'{self.first_name}{self.last_name} is a User' 
   

TestMember = Member('Sophia','Smith')
print(TestMember.show_status())
print(TestMember.expiry_date)
print('--------------')


TestAdmin = Admin('root','admin','ABRACADABRA')
print(TestAdmin.show_status())

print("--------------")

TestUser = User('Artic','Smith')
print(TestUser.show_status())