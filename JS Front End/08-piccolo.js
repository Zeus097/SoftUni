function solve(input) {
    const parkingLot = new Set();

    for (const entry of input) {

        const [direction, carNumber] = entry.split(', ');
        
        if (direction === 'IN') {
            parkingLot.add(carNumber);

        } else if (direction === 'OUT') {

            parkingLot.delete(carNumber);

        }

    }

    if (parkingLot.size === 0) {

        console.log("Parking Lot is Empty");

    } else {

        [...parkingLot]
            .sort()
            .forEach(car => console.log(car));

    }
    
}



solve([
    'IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'IN, CA9999TT',
    'IN, CA2866HI',
    'OUT, CA1234TA',
    'IN, CA2844AA',
    'OUT, CA2866HI',
    'IN, CA9876HH',
    'IN, CA2822UU'
]);
/*
CA2822UU
CA2844AA
CA9876HH
CA9999TT
*/


console.log('-----------------------');


solve([
    'IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'OUT, CA1234TA'
]);
// Parking Lot is Empty
