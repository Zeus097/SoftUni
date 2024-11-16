function solve(array) {

    let heroes = [];
    while (array.length != 0) {

        let hero = {}
        let currentHero = array[0].split(' / ');
        let [heroName, heroLevel, ...heroItems] = currentHero;
        hero.name = heroName;
        hero.level = parseInt(heroLevel, 10);
        hero.items = heroItems.join(', ')
        heroes.push(hero)
        
        array.shift()

    }

    heroes.sort((a, b) => a.level - b.level);
    for (currentHero of heroes) {
        console.log(`Hero: ${currentHero.name}\nlevel => ${currentHero.level}\nitems => ${currentHero.items}`);
    }
    
}


solve([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ])
// Hero: Hes
// level => 1
// items => Desolator, Sentinel, Antara
// Hero: Derek
// level => 12
// items => BarrelVest, DestructionSword
// Hero: Isacc
// level => 25
// items => Apple, GravityGun


console.log('--------------');


solve([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
    ])
// Hero: Batman
// level => 2
// items => Banana, Gun
// Hero: Superman
// level => 18
// items => Sword
// Hero: Poppy
// level => 28
// items => Sentinel, Antara
