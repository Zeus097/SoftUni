function solve(array) {
    let username = array[0]
    
    for (let i = 1; i < array.length; i++) {
        
        let reversedWord = array[i].split('').reverse().join('')

        if (username != reversedWord) {

            if ( i % 4 == 0 ) {
                console.log(`User ${username} blocked!`);
                break
            }else {console.log('Incorrect password. Try again.')}

        }else {console.log(`User ${username} logged in.`);}
    }

}

solve(['Acer','login','go','let me in','recA'])
// Incorrect password. Try again., Incorrect password. Try again., Incorrect password. Try again., User Acer logged in.


solve(['momo','omom'])
// User momo logged in.


solve(['sunny','rainy','cloudy','sunny','not sunny'])
// Incorrect password. Try again., Incorrect password. Try again., Incorrect password. Try again., User sunny blocked!
