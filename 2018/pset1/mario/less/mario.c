#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 0 || n > 23);

    for (int i = 0 ; i < n; i++)
    {
        int j;
        for (j = 0; j < n - i - 1; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < n - j + 1; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}