#include <stdio.h>

int main(){
    float c;
    printf("Enter temperature in celcius\n");
    scanf("%f", &c);
    printf("The temperature in farenheit is %f",(c*(9.0/5.0))+32);
    return 0;
}