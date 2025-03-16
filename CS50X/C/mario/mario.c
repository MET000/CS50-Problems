#include <cs50.h>
#include <stdio.h>

void print_row(int n);
void print_space(int n);

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int i = 0; i < height; i++)
    {
        print_space(height - (i + 1));
        print_row(i + 1);
        print_space(2);
        print_row(i + 1);
        printf("\n");
    }
}

void print_row(int n)
{
    for (int i = 0; i < n; i++)
        printf("#");
}

void print_space(int n)
{
    for (int i = 0; i < n; i++)
        printf(" ");
}
