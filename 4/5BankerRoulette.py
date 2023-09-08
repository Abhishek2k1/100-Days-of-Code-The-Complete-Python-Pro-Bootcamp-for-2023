import random
name_string = input("Give me everybody's names, separated by a comma. \n")
names = name_string.split(", ")
print(names)
print(len(names))

random_choice=random.randint(0, len(names)-1)

print(names[random_choice]+" will pay today!")



# shortcut for all this
random_choice2 = random.choice(names)
print(random_choice2+" will pay tomorrow!")