class Student :
    
    def __init__(self,name,marks1,marks2,marks3) :
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self) :
           avg = (self.marks1+self.marks2+self.marks3)/3
           print(self.name,"your average is",avg)



s1 = Student("Aayushman",9,9,10)
s1.average()

