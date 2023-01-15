#DigitExtractor

class digitextractor:

    def __init__(self, integer):
        self.integer=integer
        self.digits=[]
        
    def getinteger(self):
        return self.integer

    def __repr__(self):
        return (self)


num=digitextractor(int(input("Enter an Integer: ")))
print("Show (W)hole Number.")
print("Show (O)nes Place Number.")
print("Show (T)ens Place Number.")
print("Show (H)undreds Number.")
print("(Q)uit.")
choice=str(input("Enter your Choice: "))

num.seperate(num)


if (choice=="w" or "W" or choice=="o" or "O" or choice=="T" or "t" or choice=="h" or "H" or choice=="q" or "Q"):
    if (choice=="w" or "W"):
        print(num.getinteger()) 
    elif (choice=="o" or "O"):
        print('Digits: ', num.digits)
        
        
