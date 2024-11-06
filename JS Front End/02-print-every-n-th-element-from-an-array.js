function solve(arrayOfStrings, step) {
    
    let newArray = []
    for ( i = 0; i < arrayOfStrings.length; i += step )
        newArray.push(arrayOfStrings[i])

    return newArray

}

console.log( solve(['5', '20', '31', '4', '20'], 2) );  // ['5', '31', '20']
console.log( solve(['dsa', 'asd', 'test', 'tset'], 2) );  // ['dsa', 'test']
console.log( solve(['1', '2','3', '4', '5'], 6) );  // ['1']
