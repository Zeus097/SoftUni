function solve(myArray, rotationsNumber) {
    let currentArr;
    for (let i = 0; i < rotationsNumber; i++) {

        currentArr = myArray.shift()
        myArray.push(currentArr)
        

    }

    console.log(myArray.join(' '));
    
}

solve([51, 47, 32, 61, 21], 2) // 32 61 21 51 47
solve([32, 21, 61, 1], 4) // 32 21 61 1
solve([2, 4, 15, 31], 5) // 4 15 31 2
