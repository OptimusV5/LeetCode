/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** generateParenthesis(int n, int* returnSize){
    char ** ret;
    char * ctmp;
    int amount = 1 , m = 2*n , value = 0 , index = 0;
    long long count = 2 , tmp = 0;
    for(int i = 1;i < n;i++){
        amount *= ((m - i + 1)/i);
        count <<= 2;
    }
    printf("%d\n",amount);
    ret = (char **)malloc(sizeof(char)*(amount+2)*(m+1));
    for(int i = 0;i < count;i++){
        if(!(i&1)){
            continue;
        }
        tmp = i;
        ctmp = (char *)malloc(sizeof(char)*(m+1));
        for(int j = 0;j < m;j++){
            if(tmp & 1){
                value++;
                ctmp[m-j-1] = ')';
            }else{
                value--;
                ctmp[m-j-1] = '(';
            }
            tmp >>= 1;
            if(value < 0){
                break;
            }
        }
        ctmp[m] = '\0';
        printf("%s\n",ctmp);
        if(value == 0){
            ctmp[m] = '\0';
            printf("run here\n");
            ret[index++] = ctmp;
        }else{
            free(ctmp);
        }
        value = 0;
    }
    *returnSize = index;
    printf("%d\n",*returnSize);
    return ret;
}
