#include <stdio.h>

int main(){
    float p, r, n;
    printf("Enter principle\n");
    scanf("%f", &p);
    printf("Enter Rate of interest\n");
    scanf("%f", &r);
    printf("Enter Number of years\n");
    scanf("%f", &n);
    printf("The simple interest would be %f",(p*r*n)/100.0);
    return 0;
}