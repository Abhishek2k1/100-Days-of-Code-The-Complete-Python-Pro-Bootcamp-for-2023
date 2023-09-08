year = int(input("Which year do you want to check?"))

if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
    print("leap")
else:
    print("not leap")
