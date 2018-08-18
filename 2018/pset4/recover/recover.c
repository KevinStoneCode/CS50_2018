#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#define BUFFER_SIZE 512

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: recover infile\n");
        return 1;
    }

    // remember filenames
    char *infile = argv[1];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    unsigned char *buf = malloc(BUFFER_SIZE);
    int counter = -1;
    // open output file
    char *filename = malloc(7);
    FILE *img = NULL;

    while (fread(buf, 1, BUFFER_SIZE, inptr) > 0)
    {
        if (buf[0] == 0xff && buf[1] == 0xd8 && buf[2] == 0xff && (buf[3] & 0xf0) == 0xe0)
        {
            // close img file
            if (img != NULL)
                fclose(img);

            // open new img file
            counter++;
            sprintf(filename, "%03i.jpg", counter);
            img = fopen(filename, "w");
        }

        if (counter >= 0)
        {
            fwrite(buf, 1, BUFFER_SIZE, img);
        }
    }

    free(buf);
    free(filename);

    // close img file
    fclose(img);

    // close infile
    fclose(inptr);
}