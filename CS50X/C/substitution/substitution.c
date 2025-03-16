#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

const int NUMBER_OF_LETTERS = 26;

void encrypt_message(string key, string word);
int key_validation(string key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    int validation = key_validation(argv[1]);

    if (validation == 0)
    {
        string word = get_string("plaintext: ");
        encrypt_message(argv[1], word);
    }
    else if (validation == 1)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else if (validation == 2)
    {
        printf("Key must only contain alphabetic characters.\n");
        return 1;
    }
    else if (validation == 3)
    {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }
}

void encrypt_message(string key, string word)
{
    int len_word = strlen(word);
    printf("ciphertext: ");

    for (int i = 0; i < len_word; i++)
    {
        if (islower(word[i]) && islower(key[word[i] - 'a']))
        {
            printf("%c", key[word[i] - 'a']);
        }
        else if (islower(word[i]) && isupper(key[word[i] - 'a']))
        {
            printf("%c", key[word[i] - 'a'] + ('a' - 'A'));
        }
        else if (isupper(word[i]) && isupper(key[word[i] - 'A']))
        {
            printf("%c", key[word[i] - 'A']);
        }
        else if (isupper(word[i]) && islower(key[word[i] - 'A']))
        {
            printf("%c", key[word[i] - 'A'] - ('a' - 'A'));
        }
        else
        {
            printf("%c", word[i]);
        }
    }
    printf("\n");
}

int key_validation(string key)
{
    int len_key = strlen(key);

    if (len_key != NUMBER_OF_LETTERS)
    {
        return 1;
    }

    for (int i = 0; key[i] != '\0'; i++)
    {
        int j = i;
        if (!isalpha(key[i]))
        {
            return 2;
        }
        else
        {
            while (key[j] != '\0')
            {
                if (key[i] == key[j + 1])
                {
                    return 3;
                }
                j++;
            }
        }
    }
    return 0;
}
