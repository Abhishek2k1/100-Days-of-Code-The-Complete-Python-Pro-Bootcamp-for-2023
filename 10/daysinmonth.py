year = int(input("Which year do you want to check?"))

def isLeap(year)
    if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
        return True
    else:
        return False
    

