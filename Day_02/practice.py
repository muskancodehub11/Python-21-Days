

# Factorial of a number

num = int(input("Enter a number: "))
fact = 1
i = 1

if num < 0:
    print("Factorial is not possible for negative numbers")
else:
    while i <= num:
        fact *= i
        i += 1

    print(f"Factorial of {num} is {fact}")






#find prime number

number = int(input("Enter a number:"))
is_prime = True
if number > 1:
    for i in range(2,number):
        if number % i == 0:
            is_prime = False 
            print(f'{is_prime}, {number} is not a prime number')
            break
print(f'{is_prime}, {number} is prime a number')

#the waiting time after each failed attempt.

import time
wait_time = 1
max_retries = 5
attempts = 0
while attempts < max_retries:
    print("Attempt", attempts+1, "wait time", wait_time,)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
  