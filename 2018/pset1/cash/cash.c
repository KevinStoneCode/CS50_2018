#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float change;
    do
    {
        change = get_float("Change owed: ");
    }
    while (change < 0);

    change = round(change * 100);
    int cents = (int) change;
    int coins = 0;

    coins = coins + (cents / 25);
    cents = cents % 25;
    coins = coins + (cents / 10);
    cents = cents % 10;
    coins = coins + (cents / 5);
    cents = cents % 5;
    coins = coins + cents;

    printf("%i", coins);
    printf("\n");
}