"""
Create a Python Class called Circle with Constructor which will take a list as an 
argument for the task. The List is [10,501,22,37,100,999,87,351]
"""

# Defining a class named circle
class Circle:
    # Defining a constructor method __init__ which initializes the object with a list
    def __init__(self,list1):
        # Storing the provided list as an instance variable named list1
        self.list1=list1
    
    
    # Defining a method named display within the Circle class
    def display(self):
         # Printing a message along with the content of the list stored in the object
        print(f"The list is: {self.list1}")

# Creating  an instance of the Circle class and provide a list as input
obj=Circle([10,501,22,37,100,999,87,351])
# Calling the display method of the Circle object
# This method prints the content of the list stored in the object
obj.display()







# Defining a class named Circle
class Circle:
    # Define a constructor method __init__ which initializes the object
    # This constructor does not take any parameters other than self
    def __init__(self):
        # Initialising an instance variable named list1 with a list containing some values
        self.list1=[10,501,22,37,100,999,87,351]
    
    # Defining a method named display_list within the Circle class
    def display_list(self):
        # Printing the content of the instance variable list1
        print(self.list1)


# Create an instance of the Circle class
obj=Circle()
# Calling the display_list method of the Circle object
# This method prints the content of the list stored in the instance variable list1
obj.display_list()

