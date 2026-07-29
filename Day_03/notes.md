# Day 03 Notes - Python Strings

## Topics Covered

- String methods
- Palindrome
- Vowel & Consonant Counter
- Character Counter
- Reverse Each Word

---

## String Methods

| Method | Description |
|--------|-------------|
| lower() | Converts string to lowercase |
| upper() | Converts string to uppercase |
| title() | Converts first letter of every word to uppercase |
| split() | Splits a string into a list |
| join() | Joins list elements into a string |

---

## New Concepts Learned

### 1. isalpha()

Checks whether a character is an alphabet.

Example:

```python
'A'.isalpha()      # True
'5'.isalpha()      # False
```

---

### 2. Character Traversal

```python
for ch in text:
    print(ch)
```

Used to visit every character in a string.

---

### 3. Palindrome Logic

Reverse the string and compare it with the original.

Example:

madam → Palindrome

hello → Not Palindrome

---

### 4. Reverse Every Word

Steps:

1. Split the sentence into words.
2. Reverse each word.
3. Store the reversed words.
4. Join them back into a sentence.

---

## Mistakes I Made Today

- Compared integers with strings.
- Counted digits as consonants.
- Forgot correct indentation in nested loops.
- Used "constants" instead of "consonants".

---

## Key Takeaways

- Always use `isalpha()` before counting vowels or consonants.
- Python uses indentation to define code blocks.
- `split()` converts a string into a list.
- `join()` converts a list back into a string.