print("Welcome to love calculator!!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

name1_low = name1.lower()
name2_low = name2.lower()
true=name1_low.count("t")+name1_low.count("r")+name1_low.count("u")+name1_low.count("e")+name2_low.count("t")+name2_low.count("r")+name2_low.count("u")+name2_low.count("e")
love=name1_low.count("l")+name1_low.count("o")+name1_low.count("v")+name1_low.count("e")+name2_low.count("l")+name2_low.count("o")+name2_low.count("v")+name2_low.count("e")
total=int(str(true)+str(love))

if total<10 or total>90:
    print(f"Your Score is {total}, you go together like coke and mentos")
elif total>=40 and total<=50:
    print(f"Your score is {total}, you are alright together")
else:
    print(f"Your score is {total}")