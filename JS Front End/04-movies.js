function solve(array) {
    let movies = [];
    
    while (array.length != 0) {

        let movieInfo = array[0];

        if (movieInfo.startsWith('addMovie')) {
            
            let name = movieInfo.replace("addMovie ", "");
            movies.push({name})

        }else if (movieInfo.includes('directedBy')) {

            let [name, director] = movieInfo.split(' directedBy ');
            let result = movies.find(movie => movie.name === name);
            if (result) {
                result.director = director;
            }

        }else if (movieInfo.includes('onDate')) {

            let [name, date] = movieInfo.split(' onDate ');
            let result = movies.find(movie => movie.name === name);
            if (result) {
                result.date = date;
            }

        }

        array.shift()

    }
    
    for (info of movies) {
        if (info.name && info.director && info.date) {
            console.log(JSON.stringify(info));
        }
    }

}


solve([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
    ])
// {"name":"Fast and Furious","date":"30.07.2018","director":"Rob Cohen"}
// {"name":"Godfather","director":"Francis Ford Coppola","date":"29.07.2018"}


console.log('----------------------------');


solve([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
    ])
// {"name":"The Avengers","director":"Anthony Russo","date":"30.07.2010"}
