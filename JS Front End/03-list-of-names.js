function solve(array) {
    array
        .sort((a, b) => a.localeCompare(b))
        .forEach(function(element, index) {
            console.log(`${ index + 1 }.${element}`);
            
        })
    


    // 80 / 100 in JUDGE
    // array.sort();
    // for ( let i = 0;i < array.length; i++  ) {
    //     console.log(`${ i + 1 }.${array[i]}`)
    // }


    // 80 / 100 in JUDGE
    // array.sort();
    // array.forEach( (name, index) => {
    //     console.log(`${ index + 1 }.${name}`)
    // });
    
}

solve(["John", "Bob", "Christina", "Ema"]) // 1.Bob, 2.Christina, 3.Ema, 4.John
