function solve(num) {
    
    let number = num.toString();

    function getDigitAverage(numberString) {
        let sum = 0;
        for (let digit of numberString) {
            sum += parseInt(digit, 10);
        }
        return sum / numberString.length;
    }

    while (getDigitAverage(number) <= 5) {
        number += '9';
    }

    console.log(number);

}


solve(101); // 1019999
solve(5835); // 5835
