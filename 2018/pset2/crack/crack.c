#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <crypt.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }
    // set an array of chars we need
    char chr[52];
    for (int i = 0;i < 52; i++)
    {
        if (i < 26)
        {
            chr[i] = 65 + i;
        }
        else
        {
            chr[i] = 71 + i;
        }
    }
    // set key as a char array and set all values
    char p[6];
    for (int i = 0; i < 6;i++)
    {
        p[i] = '\0';
    }
    // get input ready to check
    string encryptKey = argv[1];
    // salt is the first two characters of hashed password
    char salt[2] = {encryptKey[0], encryptKey[1]};
    // array position and chr index
    int ap0 = 0, ap1 = 0, ap2 = 0, ap3 = 0, ap4 = 0;
    do
    {
        p[0] = chr[ap0];
        ap0++;
        printf("%s,", p);
        if (strcmp(encryptKey, crypt(p , salt)) == 0)
        {
            printf("password: %s\n", p);
            return 0;
        }

        if (ap0 == 52)
        {
            if (ap1 == 52)
            {
                if (ap2 == 52)
                {
                    if (ap3 == 52)
                    {
                        if (ap4 == 52)
                        {
                            return 1;
                        }
                        ap3 = 0;
                        p[4] = chr[ap4];
                        ap4++;
                    }
                    ap2 = 0;
                    p[3] = chr[ap3];
                    ap3++;
                }
                ap1 = 0;
                p[2] = chr[ap2];
                ap2++;
            }
            ap0 = 0;
            p[1] = chr[ap1];
            ap1++;
        }
    }
    while(true);
}