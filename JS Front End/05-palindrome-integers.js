function solve(array) {

    for (let i = 0; i < array.length; i++) {
        let isPalindrom = false

        const splitNumber = array[i].toString().split('').map(Number).join('')
        const reversedNumber = array[i].toString().split('').reverse().map(Number).join('')

        if (splitNumber === reversedNumber) {
            isPalindrom = true
        }

        console.log(isPalindrom);
        
    }
    
}

solve([123,323,421,121]) // false, true, false, true
solve([32,2,232,1010]) // false, true, true, false
