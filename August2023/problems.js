//Given a positive integer millis, write an asynchronous function 
//that sleeps for millis milliseconds. It can resolve any value.

/*
 * @param {number} millis
 */
async function sleep(millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
}

/*Write a function createHelloWorld. It should return 
a new function that always returns "Hello World".*/

var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    }
};