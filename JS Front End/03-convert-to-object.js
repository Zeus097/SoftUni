function convertObject(data) {
    
    let person = JSON.parse(data)
    person = Object.entries(person)

    for (let [key, value] of person) {
        console.log(`${key}: ${value}`);
    }
    
}


convertObject('{"name": "George", "age": 40, "town": "Sofia"}')
// name: George, age: 40, town: Sofia

convertObject('{"name": "Peter", "age": 35, "town": "Plovdiv"}')
// name: Peter, age: 35, town: Plovdiv
