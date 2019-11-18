int reverse(int x){
    int ret = 0,tmp = x;
    int minus = 0;
    if(x<0){
        if(tmp <= -2147483648)return 0;
        minus = 1;
        tmp = -tmp;
    }
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
    if(minus){
        ret = -ret;
    }
    return ret;
}
