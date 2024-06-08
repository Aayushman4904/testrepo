"""
class Student :
    college = "College"       # Class attributes
    name = ""

    def __init__(self, name) :
        self.name = name               # self.name is a object attribute
        print("Adding new student")


    def w(self) :
        print("Welcome Student")    


s1 = Student("Aayushman")    # () calls constructor  
print(s1.name) 
s1.w()

s2 =Student("Parameksu")
print(s2.name)

print(s1.college)
print(Student.college)
"""


class Account :

    def __init__(self,bal,accno) :
        self.bal = bal
        self.accno = accno

    def debit(self,deb) :
        self.bal = self.bal - deb
        print(deb,"debited from your account. Balance is",self.bal)

    def credit(self,cred) :
        self.bal = self.bal + cred
        print(cred,"credited to your account. Balance is",self.bal)

c1 = Account(12000,1100972873)
c1.credit(444)  
c1.debit(444)          
