function solve(myArray) {
    let evenSum = 0
    let oddSum = 0

    for (let i = 0; i < myArray.length; i++) {
        if (myArray[i] % 2 === 0) {
            evenSum += myArray[i]
        }else {
            oddSum += myArray[i]
        }
    }

    console.log(evenSum - oddSum);
    
}


solve([1,2,3,4,5,6]) // 3
solve([3,5,7,9]) // -24
solve([2,4,6,8,10]) // 30
