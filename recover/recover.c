#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int BLOC_SIZE = 512;
int FILENAME_SIZE = 8;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Please provide one forensic image name\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    uint8_t *buffer = malloc(sizeof(uint8_t) * BLOC_SIZE);
    int marker = 0;
    char filename[FILENAME_SIZE];

    while (true)
    {
        if ((fread(buffer, sizeof(uint8_t), BLOC_SIZE, input) == 0) && marker > 0)
        {
            break;
        }

        if ((marker > 0 || marker == 0) && (buffer[0] == 0xff && buffer[1] == 0xd8 &&
                                            buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0))
        {
            sprintf(filename, "%03i.jpg", marker);
            FILE *img = fopen(filename, "a");
            fwrite(buffer, sizeof(uint8_t), BLOC_SIZE, img);
            marker++;
            fclose(img);
        }

        else if (marker > 0 && (buffer[0] != 0xff || buffer[1] != 0xd8 || buffer[2] != 0xff ||
                                (buffer[3] & 0xf0) != 0xe0))
        {
            FILE *img = fopen(filename, "a");
            fwrite(buffer, sizeof(uint8_t), BLOC_SIZE, img);
            fclose(img);
        }
    }

    free(buffer);
    fclose(input);
}
