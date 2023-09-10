def isPrime(number):
    is_prime=True
    for n in range(2, number):
        if number%n==0:
            is_prime=False
# this is print statement
    if is_prime:
        print("it is Prime") 
    else:
        print("it is not Prime number")
            

isPrime(int(input("Check this number: ")))