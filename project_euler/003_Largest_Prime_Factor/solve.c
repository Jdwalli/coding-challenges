#include <stdlib.h>
#include <stdio.h>

long long max_factor(long long n) {
    long long max = 0;
    int i = 2;

    while (i * i <= n) {
        if (n % i == 0) {
            max = i;
            n /= i;
        } else {
            i++;
        }
    }
    if (n > 1) {
        max = n;
    }
    return max;



}


int main() {
    long long n = 600851475143;
    printf("%lld\n", max_factor(n));
    return 0;

}