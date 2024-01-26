// def leapyears(start_year, end_year):
//     leap_years = []
    
//     for year in range(start_year, end_year + 1):
//         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
//             leap_years.append(year)
        
//     return leap_years

// print(leapyears(2000, 2024))

const leapYears =(startYear, endYear)=>{
    const leapYearsArr=[];
    
    for(let year = startYear; year <= endYear; year++){
        if((year % 4 === 0 && year % 100 != 0) || year % 4 ===0){
            leapYears.push(year);
        }
        return leapYearsArr;
    }
}