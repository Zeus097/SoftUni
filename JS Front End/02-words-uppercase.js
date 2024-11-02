function solve(currentString) {
    
    const words = currentString.match(/\b\w+\b/g);

    const upperCaseWords = words.map(word => word.toUpperCase()).join(', ')

    console.log(upperCaseWords)
}


solve('Hi, how are you?') // HI, HOW, ARE, YOU
solve('hello') // HELLO
