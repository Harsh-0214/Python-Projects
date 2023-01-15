from math import sqrt
class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def point


    def setlength(self):
        self.length= sqrt( (self.x2 - self.x1)**2 + (self.y2 - self.y1)**2 )

    def getlength(self):
        return ('distance: {:.2f}'.format(self.length))

    def equation(self):
        self.m=(self.y2-self.y1)
        

L1=line(1, 2, 3, 4)
L1.setlength()
print(L1.getlength())
