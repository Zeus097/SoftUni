function solve(string) {
    const arrayWithWords = string.toLowerCase().split(' ');
    const allWords = []

    while ( arrayWithWords.length != 0 ) {
        
        let currentWord = arrayWithWords[0]
        let wordObject = {}
        let result = allWords.find( word => word.name === currentWord );
        if ( result ) {
            result.count += 1;
        }else { 
            wordObject.name = currentWord;
            wordObject.count = 1;
            allWords.push(wordObject)
        }

        arrayWithWords.shift()

    }

    let result = []
    for ( word of allWords ) {
        if ( word.count % 2 != 0 ) { result.push(word.name); }
    }

    console.log(result.join(' '));
    
}


solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#') // c# php 1 5


console.log('------------');


solve('Cake IS SWEET is Soft CAKE sweet Food') // soft food
