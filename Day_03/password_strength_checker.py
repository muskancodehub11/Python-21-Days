

## Password Strength Checker

password = input("Enter your password :")
special_chars = "@#$%^&*!"
score = 0
upper = 0
lower = 0
digit = 0
special = 0
score = 0

for char in password:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char in special_chars:
            special += 1


if len(password) >= 8:   
    score += 1

if upper > 0:            
    score += 1

if lower > 0:            
    score += 1

if digit > 0:            
    score += 1

if special > 0:          
    score += 1     

print(f"Password Score: {score}/5")     

if score <= 2:
    print("\n🔴 Your password is Weak!")

elif score <= 4:
    print("\n🟡 Your password is Medium!")

else:
    print("\n🟢 Your password is Strong!")

if score < 5:
    print("\nSuggestions:")

    if len(password) < 8:
        print("❌ Make it at least 8 characters long.")

    if upper == 0:
        print("❌ Add an uppercase letter.")

    if lower == 0:
        print("❌ Add a lowercase letter.")

    if digit == 0:
        print("❌ Add a digit.")

    if special == 0:
        print("❌ Add a special character.")