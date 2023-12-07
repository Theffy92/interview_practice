const palindrome = (number) => {
    if (!Number.isInteger(number)){
        throw new TypeError('Input must be an integer');
    }
    let numAlt = number;
    let numMod = 0;
    let reverse = '';
    let lenNum = Math.floor(Math.log10(number)) + 1;

    while(lenNum >= 1){
        numMod = numAlt % 10;
        // console.log(numMod);
        reverse += numMod.toString();
        numAlt = Math.floor(numAlt / 10);
        // console.log(numAlt);
        lenNum -= 1
        // console.log(lenNum);
    }
    const intReverse = parseInt(reverse);

    if(intReverse === number){
        return true
    } else {
        return false
    }
}

const result = palindrome(12321);
console.log(result);
const result1 = palindrome(5829);
console.log(result1);