// #include <stdio.h> HARDCORE INPUTS

// int main(){
//     int l = 5;
//     int b = 10;
//     printf("The area of rectangle is %d"l*b)
//     return 0;
// }

#include <stdio.h> //INPUT FROM USER

int main(){
    int lenght,breadth;
    
    printf("Enter lenght\n");
    scanf("%d", &lenght);

    printf("Enter breadth\n");
    scanf("%d", &breadth);

    printf("The are of rectangle is %d",lenght*breadth);
    return 0;
}