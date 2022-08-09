def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        if is_prime:
            print("Is a prime number")
        else:
            print("Is NOT a prime number")
        break

num = int(input("Enter a number. I will let you know if the number is prime or not\n"))
prime_checker(number=num)