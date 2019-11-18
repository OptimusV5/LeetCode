char * intToRoman(int num){
    char * ret;
    int index = 0 , tmp = 0;
    ret = (char *)malloc(sizeof(char)*16);
    tmp = num / 1000;
    for(int i = 0;i < tmp;i++){
        ret[index++] = 'M';
    }
    num = num % 1000;
    tmp = num / 100;
    switch(tmp){
        case 4:
            ret[index++] = 'C';
            ret[index++] = 'D';
            break;
        case 9:
            ret[index++] = 'C';
            ret[index++] = 'M';
            break;
    }
    if(tmp < 4){
        for(int i=0;i<tmp;i++){
            ret[index++] = 'C';
        }
    }else if(tmp > 4 &&tmp < 9){
        ret[index++] = 'D';
        for(int i=0;i<(tmp-5);i++){
            ret[index++] = 'C';
        }
    }
    num %= 100;
    tmp = num / 10;
    switch(tmp){
        case 4:
            ret[index++] = 'X';
            ret[index++] = 'L';
            break;
        case 9:
            ret[index++] = 'X';
            ret[index++] = 'C';
            break;
    }
    if(tmp < 4){
        for(int i=0;i<tmp;i++){
            ret[index++] = 'X';
        }
    }else if(tmp > 4 &&tmp < 9){
        ret[index++] = 'L';
        for(int i=0;i<(tmp-5);i++){
            ret[index++] = 'X';
        }
    }
    tmp = num % 10;
    switch(tmp){
        case 4:
            ret[index++] = 'I';
            ret[index++] = 'V';
            break;
        case 9:
            ret[index++] = 'I';
            ret[index++] = 'X';
            break;
    }
    if(tmp < 4){
        for(int i=0;i<tmp;i++){
            ret[index++] = 'I';
        }
    }else if(tmp > 4 &&tmp < 9){
        ret[index++] = 'V';
        for(int i=0;i<(tmp-5);i++){
            ret[index++] = 'I';
        }
    }
    ret[index++] = '\0';
    return ret;
}
