row1=["x","o","x"]
row2=["x","x"," "]
row3=[" ","x","o"]
tictactoe=[row1, row2, row3]
for symbols in range(len(row1)):
    for rows in range(len(tictactoe)):
        print(tictactoe[symbols][rows]," ",end="")
    print()
