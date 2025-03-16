#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>

int index_calculator(string s);
void counter(string s, int array[]);

int main(void)
{
    string input = get_string("Input: ");
    int index = index_calculator(input);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int index_calculator(string s)
{
    int a[] = {0, 1, 0};
    counter(s, a);
    int letters = a[0];
    int words = a[1];
    int sentences = a[2];

    double L = (letters * 100.0) / words;
    double S = (sentences * 100.0) / words;
    double index = 0.0588 * L - 0.296 * S - 15.8;
    return round(index);
}

void counter(string s, int array[])
{
    int i = 0;
    while (s[i] != '\0')
    {
        if (isalpha(s[i]))
        {
            array[0]++;
        }
        else if (isspace(s[i]))
        {
            array[1]++;
        }
        else if (s[i] == 46 || s[i] == 63 || s[i] == 33)
        {
            array[2]++;
        }

        i++;
    }
}
