// Given a list of numbers, find the mode of the set. 
// Ex: given: [7,3,5,8,3,6,1,3,4,5], mode: 3
// The number 3 occurs three times in this set of integers. This is more than any other integer, so the mode is 3. 
// - Asked about edge cases after

const finMode =(nums)=>{
    let dictNums = {};

    for(const num of nums){
        if(num in dictNums){
            dictNums[num] += 1;
        }else{
            dictNums[num] = 1;
        }
    }

    let maxValue = 0;
    let mode = 0;

    for(const [num, count] of Object.entries(dictNums)){
        if(count > maxValue){
            maxValue = count;
            mode = parseInt(num);
        }
    }

    return mode;
}

console.log(finMode([7,3,5,8,3,6,1,3,4,5]))