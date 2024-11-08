function sum(a, b, c) {
    let sumNums = a + b;

    let subtract = c => sumNums - c;

    console.log(subtract(c))
}

sum(23, 6, 10) // 19
sum(1, 17, 30) // -12
sum(42, 58, 100) // 0
