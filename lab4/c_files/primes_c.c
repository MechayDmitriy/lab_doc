/**
 * primes.c -- программа для вывода простых чисел в диапазоне от 1 до n
 *
 * Copyright (c) 2022, Mechai Dmitriy <mechai@cs.petrsu.ru>
 *
 * This code is licensed under MIT license.
 */

#include <stdio.h>
#include <stdlib.h>
#include "calculate_primes.h"

  
int main(){
    int max_n;

    printf("Введите верхнюю границу N: ");
    scanf("%d", &max_n);

    
    int *primes = (int *)malloc((max_n+1)*sizeof(int));

    if (primes == NULL){
        perror("maloc error");
        return EXIT_FAILURE;
    }

    calculate_primes(primes, max_n);
 
    for (int i=2; i<=max_n; i++){
        if (primes[i]==1){
            printf("%d ",i);
        }
    }
    printf("\n");
    free(primes);

}