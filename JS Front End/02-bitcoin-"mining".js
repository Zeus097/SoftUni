function calculateBitcoinPurchase(shiftGold) {
    const bitcoinPrice = 11949.16; // in lv
    const goldPricePerGram = 67.51; // in lv

    let totalMoney = 0; // total lv accumulated
    let bitcoinsBought = 0; // count of bitcoins bought
    let firstBitcoinDay = null; // day when the first bitcoin was bought

    for (let day = 0; day < shiftGold.length; day++) {
        let goldMined = shiftGold[day];

        // Check if it's a stealing day (every third day)
        if ((day + 1) % 3 === 0) {
            goldMined *= 0.7; // 30% is stolen
        }

        // Convert mined gold to money
        totalMoney += goldMined * goldPricePerGram;

        // Check if we can buy bitcoin(s) with the current amount of money
        while (totalMoney >= bitcoinPrice) {
            totalMoney -= bitcoinPrice; // Deduct bitcoin price
            bitcoinsBought++; // Increment bitcoin count

            // Record the day of the first bitcoin purchase if it hasn't been set
            if (firstBitcoinDay === null) {
                firstBitcoinDay = day + 1; // Days are 1-based in the output
            }
        }
    }

    // Output results
    console.log(`Bought bitcoins: ${bitcoinsBought}`);
    if (firstBitcoinDay !== null) {
        console.log(`Day of the first purchased bitcoin: ${firstBitcoinDay}`);
    }
    console.log(`Left money: ${totalMoney.toFixed(2)} lv.`);
}

// Test cases
calculateBitcoinPurchase([100, 200, 300]);
// Bought bitcoins: 2, 02-bitcoin-"mining".js:33, Day of the first purchased bitcoin: 2, 02-bitcoin-"mining".js:35, Left money: 10531.78 lv.


calculateBitcoinPurchase([50, 100]);
// Bought bitcoins: 0, Money left: 10126.50 lv.


calculateBitcoinPurchase([3124.15, 504.212, 2511.124]);
// Bought bitcoins: 30, Day of the first purchased bitcoin: 1, Money left: 5144.11 lv.
