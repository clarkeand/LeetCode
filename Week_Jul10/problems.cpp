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