function solve(array) {
    let newArray = []
    let counter = 0

    while (array.length) {

        let highNum = Math.max(...array)
        let minNum = Math.min(...array)

        if ( counter % 2 != 0 ) {
            newArray.push(highNum)
            let numberToRemove = array.indexOf(highNum)
            array.splice(numberToRemove, 1)
        } else {
            newArray.push(minNum)
            let numberToRemove = array.indexOf(minNum)
            array.splice(numberToRemove, 1)
        }

        counter += 1

    }

    return newArray

}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));
// [-3, 65, 1, 63, 3, 56, 18, 52, 31, 48]
