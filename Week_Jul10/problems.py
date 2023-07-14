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
        
