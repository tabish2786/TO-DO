// #include <stdio.h>

// int main(){
//     float radius;
//     printf("Enter radius\n");
//     scanf("%f", &radius);
//     printf("The area of the circle is %f",3.14*radius*radius);
//     return 0;
// }

#include <stdio.h>

int main(){
    float radius, height;
    printf("Enter radius\n");
    scanf("%f", &radius);
    printf("Enter height\n");
    scanf("%f", &height);
    printf("The area of the circle is %f",3.14*radius*radius*height);
    return 0;
}