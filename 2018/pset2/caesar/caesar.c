#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        int key = atoi(argv[1]) % 26;
        if (key >= 0)
        {
            string ptext = get_string("plaintext:  ");
            printf("ciphertext: ");

            for (int i = 0, n = strlen(ptext); i < n; i++)
            {
                if (isalpha(ptext[i]))
                {
                    if (isupper(ptext[i]))
                    {
                        printf("%c", (ptext[i] + key > 90 ? ptext[i] + key - 26 : ptext[i] + key));
                    }
                    else
                    {
                        printf("%c", (ptext[i] + key > 122 ? ptext[i] + key - 26 : ptext[i] + key));
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
            printf("Key must be a non-negative integer.\n");
        }
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}