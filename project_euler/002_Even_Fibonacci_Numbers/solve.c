#include <stdio.h>



int main(){
    long long sol = 0;
    int a = 1;
    int b = 2;

    while (a < 4000000) {
        if (a % 2 == 0) {
            sol += a;
        }
        int temp = a;
        a = b;
        b = temp + b;
    } 
    printf("%lld", sol);

    return 0;
}