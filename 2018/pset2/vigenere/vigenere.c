#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string k = argv[1];
        int keylen = strlen(k);
        for (int i = 0; i < keylen; i++)
        {
            if (!isalpha(k[i]))
            {
                printf("has non-alphabetical character\n");
                return 1;
            }
            else
            {
                k[i] = toupper(k[i]);
            }
        }

        string ptext = get_string("plaintext:  ");
        printf("ciphertext: ");
        for (int i = 0, j = 0, n = strlen(ptext); i < n; i++)
        {
            if (isalpha(ptext[i]))
            {
                int m = k[j] - 'A';
                if (isupper(ptext[i]))
                {
                    printf("%c", (ptext[i] + m > 90 ? ptext[i] + m - 26 : ptext[i] + m));
                }
                else
                {
                    printf("%c", (ptext[i] + m > 122 ? ptext[i] + m - 26 : ptext[i] + m));
                }
                j++;
                if (j == keylen)
                {
                    j = 0;
                }
            }
            else
            {
                printf("%c", ptext[i]);
            }
        }
        printf("\n");
    }
    else
    {
        printf("Usage: ./vigenere k\n");
        return 1;
    }
}