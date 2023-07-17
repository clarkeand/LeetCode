"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def domain_name(url):
    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]

    if url.startswith("www."):
        url = url[len("www."):]
        
    domain_name = ""
    for char in url:
        if char == '.':
            break
        domain_name += char

    return domain_name

"""
Encryption:

Write a function that takes in
1) A string made of capital letters with no spaces
2) A number n

Return a new string where all the characters have been "rotated forward" by n letters

For example, if the string was "HELLO" and n was equal to 2, the result would

be "JGNNQ", since "J" comes two letters after "H", etc.

Hint: You can use the function ord(c) to get the ASCII value of the character c.

You can also use chr(x) to turn the ASCII value x back into a character.

ord('A') # Gives 65
chr(65) # Gives 'A'
"""
#user_string = 'ABX', n = 3
def encrypt_by_n(user_string, n):
    new_string = ""
    for char in user_string: 
        letter_ascii = ord(char) 
        letter_ascii += n 
        if letter_ascii > ord('Z'):
            letter_ascii -= 26 
        new_string += chr(letter_ascii) 

    return new_string

"""
Reverse Map

Write a function that takes in a dictionary and returns a new dictionary where the keys and values have been reversed.

The values in the new dictionary should be sets, because multiple keys in the original dictionary can have the same value. For example, with

input = {
	'a': 1,
	'b': 3,
	'c': 1,
	'd': 4,
}

the output should be

output = {
	1: {'a', 'c'}
	3: {'b'}
	4: {'d'}
}
"""

def reverse_dictionary(user_dict):
    new_dict = dict()
    for key in user_dict:
        if new_dict[user_dict[key]] not in new_dict: 
            new_dict[user_dict[key]] = set(key)
        else:
            new_dict[user_dict[key]].add(key)
    
    return new_dict

print(reverse_dictionary({'a':1,'b':2,'c':1}))

"""
def reverse_dictionary(dict):
    
    new_dict = {}

    for key in dict:
        value = dict[key]
        if value not in new_dict:
            new_dict[value] = {key}
        else:
            new_dict[value].add(key)

    return new_dict"""

"""
Transpose

Take in a 2D grid like
[
	[1, 2, 3],
	[4, 5, 6, 7],

Return a new grid that has been "transposed", or flipped diagonally so that the rows become columns and vice versa:
[
	[1, 4],
	[2, 5],
	[3, 6],
    [_, 7]
]
"""

# Make a new list of lists (outside of whole loop)

[
    [1, 4]
]

def transpose(input_grid):
    new_grid = []
    for col_idx in range(len(input_grid[0])): # 0
        new_grid.append([])
        for row_idx in range(len(input_grid)): # 1
            new_grid[col_idx].append(input_grid[row_idx][col_idx])
    return new_grid

print(transpose([
	[1, 2, 3],
	[4, 5, 6],
]))

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for num in arr: 
        if num > 0: 
            positive_count += 1
        elif num < 0: 
            negative_count += 1
        else: 
            zero_count += 1
    
    print(positive_count/len(arr))
    print(negative_count/len(arr))
    print(zero_count/len(arr))

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    lowest_sum = 0
    highest_sum = 0 
    for i in range(len(arr)): 
        if i == 0: 
            lowest_sum += arr[i]
        elif i == 4:
            highest_sum += arr[i]
        else:
            lowest_sum += arr[i]
            highest_sum += arr[i]
    print (f"{lowest_sum} {highest_sum}")