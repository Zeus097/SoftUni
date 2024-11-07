calculate = (numOne, numTwo, operator) => ({
    'multiply': numOne * numTwo,
    'divide': numOne / numTwo,
    'add': numOne + numTwo,
    'subtract': numOne - numTwo
}[operator]);


console.log(calculate(5, 5, 'multiply')); // 25
console.log(calculate(40, 8, 'divide')); // 5
console.log(calculate(12, 19, 'add')); // 31
console.log(calculate(50, 13, 'subtract')); // 37
