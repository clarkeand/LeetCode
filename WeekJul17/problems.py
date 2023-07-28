"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.
"""

def cakes(recipe, available):
    min_cakes = float('inf')
    for key in recipe: 
        try: 
            recipe_quotient = available[key]//recipe[key]
        except: 
            return 0
        if recipe_quotient < min_cakes: 
            min_cakes = recipe_quotient
    return min_cakes

"""In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246"""

def parse_int(string):
    num_map = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90,
        "hundred": 100, "thousand": 1000, "million": 1000000
    }

    split_words = string.replace("-", " ").split()
    result = 0
    current_number = 0
    last_multiplier = 1

    for word in split_words:
        if word == "and":
            continue

        # Handle compound numbers with hyphens
        word = word.replace("-", "")

        if word in num_map:
            value = num_map[word]

            # Handle multipliers (hundred, thousand, million)
            if value in [100, 1000, 1000000]:
                if value == 100 and current_number != 0:
                    current_number *= value
                else:
                    result += current_number * value
                    last_multiplier = value
                    current_number = 0
            else:
                current_number += value

    result += current_number
    return result

"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
"""

def complete_equation(num,opnum):
    if opnum[0] == "+":
        return num+opnum[1]
    elif opnum[0] == "-":
        return num-opnum[1]
    elif opnum[0] == "*":
        return num*opnum[1]
    else:
        return num//opnum[1]

def zero(op = ""): 
    if op == "": 
        return 0 
    else: 
        return complete_equation(0,op)
def one(op = ""): 
    if op == "": 
        return 1 
    else: 
        return complete_equation(1,op)
def two(op = ""): 
    if op == "": 
        return 2  
    else: 
        return complete_equation(2,op)
def three(op = ""): 
    if op == "": 
        return 3 
    else: 
        return complete_equation(3,op)
def four(op = ""): 
    if op == "": 
        return 4 
    else: 
        return complete_equation(4,op)
def five(op = ""): 
    if op == "": 
        return 5 
    else: 
        return complete_equation(5,op)
def six(op = ""): 
    if op == "": 
        return 6 
    else: 
        return complete_equation(6,op)
def seven(op = ""): 
    if op == "": 
        return 7 
    else: 
        return complete_equation(7,op)
def eight(op = ""): 
    if op == "": 
        return 8 
    else: 
        return complete_equation(8,op)
def nine(op = ""): 
    if op == "": 
        return 9 
    else: 
        return complete_equation(9,op)

def plus(num): return '+',num
def minus(num): return "-",num
def times(num): return "*",num
def divided_by(num): return '//',num

"""
In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
"""
def alphanumeric(password):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers= '0123456789'
    number_in_pw = False
    letter_in_pw = False
    for char in password:
        if char in numbers:
            number_in_pw = True
        elif char.lower() in alphabet: 
            letter_in_pw = True
        else:
            return False
    
    if number_in_pw == True or letter_in_pw == True: 
        return True
    
    return False