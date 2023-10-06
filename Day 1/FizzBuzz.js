/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let result = [];
    for (let i=1; i<n+1; i+=1){

    const divisibleBy3 = (i % 3 === 0);
    const divisibleBy5 = (i % 5 === 0);

    if (divisibleBy3 && divisibleBy5){
        result.push("FizzBuzz");
    }
    else if (divisibleBy3){
        result.push("Fizz");
    }
    else if (divisibleBy5){
        result.push("Buzz");
    }
    else {
        result.push(i.toString());
    }}
    return result;
};