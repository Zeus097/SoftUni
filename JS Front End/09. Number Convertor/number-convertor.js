function solve() {
    
    const input = Number(document.querySelector('#input').value);
    const conertTo = document.querySelector('#selectMenuTo').value.toLowerCase();
    const resultEl = document.querySelector('#result');

    switch (conertTo) {

        case 'binary':
            resultEl.value = input.toString(2);
            break;
    
        case 'hexadecimal':
            resultEl.value = input.toString(16).toUpperCase();
            break;

    }

}
