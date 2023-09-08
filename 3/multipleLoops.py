print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))
bill=0
if height>=120:
    print("You can ride the rollercoaster!")
    age=int(input("What is your age?"))
    if age<=12:
        bill=7
        print("please pay $7.")
    elif age<18:
        bill=10
        print("please pay $10.")
    else:
      bill=12
      print("please pay $12.")

    wants_photo = input("Do you want photo taken? Y or N")
    if wants_photo=="Y":
        bill=bill+3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, tou can have to grow taller before you can ride!")

# ==
# =!
# >=
# <=
