print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))

if height>=120:
    print("You can ride the rollercoaster!")
    age=int(input("What is your age?"))
    if age<=12:
        print("please pay $7.")
    elif age<18:
        print("please pay $10.")
    elif age>=45 and age<=55:
        print("Everything is Free. Have a free ride")
    else:
      print("please pay $12.")  
else:
    print("Sorry, tou can have to grow taller before you can ride!")

# ==
# =!
# >=
# <=
