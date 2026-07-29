
"""
Day 03 - Python String Practice

Author: Muskan
Topics:
- String Methods
- Palindrome
- Character Counting
- Reverse Each Word
"""

## Program 1 - String Case Converter



name = input("Enter your name :")

print("Original :", name)
print("Lower    :", name.lower())
print("Upper    :", name.upper())
print("Title    :", name.title())



# Program 2 - Palindrome Checker


string = input("Enter a string :")
rev_string =''

for ch in string:
    rev_string = ch + rev_string

if string == rev_string:
    print(f'{string} is a palindrome')
else:
    print(f'{string} is not a palindrome')



# Program 3 - Vowel & Consonant Counter



text = input("Enter text :")

count_vowels = 0
count_consonants = 0
for ch in text :
    if ch.isalpha():
       if ch.lower() in "aeiou":
           count_vowels += 1
       else:
           count_consonants += 1

print(f"Number of vowels in {text} is {count_vowels}")
print(f"Number of constants in {text} is {count_consonants}") 




# Program 3 - Count uppercase, lowercase, digits, and spaces in the input string



password = input("Enter password: ")
uppercase = 0
lowercase = 0
digit = 0
space = 0
for ch in password:
    if 'A' <= ch <= 'Z':
        uppercase += 1
    elif 'a' <= ch <= 'z':
        lowercase += 1
    elif '0' <= ch <= '9':
        digit += 1
    elif ch == ' ':
        space += 1
print(f'Uppercase : {uppercase}')
print(f'Lowercase : {lowercase}')
print(f'Digit : {digit}')
print(f'Space : {space}')




 # Program 5 - Reverse Each Word
   

sentence = input("Enter Sentence :")

words = sentence.split()

new_words = []

for word in words:
    rev_word = ""

    for ch in word:
        rev_word = ch + rev_word
    new_words.append(rev_word)
    

print(" ".join(new_words))