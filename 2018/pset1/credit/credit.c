#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long long n;
    do
    {
        n = get_long_long("Number: ");
    }
    while (n < 0);

    int type = 0;
    if (n >= pow(10, 14) && n < pow(10, 15))
    {
        int am = n / pow(10, 13);
        if (am == 34 || am == 37)
        {
            type = 1;
        }
    }
    else if (n >= pow(10, 12) && n < pow(10, 13))
    {
        int i = n / pow(10, 12);
        if (i == 4)
        {
            type = 2;
        }
    }
    else if (n >= pow(10, 15) && n < pow(10, 16))
    {
        int j = n / pow(10, 14);
        if (j >= 51 && j <= 55)
        {
            type = 3;
        }
        else if (j >= 40 && j <= 49)
        {
            type = 2;
        }
    }

    if (type > 0)
    {
        int sum = 0;
        while (n > 0)
        {
            sum += (n % 10);
            n /= 10;

            int bytwo = (n % 10) * 2;
            if (bytwo >= 10)
            {
                bytwo = (bytwo % 10) + 1;
            }
            sum += bytwo;
            n /= 10;
        }
        if (sum % 10 != 0)
        {
            type = 0;
        }
    }

    switch (type)
    {
        case 0:
            printf("INVALID\n");
            break;
        case 1:
            printf("AMEX\n");
            break;
        case 2:
            printf("VISA\n");
            break;
        case 3:
            printf("MASTERCARD\n");
            break;
    }

}