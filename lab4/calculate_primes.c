#include "calculate_primes.h"

void calculate_primes(int primes[], int n){

    for (int i=2; i <= n; i++){
        primes[i] = 1;
    }

    for(int i = 2; i<= n;){
        for(int j = 2; j<=(n/i); j++){
            primes[i*j] = 0;
        }
        if (i+1>=n){
            break;
        }
        for (int k=i+1;k<=n;k++){
            i = k;
            if (primes[k]==1){
                break;
            }
        }
    }
}