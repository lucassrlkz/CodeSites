function adjacentElementsProduct($inputArray) {
    $max = $inputArray[0]* $inputArray[1];
    for($x = 1; $x <= sizeof($inputArray)-1; $x++){
        $max = max($max, ($inputArray[$x]* $inputArray[$x+1]));
    }
    return $max;
}
