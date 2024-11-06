function pyramidResources(base, increment) {
    let stone = 0;
    let marble = 0;
    let lapis = 0;
    let gold = 0;
    let steps = 0;

    while (base > 2) {
        steps++;
        let outerLayer = (base * 4) - 4; // Calculate outer layer blocks
        let innerArea = (base - 2) ** 2; // Calculate inner area blocks

        // Check if it's every fifth layer for lapis lazuli
        if (steps % 5 === 0) {
            lapis += outerLayer * increment;
        } else {
            marble += outerLayer * increment;
        }

        stone += innerArea * increment; // Add to stone required
        base -= 2; // Reduce base for the next step
    }

    // Add the final step (top) made out of gold
    steps++;
    gold = base * base * increment;

    // Calculate the final height
    const height = Math.floor(steps * increment);

    // Print the results
    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapis)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${height}`);
}


pyramidResources(11, 1);

// Stone required: 165, Marble required: 112, 
// Lapis Lazuli required: 8, Gold required: 1, Final pyramid height: 6
console.log('-------------------------------------------------------------');




pyramidResources(11, 0.75);

// Stone required: 124, Marble required: 84, Lapis Lazuli required: 6, 
// Gold required: 1, Final pyramid height: 4
console.log('-------------------------------------------------------------');



pyramidResources(12, 1);

// Stone required: 220, Marble required: 128, Lapis Lazuli required: 12, 
// Gold required: 4, Final pyramid height: 6
console.log('-------------------------------------------------------------');




pyramidResources(23, 0.5);

// Stone required: 886, Marble required: 228, Lapis Lazuli required: 36, 
// Gold required: 1, Final pyramid height: 6
console.log('-------------------------------------------------------------');
