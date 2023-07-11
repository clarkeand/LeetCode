"""
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""
#include <string>
using namespace std ; 

string reverseString (string str )
{
  string return_string = "";
  for (int i = str.size()-1; i >= 0; i--){
    return_string += str[i];
  }
    
  return return_string;
}

"""
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?
"""

#include <string>

std::string number_to_string(int num) {
  std::string str = std::to_string(num);
  return str;
}