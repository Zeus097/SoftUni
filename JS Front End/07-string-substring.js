function solve(word, text) {
    if ( text.toLowerCase().split(' ').includes( word.toLowerCase() ) ) {
        console.log(word);
    } else {
        console.log(`${word} not found!`);
        
    }
}

solve('javascript', 'JavaScript is the best programming language')
// javascript


solve('python', 'JavaScript is the best programming language')
// python not found!
