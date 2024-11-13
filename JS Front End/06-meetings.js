function solve(strings) {
    
    addressBook = {};

    for (let line of strings) {
        let tokens = line.split(' ');
        personName = tokens[1];
        weekday = tokens[0];

        if ( addressBook.hasOwnProperty(weekday) ) {
            console.log(`Conflict on ${weekday}!`);
        } else{
            addressBook[weekday] = personName
            console.log(`Scheduled for ${weekday}`);
        }
    }

    let output = Object.entries(addressBook)

        for (let [key, value] of output) {
            console.log(`${key} -> ${value}`)
        }

}


solve([
    'Monday Peter',
    'Wednesday Bill',
    'Monday Tim',
    'Friday Tim'
])
// Scheduled for Monday
// Scheduled for Wednesday
// Conflict on Monday!
// Scheduled for Friday
// Monday -> Peter
// Wednesday -> Bill
// Friday -> Tim

console.log('------------------------');

solve([
    'Friday Bob',
    'Saturday Ted',
    'Monday Bill',
    'Monday John',
    'Wednesday George'
])
// Scheduled for Friday
// Scheduled for Saturday
// Scheduled for Monday
// Conflict on Monday!
// Scheduled for Wednesday
// Friday -> Bob
// Saturday -> Ted
// Monday -> Bill
// Wednesday -> George
