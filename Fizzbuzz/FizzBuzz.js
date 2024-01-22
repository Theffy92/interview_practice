const fizzBuzz= (num) => {
    const arr = []
    
    if(num % 3 == 0){
        arr.push("Fizz")
    }
    else if(num % 5 == 0){
        arr.push("Buzz")
    }else if(num % 3==0 && num % 5 ==0){
        arr.push("FizzBuzz")
    }
    return arr
}

console.log(fizzBuzz(15))