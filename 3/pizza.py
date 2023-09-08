print("Welcome to Python Pizza Delivaries")
size = input("What size do you want? S, M, or L ")
add_pepperoni = input("Do you want peparony? Y or N ")
extra_cheese = input("Do you want cheese? Y or N ")

bill=0

if size== "S":
    bill+=15
    
        

elif size == "M":
    bill+=20

else:
    bill+=25

if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if extra_cheese=="Y":
    bill+=1

print(f"Your bill is {bill}")