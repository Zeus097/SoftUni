function solve(product, quantity) {
    let coffeePrice = 1.50, waterPrice = 1.00, cokePrice = 1.40, snacksPrice = 2.00
    let totalPrice = 0

    switch (product) {
        case 'coffee':
            totalPrice += quantity * coffeePrice
            break;
    
        case 'water':
            totalPrice += quantity * waterPrice
            break;

        case 'coke':
            totalPrice += quantity * cokePrice
            break;
        
        case 'snacks':
            totalPrice += quantity * snacksPrice
            break;
    }

    console.log(totalPrice.toFixed(2));

}

solve("water", 5) // 5.00
solve("coffee", 2) // 3.00
