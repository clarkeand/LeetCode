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
        