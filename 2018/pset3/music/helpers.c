// Helper functions for music
#include <ctype.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    // TODO
    return (fraction[0] - '0') * 8 / (fraction[2] - '0');
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    // TODO
    double n = 0;
    for (int i = 0, j = strlen(note); i < j; i++)
    {
        if (isalpha(note[i]))
        {
            switch (note[i])
            {
                case 'b':
                    n--;
                    break;
                case 'B':
                    n += 2;
                    break;
                case 'C':
                    n -= 9;
                    break;
                case 'D':
                    n -= 7;
                    break;
                case 'E':
                    n -= 5;
                    break;
                case 'F':
                    n -= 4;
                    break;
                case 'G':
                    n -= 2;
                    break;
            }
        }
        else if (note[i] == '#')
        {
            n++;
        }
        else
        {
            n += ((note[i] - '0' - 4) * 12);
        }
    }
    return round(pow(2, n / 12) * 440);
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    // TODO
    if (strcmp(s, "") == 0)
    {
        return true;
    }
    return false;
}
