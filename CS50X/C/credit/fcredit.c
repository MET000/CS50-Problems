#include <cs50.h>
#include <stdio.h>

int check_sum(long n);
int add_other_digits(long n);
int check_len(long n);
int check_first_digits(long n);

int main(void)
{
    long input = get_long("Number: ");
    int validity_identifier = check_sum(input);
    int len = check_len(input);
    int first_digits = check_first_digits(input);

    if ((len == 15) && (first_digits == 34 || first_digits == 37) && (validity_identifier == 0))
    {
        printf("AMEX\n");
    }
    else if ((len == 16) &&
             (first_digits == 51 || first_digits == 52 || first_digits == 53 ||
              first_digits == 54 || first_digits == 55) &&
             (validity_identifier == 0))
    {
        printf("MASTERCARD\n");
    }
    else if ((len == 13 || len == 16) && (first_digits / 10 == 4) && (validity_identifier == 0))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

int check_sum(long n)
{
    int sum = 0;
    long divisor = 10;
    do
    {
        int target = (n / divisor) % 10;
        if ((target * 2) < 10)
        {
            sum += target * 2;
        }
        else
        {
            sum += ((target * 2) / 10) + ((target * 2) % 10);
        }
        divisor *= 100;
    }
    while ((n / divisor) > 0);

    sum += add_other_digits(n);
    return sum % 10;
}

int add_other_digits(long n)
{
    long divisor = 1;
    int multiplicator = 100;

    int sum = 0;
    do
    {
        int target = (n / divisor) % 10;
        sum += target;
        divisor *= multiplicator;
    }
    while ((n / divisor) > 0);

    return sum;
}

int check_len(long n)
{
    long divisor = 1;
    int len = 0;
    long marker;
    do
    {
        marker = n / divisor;
        divisor *= 10;
        len += 1;
    }
    while (marker > 10);
    return len;
}

int check_first_digits(long n)
{
    long divisor = 1;
    long first_digits;
    do
    {
        first_digits = n / divisor;
        divisor *= 10;
    }
    while (first_digits > 100);
    return first_digits;
}
