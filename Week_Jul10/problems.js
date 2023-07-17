function digitalRoot(n) {
    let stringN = String(n);
    let result = 0; 
    while (stringN > 9){
      result = 0; // Reset the result to 0 for each iteration
      for (let i = 0; i < stringN.length; i++){
        result += Number(stringN[i]);
      }
      if (result < 10){
        return result;
      }
      else{
        stringN = String(result); // Update stringN for the next iteration
      }
    }
    return Number(stringN);
}

/*Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. The input string can be assumed 
to contain only alphabets (both uppercase and lowercase) and numeric digits.*/

function duplicateCount(text) {
  let newString = "";
  let counter = 0;
  let duplicateString = "";
  
  for (let i = 0; i < text.length; i++) {
    let lowerCaseChar = text[i].toLowerCase();
    
    // Check if the character is in the new string but not in the duplicate string
    if (newString.includes(lowerCaseChar) && !duplicateString.includes(lowerCaseChar)) {
      counter += 1;
      duplicateString += lowerCaseChar; // Add the character to the duplicate string
    } 
    else if (!newString.includes(lowerCaseChar)) {
      newString += lowerCaseChar;
    }
  }
  
  return counter;
}