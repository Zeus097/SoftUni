function solve(name, lastName, hairColor) {
    
    let person = {
        name,
        lastName,
        hairColor
    }
    
    console.log(JSON.stringify(person));
    
}


solve('George', 'Jones', 'Brown')
// {"name":"George","lastName":"Jones","hairColor":"Brown"}



solve('Peter', 'Smith', 'Blond')
// {"name":"Peter","lastName":"Smith","hairColor":"Blond"}
