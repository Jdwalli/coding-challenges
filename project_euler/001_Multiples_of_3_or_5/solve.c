#include <stdio.h>

int main(){
    int i;
    int solution = 0;

    for (i = 0; i < 1000; i++){
        if ((i % 3 == 0) || (i % 5 == 0)) {
            solution += i;
        }
    }

    printf("%d", solution);

    return 0;
}