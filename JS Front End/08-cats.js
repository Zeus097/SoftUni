function solve(array) {

    let cats = []

    class Cat {
        
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }

    }

    for (let i = 0; i < array.length; i++) {
        let catData = array[i].split(' ');
        let name, age;
        [name, age] = [catData[0], catData[1]];
        cats.push(new Cat(name, age));
    }

    for (let currentCat of cats) {
        currentCat.meow()
    }

}


solve(['Mellow 2', 'Tom 5'])
// Mellow, age 2 says Meow
// Tom, age 5 says Meow

console.log('---------------------');

solve(['Candy 1', 'Poppy 3', 'Nyx 2'])
// Candy, age 1 says Meow
// Poppy, age 3 says Meow
// Nyx, age 2 says Meow
