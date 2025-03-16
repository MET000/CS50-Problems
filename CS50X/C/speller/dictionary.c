// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 702;

// Hash table
node *table[N];

// Size of dict
int size_of_dict = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int a = hash(word);

    node *check = table[a];

    while (check != NULL)
    {
        if (strcasecmp(word, check->word) == 0)
        {
            return true;
        }

        check = check->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int pos = -1;
    for (int i = 0; i < 2; i++)
    {
        if (word[i] != '\0')
        {
            pos += pow(26, i) * (toupper(word[i]) - 'A' + 1);
        }
    }

    return pos;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *f = fopen(dictionary, "r");
    if (f == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];

    while (fscanf(f, "%s", buffer) != EOF)
    {
        size_of_dict++;
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }

        // copy the word into the node.
        strcpy(n->word, buffer);

        // Determine where the word should be linked.
        int index = hash(buffer);

        // first element to be linked to the list.
        if (table[index] == NULL)
        {
            n->next = NULL;
            table[index] = n;
            continue;
        }
        n->next = table[index];
        table[index] = n;
    }

    fclose(f);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return size_of_dict;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *next = cursor->next;
            free(cursor);
            cursor = next;
        }
    }

    return true;
}
