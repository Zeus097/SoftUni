function solve(num) {
    let percentSymbol = '%', pointSymbol = '.', repeatCount = (100 - num) / 10

    if (num === 100) {
        console.log(`100% Complete!\n[${percentSymbol.repeat(10)}]`);
    }else {
        console.log(`${num}% [${percentSymbol.repeat(num / 10)}${pointSymbol.repeat(repeatCount)}]\nStill loading...`);
    }
}

solve(30)
// 30% [%%%.......]
// Still loading...
console.log('------------------------------------------------------'); // divide inputs for better reading, not part of the topic.


solve(50)
// 50% [%%%%%.....]
// Still loading...
console.log('------------------------------------------------------'); // divide inputs for better reading, not part of the topic.


solve(100)
// 100% Complete!
// [%%%%%%%%%%]
console.log('------------------------------------------------------'); // divide inputs for better reading, not part of the topic.
