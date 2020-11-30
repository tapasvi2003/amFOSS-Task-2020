#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);
    int arr[n];
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    
    for(int i = 0; i < n; i++)
    {
        for(int j = i+1; j < n; j++)
        {
            if(arr[i]+arr[j] == m)
            {
                printf("True");
                return 0;
            }
        }
    }
    printf("False");
    return 0;
}