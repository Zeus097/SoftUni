function passwordValidation(password) {
    
    const PLength = new RegExp(/^.{6,10}$/);
    const PLettersAndDigits = new RegExp(/^[a-zA-Z0-9]+$/);
    const PAtleastTwoDigits = new RegExp(/^(.*\d.*\d.*)$/);

    const validPLength = PLength.test(password);
    const validPLettersAndDigits = PLettersAndDigits.test(password);
    const validPAtleastTwoDigits = PAtleastTwoDigits.test(password);

    if (validPLength && validPLettersAndDigits && validPAtleastTwoDigits) {
        console.log("Password is valid")
    }else {
        if (! validPLength) console.log("Password must be between 6 and 10 characters")
        if (!validPLettersAndDigits) console.log("Password must consist only of letters and digits");
        if (! validPAtleastTwoDigits) console.log("Password must have at least 2 digits");
        
    }

}

passwordValidation('logIn')
// Password must be between 6 and 10 characters, Password must have at least 2 digits

passwordValidation('MyPass123')
// Password is valid

passwordValidation('Pa$s$s')
// Password must consist only of letters and digits, Password must have at least 2 digits
