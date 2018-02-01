bool checkPalindrome(char * inputString) {
    
    int len = strlen(inputString);
    bool flag;
        for(int i=0 ; i <= len ; i++){
            if(inputString[i] != inputString[len-1-i]){
                flag = false;
                break;
            }
            else{
                 flag = true;
            }
    }
    
    return flag;
   
}
