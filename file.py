"""f = open("practice.txt","r")
data = f.read()
f.close()  #No effect without it
data1 = data.replace("Python","R")

f = open("practice.txt","w")
f.write(data1)
f.close()  #No effect"""

#Program to check in which line does learning occur first
f = open("practice.txt","r")
l = 1
data = " "
while data != "" :
    data = f.readline()
    i = data.find("learning")
    if i != -1 :
        break
    else :
        l+=1

print(l)        
