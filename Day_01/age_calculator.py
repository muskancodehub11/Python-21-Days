name = input("Enter your name: ")
print(f'Welcome, {name}! Let\'s calculate your age.')
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))
if current_year >= birth_year:
    current_age = current_year - birth_year
    print(f'Your current age is: {current_age} years old.')
    if current_age >= 18:
      print("You are eligible to vote.")
    else:
      print("You are not eligible to vote.")
    days_lived = current_age * 365
    print(f'You have lived approximately {days_lived} days.')
else:
    print("Invalid input. The current year must be greater than your year of birth.")
   
