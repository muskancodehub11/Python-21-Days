
# Day 04 - Python List & Matrix Practice




# Program 1: Access Element from Nested List


L = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

print(L[0][0][1])



# Program 2: List extend() Method


L = [1, 2, 3, 4, 5]

L.extend("delhi")

print(L)



# Program 3: Delete Element using del


L = [1, 2, 3, 4, 5]

del L[1]

print(L)



# Program 4: Membership Operators (in / not in)


L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 3, 4, [5, 6]]

print(5 not in L2)
print([5, 6] in L2)



# Program 5: List Comprehension with Condition


languages = ['java', 'python', 'php', 'c', 'javascript']

x = [language for language in languages if language.startswith('p')]

print(x)




# Program 6: zip() with List Comprehension


L1 = [1, 2, 3, 4]
L2 = [-1, -2, -3, -4]

pairs = list(zip(L1, L2))

print(pairs)

sum_list = [i + j for i, j in pairs]

print(sum_list)


# Program: Sum of Current Element and All Greater Elements

l = [2, 4, 6, 10, 1]

result = []

for i in l:
    total = i

    for j in l:
        if j > i:
            total = total + j

    result.append(total)

print(result)




# Program 8: Find Common Elements in Two Lists


num1 = [23, 45, 67, 78, 89, 34]
num2 = [34, 89, 55, 56, 39, 67]

common = []

for i in num1:
    if i  in num2 :
        common.append(i)


common.sort()

print(common)




# Program 9: Maximum Element from Each Row


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_list = []

for row in matrix:
    new_list.append(max(row))

print(new_list)



# Program 10: Create Matrix using
# Nested List Comprehension


matrix = [[i * 3 + j for j in range(3)] for i in range(3)]

print(matrix)



# Program 11: Matrix Transpose using
# List Comprehension


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("Transpose Matrix:")

for row in transpose:
    print(row)




# Program 12: Flatten a Matrix using
# List Comprehension


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flatten = [num for row in matrix for num in row]

print(flatten)




# Program 13: Sort Alphanumeric Strings Based on Product of Digits


l = ['1ac21', '23fg', '456', '098d', '1', 'kls']

temp = []

for i in l:
    product = 1

    for j in i:
        if j.isdigit():
            product = product * int(j)

    temp.append([product, i])

temp.sort()

result = []

for i in temp:
    result.append(i[1])

print(result)