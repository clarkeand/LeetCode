"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"""

def to_camel_case(text): 
    if text == "" or None: 
        return ""
    
    new_string = ""
    for char in text: 
        if char in "_-": 
            char = " "
        new_string += char
        
    text_list = new_string.split()
    camel_case = text_list.pop(0)
    for text in text_list: 
        camel_case += text[0].upper()+text[1:]
        
    return camel_case

"""
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
"""
        
def is_prime(num):
    
    if num <= 0 or num == 1: 
        return False
    
    i = 1
    
    while i < 100000: 
        if num % i == 0 and i != 1:
            return False
        i += 1
        if i == num: 
            return True
        
    return True

"""In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )"""

def alphabet_position(text):
    
    alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,
             'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    return_string = ""
    
    for char in text:
        char = char.lower()
        if char in alphabet.keys():
            return_string += str(alphabet[char]) + " "
            
    return return_string.rstrip()
    
"""
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)
"""

def tribonacci(signature, n):
    if n == 0: 
        return []
    
    trib_list = []
    
    if n <= 3: 
        i = 0 
        while i <= n-1:
            trib_list.append(signature[i])
            i += 1 
        return trib_list
    
    i = 0
    sum = 0
    for num in signature: 
        trib_list.append(num)
    while i < n-3:
        for num in signature:
            sum += num
        trib_list.append(sum)
        signature.pop(0)
        signature.append(sum)
        i+=1
        sum = 0
    return trib_list

"""Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character."""

def tower_builder(n_floors):
    num_stars = 1
    num_spaces = n_floors * 2 - 2
    floors_list = []
    
    if n_floors == 1: 
        return ['*']
    
    for i in range(n_floors):
        floors_list.append((" "*(num_spaces//2)) + ("*"*num_stars) + (" "*(num_spaces//2)))
        num_stars += 2
        num_spaces -= 2
                    
    return floors_list

"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
"""

def generate_hashtag(s):
    #Set False return points
    if s == "" or len(s)>140: 
        return False
    
    #If any whitespace exists get rid of it
    if s[0] == " ":
        s.lstrip()
    if s[-1] == " ":
        s.rstrip()
        
    #split by whitespace and start a return string with a hashtag
    string_list = s.split()
    return_string = "#"
    
    #go through return string list and make the first letter uppercase and the return lowercase by slicing
    for word in string_list: 
        return_string += word[0].upper() + word[1:].lower()
        
    return return_string

"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

def is_pangram(s):
    alpha_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z'}
        
    for char in s: 
        char = char.lower()
        if char in alpha_set: 
            alpha_set.remove(char)
            
    if len(alpha_set) == 0: 
        return True
    return False

"""The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod."""

def productFib(prod):
    fib_array = [0, 1]  # Initial values of the Fibonacci sequence

    # Generate Fibonacci numbers dynamically until prod is reached or surpassed
    while fib_array[-1] * fib_array[-2] < prod:
        fib_array.append(fib_array[-1] + fib_array[-2])

    # Check if the product is equal to prod
    if fib_array[-1] * fib_array[-2] == prod:
        return [fib_array[-2], fib_array[-1], True]
    else:
        return [fib_array[-2], fib_array[-1], False]
    
#Write a function that given, an array arr, returns an array containing at each index i the amount of numbers that are smaller than arr[i] to the right.

def smaller(arr):
    output_array = []
    
    for i in range(len(arr)):
        counter = 0
        current_num = arr[i]
        for j in range(i+1, len(arr)):
            if current_num > arr[j]:
                counter += 1
        output_array.append(counter)
        
    return output_array

# 'return a list with the reverse order of l'
def reverse_list(l):
    stack = []
    while len(l) > 0: 
        stack.append(l.pop())
        
    return stack

"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""

def make_readable(seconds):
    hours = (seconds/60)/60
    minutes = (hours - int(hours))*60
    seconds = (minutes - int(minutes)) * 60
    seconds = round(seconds)
    
    if seconds == 60:
        minutes += 1
        seconds = 0
    
    string = f"{int(hours):02d}:{int(minutes):02d}:{seconds:02d}"
    return string 

"""
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of 
�
3
n 
3
 , the cube above will have volume of 
(
�
−
1
)
3
(n−1) 
3
  and so on until the top which will have a volume of 
1
3
1 
3
 .

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?
"""

import math

def find_nb(m):
    total_cubes = 0
    n = 0
    while total_cubes < m: 
        total_cubes += pow(n,3)
        n += 1
        
    if total_cubes == m: 
        return n - 1
    return -1

#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(lst):
    indeces_contain_zero = []
    
    for i in range(len(lst)-1): 
        if lst[i] == 0:
            indeces_contain_zero.append(i)
            
    index_adjust = 0
    for item in indeces_contain_zero: 
        lst.pop(item-index_adjust)
        lst.append(0)
        index_adjust += 1
        
    return lst