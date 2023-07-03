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