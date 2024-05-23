#first program
marks = input("marks: ")
  
if (marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D") 
    
#second program
    A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 and G == "F"):
    print("fee is 200")
elif(A == 5 and G == "F"):
    print("fee is 300")
else:
    print("no fee")

    #single line if / ternary operator
#<var>=<val1> if <condition> else <val2>

food = input("food : ")
eat="yes" if food == "cake" else "no"
print(eat)



#<stt1> if <condition> else <stt2>

food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet") 

#calculate simple interest 
p = float(input("p : "))
r = float(input("r : "))
t = float(input("t : "))
si = (p*r*t)/100
print(si)

#WAP TO INPUT SIDE OF A SQUARE & PRINT ITS AREA
side = int(input("num : "))
area = side*side
print(area)

#WAP TO INPUT 2 FLOATING POINT NUMBERS & PRINT THEIR AVERAGE
a = float(input("num1 : "))
b = float(input("num2 : "))
average = a+b/2
print(average)

#WAP TO INPUT 2 int NUMBERS a and b
#PRINT TRUE IF A GREATER THAN OR EQUAL TO B . IF NOT PRINT FALSE
a = int(input("num1 : "))
b = int(input("num2 : "))
if(a>=b):
  print(True)
else:
  print(False)

'''STRING FUNCTIONS-

str = "I am a coder"
str.endswith("er)#returns true if string ends with substr
str.capitalize( )#capitalizes 1st char
str.replace(old,new)#replaces all occurrence of old and new
str.find(word)#returns 1st index of 1st occurrer
str.count("am")#count the occurences of substr'''

str = "my name is anshi"
print(str.endswith("shi"))
print(str.capitalize())
print(str.replace("anshi" , "raunak"))
print(str.find("n"))
print(str.count("anshi"))

#WAP to check if a number entered by the user is odd or even

a = int(input("number : "))
if(a%2 == 0):
    print("even")
else:
    print("odd")
    #or

num = int(input("num : "))

rem = num % 2

if(rem == 0):
   print("even")
else:
   print("odd")

#WAP to find the greatest of 3 numbers entered by the user

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if(a > b and a > c):
    print("a is greater")
elif(b > c):
    print("b is greater")
else:
    print("c is greater")

#WAP to check if a number is a multiple  of 7 or not

a = int(input("number : "))
if(a % 7 == 0):
    print("it is multiple of 7")
else:
    print("it is not multiple of 7")

    #if you want to print any nmber with the help of its index number 
marks = [34.3 , 56 , 88.8 , 53]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

'''#list methods
list = [2,1,3]
list.append(4) 'adds one element at the one '
output=[2,1,3,4]
list.sort() 'sorts in ascending order'
output=[1,2,3]
list.sort(reverse=true)'sorts in descending order'
output=[3,2,1]
list.reverse()'reverses list'
output=[3,1,2]
list.insert(idx ,el) 'insert element at index'
output=it inserts new elements at the place of any index and replace it with new one
like if we have to replace 1 with 5
so we will write
list.insert(1 , 5)
output=[2,5,1,3]
list.remove(1) 'removes first occurence of element'
output=[2,3,1]
list.pop(idx)
list.pop(2)'removes element at idx'
output=(2,3)'''

