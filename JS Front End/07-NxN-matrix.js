function matrix(num) {
    
    const result = ((num + ' ').repeat(num) + '\n').repeat(num)
    console.log(result);
    
}

matrix(3)
// 3 3 3
// 3 3 3
// 3 3 3

matrix(7)
// 7 7 7 7 7 7 7
// 7 7 7 7 7 7 7
// 7 7 7 7 7 7 7
// 7 7 7 7 7 7 7
// 7 7 7 7 7 7 7
// 7 7 7 7 7 7 7
// 7 7 7 7 7 7 7

matrix(2)
// 2 2
// 2 2
