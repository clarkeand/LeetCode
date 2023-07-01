# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    x = 0
    sum = 0
    while x < number: 
        if x % 3 == 0 or x % 5 == 0:
            sum += x
        x += 1
        
    return sum

"""In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words."""

from preloaded import MORSE_CODE

def decode_morse(morse_code):
    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example: 
    # MORSE_CODE['.-'] = 'A'
    # MORSE_CODE['--...'] = '7'
    # MORSE_CODE['...-..-'] = '$'
    
    morse_list = morse_code.split(" ")
    return_word = ""
    dbl_space = 0
    for morse in morse_list: 
        if morse == "" and dbl_space == 1:
            return_word += " "
            dbl_space = 0
        elif morse == "": 
            dbl_space += 1
        else:
            return_word += MORSE_CODE[morse]
        
    return return_word.lstrip().rstrip()


"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        new_num_list = []
        return_num = ""
        
        for digit in x:
            new_num_list.append(digit)

        if new_num_list[0] == '-':
            return_num += new_num_list.pop(0)

        while new_num_list != []:
            return_num += new_num_list.pop()

        return_num = int(return_num)

        if return_num >= 2147483647 or return_num <= -2147483648: 
            return 0
    
        return return_num