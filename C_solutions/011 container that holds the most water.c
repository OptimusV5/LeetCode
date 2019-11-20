int maxArea(int* height, int heightSize){
//    printf("%d %d ",height[0],heightSize);
    int com = 0,com1 = 0,index = 1;
    if(heightSize == 2){
        return height[0]>height[1]?height[1]:height[0];
    }
    if(height[0] == 0){
        return maxArea(++height,heightSize-1);
    }
    int area = 0;
    for(int i=1;i<heightSize;i++){
        area = height[0]>height[i]?(height[i]*i):(height[0]*i);
        if(area>com){
            com = area;
            index = i;
        }
    }
//    printf("%d\n",com);
    if(index == 1)return com;
    com1 = maxArea(++height,index);
    return com>com1?com:com1;
}
