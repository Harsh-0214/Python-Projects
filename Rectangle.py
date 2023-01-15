#Harsh Tamakuwala
#662282
#Mr.Veera ICS4U0-2A
#1. Rectangle Review Part 1 of 5 Adobe Pg 574(Textbook Pg 184)
#2. Rectangle Review Part 2 of 5 Adobe Pg 575(Textbook Pg 185)
#February 25, 2021

#creates rectangle class
class rectangle:
    def __init__(self): #initializes rectangle class
        self.l= 0
        self.w= 0
        
    def setlength(self, l): #changes length value
        self.l=l
        
    def getlength(self): #returns length value
        return self.l
    
    def setwidth(self, w): #changes width value
        self.w=w
        
    def getwidth(self):#returns width value
        return self.w
    
    def area(self): #calculates area
        rectangle_area=((self.l)*(self.w))
        return rectangle_area
    def perimeter(self): #calculates perimeter
        rectangle_perimeter=((2*self.l)+(2*self.w))
        return rectangle_perimeter
    
    def __repr__(self):
        return ('Area = ', self.area(), 'Perimeter = ', self.perimeter())
        
##Client Code

shape=rectangle() #creates the object 'shape'


l_value=shape.getlength()
w_value=shape.getwidth()

print('Length of House is: {:.2f}'.format(l_value))
print('Width of House is: {:.2f}'.format(w_value))

shape.setlength(int(input('Length: ')))# able to set own length and width
shape.setwidth(int(input('Width: ')))

print("({}, {})".format(shape.l, shape.w))

print('New length is: %.2f and New width is %.2f and Area of shape is %.2f and perimeter of shape is %.2f'%(shape.getlength(), shape.getwidth(), shape.area(), shape.perimeter()))

print('Area of shape is: %.2f'%(shape.area()))
print('Perimeter of shape is: %.2f'%(shape.perimeter()))
##print(shape) #this print statement gives me an error

