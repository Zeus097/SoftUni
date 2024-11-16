function solve(array) {
    
    let searchedWords = array.shift().split(' ');
    let arrayOfWords = [];
    
    for ( word of searchedWords ) {
        
        let wordsObj = {};
        wordsObj.name = word;
        wordsObj.count = 0;
        arrayOfWords.push(wordsObj);

    }
    
    while ( array.length != 0 ) {
        
        let searchedWord = array[0];
        let result = arrayOfWords.find( word => word.name === searchedWord );
            if ( result ) { result.count += 1 } 
        
        array.shift();

    }
    
    arrayOfWords.sort((a, b) => b.count - a.count);
    for (word of arrayOfWords ) {
        console.log(`${word.name} - ${word.count}`);
    }

}


solve([
    'this sentence', 
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
])
// this - 3, sentence - 2


console.log('---------------');


solve([
    'is the', 
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence'
])
// the – 3, is - 1
