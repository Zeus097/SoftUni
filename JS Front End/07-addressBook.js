function solve(array) {
     
    let addressBook = {};

    for (let line of array) {
        let tokens = line.split(/:/);
        personName = tokens[0];
        address = tokens[1];

        addressBook[personName] = address
    }

    const sortedObject = {}
    const sortedKeys = Object.keys(addressBook).sort();

    for (const key of sortedKeys) {
        sortedObject[key] = addressBook[key];
    }

    let output = Object.entries(sortedObject)
    for ( [personName, street] of output ) {
        console.log(`${personName} -> ${street}`);
    }
    
}


solve([
    'Tim:Doe Crossing',
    'Bill:Nelson Place',
    'Peter:Carlyle Ave',
    'Bill:Ornery Rd'
])
// Bill -> Ornery Rd
// Peter -> Carlyle Ave
// Tim -> Doe Crossing


console.log('-------------------------');


solve([
    'Bob:Huxley Rd',
    'John:Milwaukee Crossing',
    'Peter:Fordem Ave',
    'Bob:Redwing Ave',
    'George:Mesta Crossing',
    'Ted:Gateway Way',
    'Bill:Gateway Way',
    'John:Grover Rd',
    'Peter:Huxley Rd',
    'Jeff:Gateway Way',
    'Jeff:Huxley Rd'
])
// Bill -> Gateway Way
// Bob -> Redwing Ave
// George -> Mesta Crossing
// Jeff -> Huxley Rd
// John -> Grover Rd
// Peter -> Huxley Rd
// Ted -> Gateway Way
