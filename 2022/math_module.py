#sin Returns the sine of a number, in radians sin(angle)
#cos Returns the cosine of a number, in radians cos(angle)
#tan Returns the tangent of a number, in radians tan(angle)
#ceil Returns the largest integer greater than or equal to a number ceil(3.4323)
#fabs Returns the absolute value (without the sign) of number fabs(–2.65)
#floor Returns the largest integer less than or equal to a number floor(7.234)
#pi The value of pi pi*radius**2

#Forma de importar librerias 
#Libreria de matematicas
from math import *
def area_of_circle(radius):
    return pi*radius**2
area_circulo=area_of_circle(5)
print("area de circulo",str(area_circulo))
print("========")
print("========")
print("========")

#Datetime Libreria

#timedelta Stores a difference between two times
#date Stores a date value
#datetime Stores date and time values
#time Stores a time value
from datetime import datetime
the_time = datetime.now()
print(the_time) #--->  2022-12-28 00:19:59.942982
print(the_time.ctime()) # ---> Wed Dec 28 00:19:59 2022
print("========")
print("========")
print("========")

#Random Module

#seed Seeds the random number generator
#randint Returns a random integer between two values
#choice Selects a random element from a collection
#random Return a float between 0 and 1

import random
for roll in range(7):
 print (random.randint(1,6))

print("***Otro ejemplo de random***")
random.seed(100) # ---> seed es semilla 
for roll in range(10):
 print (random.randint(1, 6))
print ("Re-seeded")
random.seed(100)
for roll in range(10):
 print (random.randint(1, 6))
print("========")
print("========")
print("========")