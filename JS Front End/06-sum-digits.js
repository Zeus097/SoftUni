function solve(number) {
    let sum = 0;
    let digits = number.toString();
    for (let digit of digits) {
        sum += parseInt(digit);
    }
    console.log(sum);

}

solve(245678) // Output: 32
solve(97561) // Output: 28
solve(543) // Output: 12
