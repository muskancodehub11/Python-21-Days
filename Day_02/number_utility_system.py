



def menu():
   print("\n===== Number Utility System =====")
   print("1.Even Number")
   print("2.Odd Number")
   print("3.Prime Number")
   print("4.Factorial Of Number")
   print("5.Exit")



#find even number

def even_number():
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is an Even Number")
    else:
        print(f"{num} is not an Even Number")



#find odd number


def odd_number():
    num = int(input("Enter a number: "))

    if num % 2 != 0:
        print(f"{num} is an Odd Number")
    else:
        print(f"{num} is not an Odd Number")


#find prime number

def prime_number():
    num = int(input("Enter a number: "))

    if num < 2:
        print(f"{num} is not a prime number")
        return

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")



#find Factorial of number


def fact():
    num1 = int(input("Enter a number: "))
    fact = 1
    i = 1

    if num1 < 0:
        print("Factorial is not possible for negative numbers")
    else:
        while i <= num1:
            fact *= i
            i += 1
        print(f"Factorial of {num1} is {fact}")



while True:
    menu()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        even_number()

    elif choice == 2:
        odd_number()

    elif choice == 3:
        prime_number()

    elif choice == 4:
        fact()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid Choice")