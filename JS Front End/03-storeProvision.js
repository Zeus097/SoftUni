function solve(stock, orders) {
    // Every even index -> product name
    // every odd index -> product quantity
    
    const store = {};

    let counter = 0
    while (stock.length != 0) {
        let productName = stock[counter];
        let productQuantity = parseInt(stock[counter + 1], 10);

        store[productName] = productQuantity;
        stock.splice(0, 2);
    }

    for (let i = 0; i < orders.length; i += 2) {
        let orderName = orders[i];
        let orderQuantity = parseInt(orders[i + 1], 10);

        if ( store.hasOwnProperty(orderName) ) {
            store[orderName] += orderQuantity
        }else{
            store[orderName] = orderQuantity
        }
    }
    
    const productEntries = Object.entries(store)
    for ( [ product, quantity ] of productEntries ) {
        console.log(`${product} -> ${quantity}`);
    }

}


solve([
    'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
    'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ])
// Chips -> 5
// CocaCola -> 9
// Bananas -> 44
// Pasta -> 11
// Beer -> 2
// Flour -> 44
// Oil -> 12
// Tomatoes -> 70


console.log('--------------------');


solve([
    'Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'
    ],
    [
    'Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30'
    ])
// Salt -> 2
// Fanta -> 4
// Apple -> 21
// Water -> 4
// Juice -> 5
// Sugar -> 44
// Oil -> 12
// Tomatoes -> 7
// Bananas -> 30
