function solve(numOne, numTwo, numThree) {
    
    let negativeCounter = 0;

    if (numOne < 0) negativeCounter++;
    if (numTwo < 0) negativeCounter++;
    if (numThree < 0) negativeCounter++;

    if ( negativeCounter === 1 || negativeCounter === 3 ) {
        console.log('Negative');
    }else {
        console.log('Positive');
    }

}

solve(5, 12, -15) // Negative
solve(-6, -12, 14) // Positive
solve(-1, -2, -3) // Negative
solve(-5, 1, 1) // Negative
