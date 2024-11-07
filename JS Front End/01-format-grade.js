function solve(grade) {
    if (grade < 3) {
        console.log(`Fail (2)`);
    }else if (grade >= 3 && grade < 3.50) {
        console.log(`Poor (${grade.toFixed(2)})`); 
    }else if (grade >= 3.50 && grade < 4.50) {
        console.log(`Good (${grade.toFixed(2)})`); 
    }else if (grade >= 4.50 && grade < 5.50) {
        console.log(`Very good (${grade.toFixed(2)})`); 
    }else {
        console.log(`Excellent (${grade.toFixed(2)})`);
    }
}

solve(3.33) // Poor (3.33)
solve(4.50) // Very good (4.50)
solve(2.99) // Fail (2)
