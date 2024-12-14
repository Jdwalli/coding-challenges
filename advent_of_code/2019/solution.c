#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void additional_fuel_counter(unsigned long *score, int mass){
    unsigned long score_ptr = score;

    while (mass > 0) {
        mass = (mass / 3) - 2; 
        if (mass > 0) {        
            *score += mass;
        }
    }



}



int main(){
    FILE *file = fopen("input.txt", "r");

    int mass = 0;
    unsigned long score = 0;

    while (fscanf(file, "%d", &mass) == 1) {
        
        
        // Part One Solve
        // score += (round(mass / 3) - 2);

        // Part Two Solve
        additional_fuel_counter(&score, mass);

    }

    fclose(file);

    printf("%ld\n", score);

    return 0;
}