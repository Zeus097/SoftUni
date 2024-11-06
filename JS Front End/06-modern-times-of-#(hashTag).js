function solve(string) {
    let regexp = /#[A-Za-z]+/g;
    let matches = string.match(regexp)

    for (let match of matches) {
        console.log(match.slice(1));
        
    }
    
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia')
 //special, socialMedia
 
 
solve('The symbol # is known #variously in English-speaking #regions as the #number sign')
 // variously, regions, number

