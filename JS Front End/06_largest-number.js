function largestNum(num1, num2,num3) {
    let number;

    if (num1 > num2 && num1 > num3) {
            number = num1;
        }else if (num2 > num1 && num2 > num3) {
            number = num2;
        }else if (num3 > num1 && num3 > num2) {
            number = num3;
        }
    
    console.log(`The largest number is ${number}.`)
}

largestNum(5, -3, 16) // The largest number is 16.
largestNum(-3, -5, -22.5) // The largest number is -3
