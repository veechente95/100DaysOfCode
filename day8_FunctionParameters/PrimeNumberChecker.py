def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
        if prime:
            print("Your number is prime number")
        else:
            print("Your number is NOT a prime number")
        break


num = int(input("Enter your number. I will let you know if it is a prime number: "))
prime_checker(number=num)
