function solve(lostFightsCount,  helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let expenses = 0;
    let brokenShieldCount = 0;

    for (let i = 1; i <= lostFightsCount; i++) {
        let brokenHelmet = false;
        let brokenSword = false;
        
        if ( i % 2 === 0 ) {
            brokenHelmet = true;
            expenses += helmetPrice;
        }
        
        if ( i % 3 === 0) {
            brokenSword = true;
            expenses += swordPrice;
        }
        
        if ( brokenHelmet && brokenSword ) {
            brokenShieldCount ++;
            expenses += shieldPrice

            if ( brokenShieldCount % 2 == 0) {
                expenses += armorPrice;
            }
        }

    }

    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);
    
}


solve(7, 2, 3, 4, 5) // Gladiator expenses: 16.00 aureus
// Trashed helmet -> 3 times; Trashed sword -> 2 times; Trashed shield -> 1 time; Total: 6 + 6 + 4 = 16.00 aureus;

solve(23, 12.50, 21.50, 40, 200) // Gladiator expenses: 608.00 aureus
