
"""
From the given list creata two class Methods Area and Perimeter which will be going to 
calculate the Area and Perimeter
"""
# Defining a class named Circle
class Circle:

    # Constructor to initialize the Circle object with a list of radii
    def __init__(self, radius_list):
        
        # Storing the list of radii as an instance variable
        self.radius_list = radius_list
        
        # Defining  a private variable for pi
        self.__pi = 3.141  


    # Method to calculate the area of circles with radii from the radius_list
    def calculate_area(self):
        
        # Using list comprehension to calculate the area of each circle
        areas = [self.__pi * (r ** 2) for r in self.radius_list]
        # Returning  a list of areas
        return areas
    

    # Method to calculate the perimeter of circles with radii from the radius_list
    def calculate_perimeter(self):
        
        # Using list comprehension to calculate the perimeter of each circle
        perimeters = [2 * self.__pi * r for r in self.radius_list]
        
        # Returning a list of perimeters
        return perimeters

# Testing the class
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)

# Calculating areas and perimeters for each circle in the list
areas = circle.calculate_area()
perimeters = circle.calculate_perimeter()

# Printing  the details of each circle along with its calculated area and perimeter
for i, radius in enumerate(radius_list):
    print(f"Circle {i+1} - Radius: {radius}, Area: {areas[i]}, Perimeter: {perimeters[i]}")





"""
From the given list creata two class Methods Area and Perimeter which will be going to 
calculate the Area and Perimeter
"""
# Defining a class named Circle
class Circle:
    # Constructor to initialize the Circle object with a list of radii and the value of pi
    def __init__(self,radius_list,pi):
        # Storig the list of radii as an instance variable
        self.radius_list=radius_list
        # Storing the value of pi as an instance variable
        self.pi=pi

    # Method to calculate and print the area of circles for each radius in the radius_list
    def area(self):
        # Iterating over each radius in the radius_list
        for i in self.radius_list:
           # Printing the calculated area for the current radius
            print(f"The area of circle for radius:{i} and pi:{self.pi} = {self.pi*(i*i)}")
    
    # Method to calculate and print the perimeter of circles for each radius in the radius_list
    def perimeter(self):
         # Iterating over each radius in the radius_list
        for i in self.radius_list:
            # Printing the calculated perimeter for the current radius
            print(f"The perimeter of circle for radius:{i} and pi:{self.pi} ={2*self.pi*i}")

# Creating an instance of the Circle class with a list of radii and the value of pi
obj=Circle([10,501,22,37,100,999,87,351],3.141)
# Printing the area of circles for each radius in the list
print("Area:")
obj.area()
# Print the perimeter of circles for each radius in the list
print("Perimeter:")
obj.perimeter()



"""
From the given list creata two class Methods Area and Perimeter which will be going to 
calculate the Area and Perimeter
"""

# Defining a class named Circle
class Circle:
    # Constructor to initialize the Circle object with a list of radii and the value of pi
    def __init__(self,radius_list,pi):
        # Storing the list of radii as an instance variable
        self.radius_list=radius_list
        # Storing the value of pi as a private instance variable (private with double underscore)
        self.__pi=pi

    # Method to calculate and print the area of circles for each radius in the radius_list
    def area(self):
        # Iterating over each radius in the radius_list
        for i in self.radius_list:
            # Printing the calculated area for the current radius
            print(f"The area of circle for radius:{i} and pi:{self.__pi} = {self.__pi*(i*i)}")
    
    # Method to calculate and print the perimeter of circles for each radius in the radius_list
    def perimeter(self):
         # Iterating over each radius in the radius_list
        for i in self.radius_list:
            # Printing the calculated perimeter for the current radius
            print(f"The perimeter of circle for radius:{i} and pi:{self.__pi} ={2*self.__pi*i}")

# Creating an instance of the Circle class with a list of radii and the value of pi
obj=Circle([10,501,22,37,100,999,87,351],3.141)
# Printing the area of circles for each radius in the list
print("Area:")
obj.area()

# Printing the perimeter of circles for each radius in the list
print("Perimeter:")
obj.perimeter()
