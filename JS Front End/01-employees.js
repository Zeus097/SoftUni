function solve(input) {
    const newObj = {}

    for (let name of input) {
        newObj[name] = name.length
    }

    let entries = Object.entries(newObj);
    for ( let [ employeeName, personalNum ] of entries ) {
        console.log(`Name: ${employeeName} -- Personal Number: ${personalNum}`);
    }
}


solve([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ])
// Name: Silas Butler -- Personal Number: 12
// Name: Adnaan Buckley -- Personal Number: 14
// Name: Juan Peterson -- Personal Number: 13
// Name: Brendan Villarreal -- Personal Number: 18


console.log('-------------------------------------------------');


solve([
    'Samuel Jackson',
    'Will Smith',
    'Bruce Willis',
    'Tom Holland'
    ])
// Name: Samuel Jackson -- Personal Number: 14
// Name: Will Smith -- Personal Number: 10
// Name: Bruce Willis -- Personal Number: 12
// Name: Tom Holland -- Personal Number: 11
