// #include <stdio.h>

// int main(){
//     float a;
//     printf("Enter the number to check divisiblity by 97\n");
//     scanf("%f", &a);
//     printf("The remainder of a dividing by 97 is %f",(a/97.0));
//     return 0;
// }

#include <stdio.h>

int main() {
    int a;
    printf("Enter the number to check divisibility by 97\n");
    scanf("%d", &a);
    printf("The remainder of a dividing by 97 is %d", a % 97);
    return 0;
}
