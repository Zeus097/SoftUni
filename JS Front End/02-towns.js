function solve(array) {
    
    const cityObj = {};
    const resultArray = array.map(text => text.split('|').map(part => part.trim()));

    for (let city of resultArray) {
        cityObj.town = city[0]
        cityObj.latitude = parseFloat(city[1], 10).toFixed(2)
        cityObj.longitude = parseFloat(city[2], 10).toFixed(2)
    
        console.log(cityObj);

    }    

}


solve([
    'Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625'
])
// { town: 'Sofia', latitude: '42.70', longitude: '23.33' }
// { town: 'Beijing', latitude: '39.91', longitude: '116.36' }


console.log('----------------------------');


solve(['Plovdiv | 136.45 | 812.575'])
// { town: 'Plovdiv', latitude: '136.45', longitude: '812.58' }
