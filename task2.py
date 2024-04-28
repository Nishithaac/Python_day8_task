"""
2) Create proper member variables inside the task if required and use them when 
necessary. For example for this task create a class private variable named pi=3.141
"""

# Defining a class named Circle
class Circle:
    # Defining a private class variable named __pi with a value of 3.141
    __pi=3.141

    # Defining a method named display within the Circle class
    def display(self):
        
        # Returning the value of the private class variable __pi
        return(self.__pi)

# Creating an instance of the Circle class
obj=Circle()


# Call the display method of the Circle class using the instance obj
# The display method returns the value of the private class variable __pi
print(obj.display())

    
