class Vehicle {

    constructor(type, model, parts, fuel) {

        this.type = type;
        this.model = model;
        this.parts = {
            engine: parts.engine,
            power: parts.power,
            quality: parts.engine * parts.power

        };

        this.fuel = fuel;

    }

    drive(fuelLoss) {

        this.fuel -= fuelLoss;

    }
    
}



// Input 1
let parts1 = { engine: 6, power: 100 };
let vehicle1 = new Vehicle('a', 'b', parts1, 200);
vehicle1.drive(100);
console.log(vehicle1.fuel);
console.log(vehicle1.parts.quality);
/*
100
600
*/


console.log('--------------------------------------------');



// Input 2
let parts2 = { engine: 9, power: 500 };
let vehicle2 = new Vehicle('l', 'k', parts2, 840);
vehicle2.drive(20);
console.log(vehicle2.fuel); // Output: 820
// 820
