#Harsh Tamakuwala
#662282
#Mr.Veera ICS4U0-2A
#MySavings Adobe Pg 598(Textbook Pg 208)
#February 26, 2021

class bank:

    def __init__(self, numpennies, numnickels, numdimes, numquarters):
        self.numpennies=0
        self.numnickels=0
        self.numdimes=0
        self.numquarters=0

    def addingcoins(self):
        numpennies=int(input('add a penny: '))
        numnickels=int(input('add a nickel: '))
        numdimes=int(input('add a dime: '))
        numquarters=int(input('add a quarter: '))

    def removingcoins(self):
        pass

    def balance(self):
        pennytotal=numpennies
        nickeltotal=(5*numnickels)
        dimetotal=(10*numdimes)
        quartertotal=(25*numquarters)
        totalbalance=(pennyotal+nickeltotal+dimetotal+quartertotal)
        return (totalbalance)

    def __repr__(self):
        return(self, numpennies, numnickels, numdimes, numquarters)



piggybank=bank()
