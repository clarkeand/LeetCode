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

#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

def timeConversion(s):
    hours = int(s[0:2])
    minutes = int(s[3:5])
    seconds = int(s[6:8])
    am_or_pm = s[8:10]
    
    if hours == 12 and am_or_pm == "AM":
        return f"00:{minutes:02d}:{seconds:02d}"
    
    if am_or_pm == 'PM' and hours != 12:
        hours += 12
        
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

#Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = dict()
        
        for num in arr:
            if num not in counter.keys():
                counter[num] = 1
            else:
                counter[num]+=1
                
        unique_list = []
        
        for key in counter.keys():
            if counter[key] in unique_list: 
                return False
            else:
                unique_list.append(counter[key])
        return True
    
"""
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.
"""
    
class Solution(object):
    def minOperations(self, boxes):
        num_list = []
        result_list = []
        sum_nums = 0
        for char in boxes: 
            num_list.append(int(char))
            if char == "1":
                sum_nums += 1
            
        for i in range(len(num_list)):
            counter = 0
            for j in range(len(num_list)):
                if num_list[j] == 1:
                    counter += abs(j - i)
            result_list.append(counter)
    
        return result_list
    
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()  # Dummy node to simplify the code
        curr = dummy  # Pointer to the current node
        carry = 0  # Carry digit

        while l1 or l2 or carry:
            # Calculate the sum of current digits and carry
            sum_val = carry

            # If l1 is not None, add its value to sum_val
            if l1:
                sum_val += l1.val
                l1 = l1.next

            # If l2 is not None, add its value to sum_val
            if l2:
                sum_val += l2.val
                l2 = l2.next

        # Update the carry and create a new node for the sum_val
            carry = sum_val // 10
            curr.next = ListNode(sum_val % 10)
            curr = curr.next

        return dummy.next