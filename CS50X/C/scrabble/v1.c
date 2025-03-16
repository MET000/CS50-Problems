#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int count_score(string s);
string to_uppercase(string s);

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

int count_score(string s)
{
    // 26 is the number of letter of the alphabet.
    int SCORES[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
                      1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    char CHARACTERS[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    string a = to_uppercase(s);
    int counter = 0;
    int i = 0;

    while (a[i] != '\0')
    {
        if (isalpha(a[i]))
        {
            for (int j = 0; CHARACTERS[j] != '\0'; j++)
            {
                if (a[i] == CHARACTERS[j])
                {
                    counter += SCORES[j];
                    break;
                }

                else
                {
                    continue;
                }
            }
        }
        else
        {
            continue;
        }
        i++;
    }
    return counter;
}

string to_uppercase(string s)
{
    int i = 0;
    while (s[i] != '\0')
    {
        if (islower(s[i]))
        {
            s[i] -= 'a' - 'A';
        }
        else if (isupper(s[i]))
        {
            s[i] = s[i];
        }
        else
        {
            s[i] -= s[i];
        }
        i++;
    }
    return s;
}
