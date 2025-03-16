#include <cs50.h>
#include <stdio.h>

int check_sum(long n);
int add_digits(long number, long divisor, bool multiply_by_two);
int check_len(long n);
int check_first_digits(long n);

int main(void)
{
    long input = get_long("Number: ");
    int validity_identifier = check_sum(input);
    int number_of_digits = check_len(input);
    int first_digits = check_first_digits(input);

    if ((number_of_digits == 15) && (first_digits == 34 || first_digits == 37) &&
        (validity_identifier == 0))
    {
        printf("AMEX\n");
    }
    else if ((number_of_digits == 16) &&
             (first_digits == 51 || first_digits == 52 || first_digits == 53 ||
              first_digits == 54 || first_digits == 55) &&
             (validity_identifier == 0))
    {
        printf("MASTERCARD\n");
    }
    else if ((number_of_digits == 13 || number_of_digits == 16) && (first_digits / 10 == 4) &&
             (validity_identifier == 0))
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
    int sum1 = add_digits(n, 10, true); // Calculate sum * 2 of every other digit, starting with the
                                        // number’s second-to-last digit.
    int sum2 = add_digits(n, 1, false); // Calculate sum of other digits.
    int last_digit = (sum1 + sum2) % 10; // Catch the last digit of sum1 + sum2.
    return last_digit;
}

int add_digits(long number, long divisor, bool multiply_by_two)
{
    int sum = 0;
    int multiplicator = 100;
    int target;

    do
    {
        target = (number / divisor) % 10;
        if (((target * 2) < 10) && multiply_by_two)
        {
            sum += target * 2;
        }
        else if (((target * 2) >= 10) && multiply_by_two) // If the target * 2 is higher than 9 we
                                                          // then add the digits of the target.
        {
            sum += ((target * 2) / 10) + ((target * 2) % 10);
        }
        else // Concerns digits that should not to be mulplied by 2 (multiply_by_two = false).
        {
            sum += target;
        }
        divisor *= multiplicator;
    }
    while ((number / divisor) > 0);
    return sum;
}

int check_len(long n)
{
    long divisor = 1;
    int number_of_digits = 0;
    long marker; // Create a marker to stop the loop when number_of_digits equals actual
                 // number of digits.
    do
    {
        marker = n / divisor;
        divisor *= 10;
        number_of_digits++;
    }
    while (marker > 10);
    return number_of_digits;
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
