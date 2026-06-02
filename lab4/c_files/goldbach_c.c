/**
 * goldbach.c -- программа для проверки гипотезы Гольдбаха
 *
 * Copyright (c) 2022, Mechai Dmitriy <mechai@cs.petrsu.ru>
 *
 * This code is licensed under MIT license.
 */

#include <stdio.h>
#include <stdlib.h>
#include "calculate_primes.h"


int main(){

    int n,m;
    
    printf("Введите верхнюю и нижнюю границу n и m через пробел: ");
    scanf("%d %d", &n, &m);

    int *primes = (int *)malloc((m+1)*sizeof(int));

    if (primes == NULL){
        perror("maloc failed");
        return EXIT_FAILURE;
    }

    calculate_primes(primes, m);

    for (int k=n; k<=m; k+=2){
	int counter=0;
	int x=-1,y;
	for (int i=2; i<=k/2; i++){
	    if (primes[i]==1 && primes[k-i]==1){
                if (x==-1){
                    x = i;
                    y = k-i;    
                }
                counter++;
            }
	}
        printf("%d %d %d %d\n",k,counter,x,y);
    }
    free(primes);
}
