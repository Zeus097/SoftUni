function solve() {
    
    const inputText = document.querySelector('#text').value.toLowerCase().split(' ');
    const namingConvention = document.querySelector('#naming-convention').value.toLowerCase().trim();
    
    console.log(inputText);
    

    const resultEl = document.querySelector('#result');

    switch (namingConvention) {
        case 'camel case':
            resultEl.textContent = inputText[0] + inputText.slice(1).map(word => word[0].toUpperCase() + word.slice(1)).join('');
            break;
        case 'pascal case':
            resultEl.textContent = inputText.map(word => word[0].toUpperCase() + word.slice(1)).join('');
            break;
  
        default:
            resultEl.textContent = 'Error!'
            break;
    }

}
