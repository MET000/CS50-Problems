#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int count_score(string a);

int main(void)
{
    string player_1 = get_string("Player 1: ");
    string player_2 = get_string("Player 2: ");
    int score_1 = count_score(player_1);
    int score_2 = count_score(player_2);

    if (score_1 > score_2)
    {
        printf("Player 1 wins!\n");
    }
    else if ((score_1 < score_2))
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int count_score(string a)
{
    int SCORES[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int counter = 0;

    for (int i = 0; a[i] != '\0'; i++)
    {
        if (isupper(a[i]))
        {
            int position = a[i] - 'A';
            counter += SCORES[position];
        }
        else if (islower(a[i]))
        {
            int position = (a[i] - 'a');
            counter += SCORES[position];
        }
        else
        {
            continue;
        }
    }
    return counter;
}
