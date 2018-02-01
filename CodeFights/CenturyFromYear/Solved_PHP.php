function centuryFromYear($year) {
    
    if($year % 100 == 0){
        return Floor(($year / 100));
    }else{
        return Floor((($year / 100)+1));
    }
}
