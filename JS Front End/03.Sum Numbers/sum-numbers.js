function calc() {
    const num1Element = document.querySelector('#num1');
    const num2Element = document.querySelector('#num2');
    const sumElement = document.querySelector('#sum');

    // console.log(num1Element.value);
    
    sumElement.value = Number(num1Element.value) + Number(num2Element.value);

}