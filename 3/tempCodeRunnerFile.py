print("Welcome to love calculator!!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

name1_low = name1.lower()
name2_low = name2.lower()
true=name1_low.count("t")+name1_low.count("r")+name1_low.count("u")+name1_low.count("e")+name2_low.count("t")+name2_low.count("r")+name2_low.count("u")+name2_low.count("e")
print(true)