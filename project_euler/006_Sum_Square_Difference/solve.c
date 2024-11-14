#include <stdio.h>

int main()
{
    int sum_of_squares = 0;
    int square_of_sum = 0;
    int i;

    for (i = 0; i < 101; i++)
    {
        sum_of_squares += i * i;
        square_of_sum += i;
    }

    printf("%d", (square_of_sum * square_of_sum) - sum_of_squares);

    return 0;
}