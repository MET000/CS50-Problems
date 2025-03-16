#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>


int main(void)
{
    string key = "ABCDEEF";

    int len_key = strlen(key);
    int i = 0;

    for (int j = 0; j < len_key; j++)
    {
        i = j;
        while (key[i] != '\0')
        {
            if (key[j] == key[i+1])
            {
                printf("ok\n");
                return 1;
            }
            i++;
        }
    }
}

