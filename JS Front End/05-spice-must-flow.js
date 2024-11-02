function solve(startingYield) {
    let days = 0;
    let totalSpice = 0;
    
    // Mine as long as the yield is at least 100
    while (startingYield >= 100) {
        days++;
        totalSpice += startingYield;
        
        // Daily consumption of 26 spices
        totalSpice -= 26;
        
        // Yield decreases by 10 after each day
        startingYield -= 10;
    }
    
    // Final consumption of 26 spices after the mining is abandoned, if there is spice left
    if (totalSpice >= 26) {
        totalSpice -= 26;
    }
    
    console.log(days);
    console.log(totalSpice);
}

// Example usage:
solve(111);  // 2, 134
solve(450);  // 36, 8938
