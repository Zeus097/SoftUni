function solve(x1, y1, x2, y2) {
    
    function isValid(a1, b1, a2, b2) {
        return Number.isInteger( Math.sqrt((a2 - a1)** 2 + (b2-b1)**2) );
    }

    // {x1, y1} to {0, 0}
    console.log(`{${x1}, ${y1}} to {0, 0} is ${ isValid(x1, y1, 0, 0) ? 'valid' : 'invalid' }`)

    // {x2, y2} to {0, 0}
    console.log(`{${x2}, ${y2}} to {0, 0} is ${ isValid(x2, y2, 0, 0) ? 'valid' : 'invalid' }`)

    // {x1, y1} to {x2, y2}
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${ isValid(x1, y1, x2, y2) ? 'valid' : 'invalid' }`)
    
}


solve(3, 0, 0, 4) // {3, 0} to {0, 0} is valid, {0, 4} to {0, 0} is valid, {3, 0} to {0, 4} is valid
solve(2, 1, 1, 1) // {2, 1} to {0, 0} is invalid, {1, 1} to {0, 0} is invalid, {2, 1} to {1, 1} is valid
