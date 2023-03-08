#fugu es un pez que lo sirven como gourmet

fugu='tasty'
is_fugu_tasty = (fugu == "tasty")
print(is_fugu_tasty)
print("==========")
#Equal operator
if fugu == "tasty":
 print("Eat the fugu!")
 print("==========")
 
#AND operator 
price = 50.0
if fugu == "tasty" and price < 100.0:
 print("Eat eat eat!")
 print("==========")

#Logic Result
#False and False False
#True and False False
#False and True False
#True and True True

#OR Operator
if fugu == "tasty" or price < 20.0:
 print ("some some some!")
 print("==========")
#False or False False
#True or False True
#False or True True
#True or True True
 
#Not Operator
if not (fugu == "tasty" and price < 100.0):
 print("Don't eat the fugu!")
print("==========")
#not True False
#not False True

#Else statement
if fugu == "tasty":
 print ("enter if")
else:
 print( "Don't enter the if, enter in else")

#Elif Statement
price=0 #Cheap
#price=50 #reasonably
#price=150 #Expensive
print("==========")
if price < 20:
 print ("Cheap fugu!")
elif price < 100:
 print ("Reasonably priced fugu.")
else:
 print ("Expensive fugu!")


# abs Finds the absolute value of a number abs(-3)
# help Displays usage information for any Python object help([])
# len Returns the length of a string or collection len("hello")
# max Returns the largest value max(3, 5)
# min Returns the smallest value min(3, 4)
# range Returns a list containing a range of numbers range(1,6)
# round Rounds a float to a given precision round(10.2756, 2)

# visit http://doc.python.org

#Defining Functions

def fugu_tip(price, num_plates, tip):
 total = price * num_plates
 tip = total * (tip / 100.)
 return tip
print("==========")
print ("propina 1 -> ",str(fugu_tip(100.0, 2, 15.0)))
print ("propina 2 ->",str(fugu_tip(50.0, 1, 5.0)))
print("==========")
#Default Values in fuction 
def fugu_tip(price, num_plates=2, tip=15.):
 total = price * num_plates
 tip = total * (tip / 100.)
 return tip
print ("propina 3 -> ",str(fugu_tip(100.0)))
print ("propina 4 -> ",str(fugu_tip(50.0, 1, 5.0)))
print ("propina 5 -> ",str(fugu_tip(50.0, tip=10.0)))
print("==========")

 
 
 
 
 
 
 