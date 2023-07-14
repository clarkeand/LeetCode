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