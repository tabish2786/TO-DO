#include <stdio.h>

int main(){
    // Explain step by step evaluation of 3*x/y – z+k, where x=2, y=3, z=3, k=1
    // (3 * 2)/3-3+1
    // 6/3 - 3 + 1 
    // 2 - 3 + 1 
    // 0
    int x=2, y=3, z=3, k=1;
    float w = 3*x/y - z+k;
    printf("%f",w);
    return 0;
}