#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool is_prime(int n)
{
    if (n <= 1)
    {
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int count = 0;
    int prime = 2;

    while (count < 10001)
    {
        if (is_prime(prime))
        {
            count += 1;
        }
        prime++;
    }
    printf("The 10001th prime number is: %d\n", prime - 1);
}