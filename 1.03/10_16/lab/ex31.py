import math

# 1a) Create a function which takes a string and concatenates
# "@gmail.com" to this string before returning it
#def emailer(word):
    
    


# 1b) call and print this function on your name
...

# 2a) Fix the function below. It should take in a radius and calculate
# the area of a circle (pi * radius ^ 2)
def area_of_a_circle(radius):
    area = radius ** 2 * math.pi
    return area

radius=float(input("please enter the radius of the given circle:"))

# 2b) use this function to calc the area of a circle with a radius of 5
# (answer should be ~78.5398)

print("The area of the given circle is:", area_of_a_circle(radius))


# 3a) Create a function that converts kilometers to miles
# there are roughly 1.61 km in one mile
def kilometer_1(km):
    conversion_ratio_ = 0.621371
    miles_ = km * conversion_ratio_
    print ("The speed value of car in Miles: ", miles_)
km = float(input('Please enter the speen of car in kilometer as a unit:'))
kilometer_1(km)


# 3b) use this function to convert 10km to miles

#6.21371 miles in 10 km