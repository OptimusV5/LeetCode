char * convert(char * s, int numRows){
    int x=0,y=0,acount=strlen(s);
    if(acount==0)return "";
    if(numRows==1)return s;
    int index[numRows];
    char line[numRows][acount];
    char * ret = malloc(sizeof(char)*(acount+1));
    int down=1,right=2,go=0;
    for(int i=0;i<numRows;i++){
        index[i]=0;
    }
    for(int i=0;i<acount;i++){
        line[y][index[y]++] = s[i];
        if(y==(numRows-1)){
            go = right;
        }
        if(y==0){
            go = down;
        }
        if(go == right){
            x++;
            y--;
        }else{
            y++;
        }
    }
    int k=0;
    for(int i=0;i<numRows;i++){
        for(int j=0;j<index[i];j++){
          //  printf("%c",line[i][j]);
            ret[k++] = line[i][j];
        }
    }
    ret[k]='\0';
    return ret;
}
