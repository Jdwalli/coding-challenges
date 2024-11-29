#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int count_divisors(int n)
{
    long triangular_number = calculate_triangular_number(n);
    int divisors = 0;

    for (int i = 1; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            divisors++;
            if (i != n / i)
            {
                divisors++;
            }
        }
    }

    return divisors;
}

int calculate_triangular_number(int n)
{
    return (n * (n + 1)) / 2;
}

int main()
{
    int i = 1;
    int triangle = 0;

    while (1)
    {
        triangle = calculate_triangular_number(i);
        int divisors = count_divisors(triangle);

        if (divisors > 500)
        {
            printf("%d\n", triangle);
            break;
        }
        i++;
    }

    return 0;
}