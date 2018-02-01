function adjacentElementsProduct(inputArray) {
    var n = inputArray[0] * inputArray[1];

    for(var i = 0; i <inputArray.length; i++){
        n = inputArray[i] * inputArray[i+1] >= n ? inputArray[i] * inputArray[i+1] : n;
    }
    return n;
}