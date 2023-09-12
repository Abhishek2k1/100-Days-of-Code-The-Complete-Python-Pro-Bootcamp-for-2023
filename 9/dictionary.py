programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

# Retreving items from a dictionary

print(programming_dictionary["Bug"])
#    adding element in dictionary
programming_dictionary["loop"]="The action of doing something over and over again"
print(programming_dictionary)


# creating empty dictionary 
empty_dictionary={}

# empty dictionary 
# programming_dictionary={}
# print(programming_dictionary)

# loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
