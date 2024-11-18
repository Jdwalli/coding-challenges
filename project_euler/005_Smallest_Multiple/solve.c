#include <stdio.h>

long long gcd(long long a, long long b){
    while (b != 0){
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main(){
    int n = 20;
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result = result * i / gcd(result, i);
    }
    printf("%lld\n", result);

    return 0;
   
}