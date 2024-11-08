function solve(num) {
    
    let evenNums = 0, oddNums = 0;
    const digits = num.toString().split('').map(Number);
    for (number of digits) {
        if (number % 2 == 0) evenNums += number
        if (number % 2 != 0) oddNums += number
    }

    console.log(`Odd sum = ${oddNums}, Even sum = ${evenNums}`)
    
}

solve( 1000435) // Odd sum = 9, Even sum = 4
solve( 3495892137259234) // Odd sum = 54, Even sum = 22
