function processCrystals(input) {
    const targetThickness = input[0];
    const chunks = input.slice(1);

    chunks.forEach((chunk) => {
        console.log(`Processing chunk ${chunk} microns`);
        let thickness = chunk;
        let operations = [];

        function performOperation(operation, operationFunc) {
            let count = 0;
            while (operationFunc()) {
                count++;
            }
            if (count > 0) {
                operations.push(`${operation} x${count}`);
                operations.push("Transporting and washing");
                thickness = Math.floor(thickness);
            }
        }

        performOperation("Cut", () => {
            if (thickness / 4 >= targetThickness) {
                thickness /= 4;
                return true;
            }
            return false;
        });

        performOperation("Lap", () => {
            if (thickness * 0.8 >= targetThickness) {
                thickness *= 0.8;
                return true;
            }
            return false;
        });

        performOperation("Grind", () => {
            if (thickness - 20 >= targetThickness) {
                thickness -= 20;
                return true;
            }
            return false;
        });

        performOperation("Etch", () => {
            if (thickness - 2 >= targetThickness - 1) { // Allows for X-ray adjustment
                thickness -= 2;
                return true;
            }
            return false;
        });

        if (thickness < targetThickness) {
            operations.push("X-ray x1");
            thickness += 1;
        }

        operations.forEach(op => console.log(op));
        console.log(`Finished crystal ${targetThickness} microns`);
    });
}


processCrystals([1375, 50000]);
// Processing chunk 50000 microns
// Cut x2
// Transporting and washing
// Lap x3
// Transporting and washing
// Grind x11
// Transporting and washing
// Etch x3
// Transporting and washing
// X-ray x1
// Finished crystal 1375 microns


console.log('--------------------------------------------------');


processCrystals([1000, 4000, 8100]);
// Processing chunk 4000 microns
// Cut x1
// Transporting and washing
// Finished crystal 1000 microns
// Processing chunk 8100 microns
// Cut x1
// Transporting and washing
// Lap x3
// Transporting and washing
// Grind x1
// Transporting and washing
// Etch x8
// Transporting and washing
// Finished crystal 1000 microns
