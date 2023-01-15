# Lesson on Object Oriented Programming
# Code for Circle Class
# ICS4U0A
# 08 Oct 2020
# Mr Veera

from math import pi 

# Following code creates "Circle" class
class Circle:

    def __init__(self): # Constructor for circle class.
        self.radius=0   # This function is executed when
                        # an object of the class is instantiated(created).
                        # All class variables(class attributes) are defined
                        # and initialized in the constructor function.

    def setRadius(self, radius): # Changes the radius value.
        self.radius=radius

    def getRadius(self): # Returns the radius value.
        return self.radius

    def area(self):     # Computes the area.
        circleArea=pi*(self.radius**2)
        return circleArea

    def __repr__(self): # This function is executed when an object is printed.
        return ('Radius = {:.2f}'.format(self.radius))


# The following code is called client code.
# As it uses the class code created above.

spot=Circle() #Instantiates(creates) an object of Circle class.
              #Name of this object, 'spot'.           

dot=Circle()  #Another Circle object called 'dot' instantiated.

radius_value=spot.getRadius()#the stop in this statement is called the "dot operator"
# dot operator is used to execute a class function.
#In this case the "getRadius()"function.

print('Radius of spot is: {:.2f}'.format(radius_value))


spot.setRadius(2)#dot operator used to execute a different class function.

# The statement below uses dot operators within a print command.
print('New radius is: %.2f and area of spot is %.2f'%(spot.getRadius(),spot.area()))

print('Area of spot is: %.2f'%(spot.area())) # uncomment this line and check the output

# The following 2 statements run the "__repr__()" function in the class definition.
print(spot)
print(dot)
