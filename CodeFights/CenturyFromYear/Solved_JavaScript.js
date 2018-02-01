function centuryFromYear(year) {
    var y = Math.floor(year / 100);
    return(year % 100 === 0 ) ? y : ++y;
}
