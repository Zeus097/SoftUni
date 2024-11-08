function solve(a, b) {
    
    let start = a.charCodeAt();
    let end = b.charCodeAt();
    let charsArray = []
    
    if (end > start) {
        for ( let i = start; i < end - 1; i++ ) {
            charsArray.push(String.fromCharCode(i + 1))
        }
    }else {
        for ( let i = end; i < start - 1; i++ ) {
            charsArray.push(String.fromCharCode(i + 1))
        }
    }

    console.log(charsArray.join(' '));
    
}

solve('a', 'd') // b c
solve('#', ':') // $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9
solve('C', '#') // $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
