##Harsh Tamakuwala
##662282
##Mr.Veera
##Classes and Objects Test
##Question1

##Sphere Class
class sphere:
    def __init__(self): # Constructor for sphere class.
        self.radius=0   
        self.radius=0 
        self.volume=0 # All class variables(class attributes) are defined
        self.surface_area=0 # and initialized in the constructor function.

    def setradius(self, radius): # Changes the radius value.
        self.radius=radius

    def getradius(self):
        return ('Radius = {:.2f}'.format(self.radius)) ##To bring the Radius as an output

    def set_volume(self):
        self.volume=(4*3.14*((self.radius)**3))/3 ##goes through volume formula

    def get_volume(self):
        return ('Volume = {:.2f}'.format(self.volume)) ##To bring the Volume as an output
    
    def set_surface_area(self):
        self.surface_area=(4*3.14*((self.radius)**2)) ##goes through the surface area formula

    def get_surface_area(self):
        return ('Surface Area = {:.2f}'.format(self.surface_area)) ##To bring the surface area as an output
    
    def __repr__(self):
        return ('Radius = {:.2f}'.format(self.radius), 'Volume = {:.2f}'.format(self.volume), 'Surface Area = {:.2f}'.format(self.surface_area))

class Point:
    def __init__(self): ##Initializes the coordinates
        self.x=0
        self.y=0

    def currentcoordinates(self): ##Shows current coordinates
        self.coordinates=[self.x,self.y]
        return self.coordinates
        
    def set_xy(self, x, y): ##Changes the coordinates
        self.x=x
        self.y=y

    def distancefinder(self): ## Finds the distance from a set coordinate, in my code it is [2,2]
        self.distance=[((self.x-2),' unit(s)'), ((self.y-2),' unit(s)')]
        return self.distance

    def __repr__(self):
        return ('Coordinates: {:.2f}'.format(self.coordinates))
        
##Client Code

ball=sphere() #Ball becomes an object for the sphere class

ball.setradius(int(input("enter the radius: "))) ##These three set the radius, volume and surface area after the input is given
ball.set_volume()
ball.set_surface_area()

print(ball.getradius())
print(ball.get_volume())
print(ball.get_surface_area())##These three bring the values out of the class and print them as outputs
##print(ball)##Prints the Object

p1=Point() #p1 (point1) becomes an object for the point class
print('Coordinates: ', p1.currentcoordinates()) ##shows initialized coordinates
p1.set_xy((int(input("enter the x-value: "))),(int(input("enter the y-value: ")))) ##b)When coordinates are changed
print('Coordinates: ', p1.currentcoordinates()) ##b)Shows new changed Coordinates
print('Distance from [2,2]: ', p1.distancefinder()) ##d)Finds distance from [2,2]
##print(p1)
    
