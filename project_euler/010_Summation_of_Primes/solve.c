#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

long long sieve(int n)
{

    bool *primes = (bool *)malloc((n + 1) * sizeof(bool));

    for (int i = 0; i <= n; i++)
    {
        primes[i] = true;
    }

    primes[0] = false;
    primes[1] = false;

    for (int i = 2; i * i <= n; i++)
    {
        if (primes[i])
        {
            for (int j = i * i; j <= n; j += i)
            {
                primes[j] = false;
            }
        }
    }

    long long sum = 0;
    for (int i = 2; i <= n; i++)
    {
        if (primes[i])
        {
            sum += i;
        }
    }

    free(primes);

    return sum;

}

int main()
{
    long long n = 2000000 - 1;
    long long sum = sieve(n);
    printf("%lld\n", sum);
    return 0;
}