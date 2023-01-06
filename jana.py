def comic_condition(rating):
    MINT = 9.0
    FINE = 5.5
    GOOD = 3.0
    FAIR = 1.5
    POOR = 0
    if rating >= MINT:
        condition = ("near mint")
        return condition
    elif rating >= FINE and rating < MINT:
        condition = ("fine")
        return condition
    elif rating >= GOOD and rating < FINE:
        condition = ("good")
        return condition
    elif rating >= FAIR and rating < GOOD:
        condition = ("fair")
        return condition
    elif rating >= POOR and rating < FAIR:
        condition = ("poor")
        return condition
    else:
        print("Error")
        return condition

rating = int(input("Enter AQI: ")
comic_condition(rating)

    
    

    
