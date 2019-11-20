bool isPalindrome(int x){
    if(x<0)return false;
    int ret = 0,tmp = x;
    while(tmp>10){
        if(ret > 214748364){
            return 0;
        }
        ret = ret *10 + tmp%10 ;
        tmp /= 10;
    }
    if(tmp==10){
        if(ret > 214748364){
            return 0;
        }
        ret = ret*100 +1;
    }else{
        if(ret > 214748364){
            return 0;
        }
        ret = ret*10 + tmp;
    }
    if(ret == x)return true;
    else return false;
}
