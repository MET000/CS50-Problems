#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }

    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count - 1; i++)
    {
        int current = ranks[i];
        for (int j = i; j < candidate_count - 1; j++)
        {
            preferences[current][ranks[j + 1]] += 1;
        }
    }

    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO
    int index = 0;
    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = i; j < candidate_count - 1; j++)
        {
            if (preferences[i][j + 1] > preferences[j + 1][i])
            {
                pairs[index].winner = i;
                pairs[index].loser = j + 1;
                index++;
                pair_count++;
            }
            else if (preferences[i][j + 1] < preferences[j + 1][i])
            {
                pairs[index].winner = j + 1;
                pairs[index].loser = i;
                index++;
                pair_count++;
            }
        }
    }

    for (int i = 0; i < pair_count; i++)
    {
        printf("(%i, %i)\n", pairs[i].winner, pairs[i].loser);
    }

    printf("\n");

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    typedef struct
    {
        int winner;
        int loser;
        int strength_of_victory;
    } victory;

    victory strength[pair_count];
    int index = 0;

    for (int i = 0; i < candidate_count - 1; i++)
    {
        for  (int j = i; j < candidate_count - 1; j++)
        {
            if (preferences[i][j+1] > preferences[j+1][i])
            {
                strength[index].winner = i;
                strength[index].loser = j + 1;
                strength[index].strength_of_victory = preferences[i][j+1];
                index++;
            }

            else if (preferences[i][j+1] < preferences[j+1][i])
            {
                strength[index].winner = j + 1;
                strength[index].loser = i;
                strength[index].strength_of_victory = preferences[j+1][1];
                index++;
            }

        }
    }

    for (int i = 0; i < pair_count; i++)
    {
        printf("(%i, %i)\n", strength[i].winner, strength[i].loser);
    }
    printf("\n");


    while (true)
    {
        int marker = 0;

        for (int i = 0; i < pair_count - 1; i++)
        {
            if (strength[i].strength_of_victory < strength[i+1].strength_of_victory)
            {
                int higher_winner = strength[i+1].winner;
                int higher_loser = strength[i+1].loser;
                int higher_strength = strength[i+1].strength_of_victory;

                strength[i+1].winner = strength[i].winner;
                strength[i+1].loser = strength[i].loser;
                strength[i+1].strength_of_victory = strength[i].strength_of_victory;

                strength[i].winner = higher_winner;
                strength[i].loser = higher_loser;
                strength[i].strength_of_victory = higher_strength;

                marker++;
            }
        }

        if (marker == 0)
        {
            break;
        }
    }

    for (int i = 0; i < pair_count; i++)
    {
        printf("(%i, %i)\n", strength[i].winner, strength[i].loser);
    }
    printf("\n");


    for (int i = 0; i < pair_count; i++)
    {
        pairs[i].winner = strength[i].winner;
        pairs[i].loser =  strength[i].loser;

    }


    for (int i = 0; i < pair_count; i++)
    {
        printf("(%i, %i)\n", pairs[i].winner, pairs[i].loser);
    }

    printf("\n");

    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    for (int i = 0; i < pair_count; i++)
    {
        int current_winner = pairs[i].winner;
        int current_loser = pairs[i].loser;
        int marker = 0;
        int catch_j = 0;
        int initialize = 0;

        while (true)
        {
            if (current_winner == pairs[i].winner)
            {
                initialize = catch_j;       // catch_j is a reminder used to continue the search where it should be.
            }

            for (int j = initialize; j < i; j++)
            {
                if (current_winner == pairs[i].winner)
                {
                    catch_j++;
                }

                if (current_winner == pairs[j].loser)
                {
                    if (pairs[j].winner == current_loser) // this will create a cycle !
                    {
                        marker = 10;
                        break;
                    }
                    else if (pairs[j].winner != current_loser) // update current winner and continue searching.
                    {
                        current_winner = pairs[j].winner;
                        marker = 1;

                        break;
                    }
                }
            }

            if (marker == 10)
            {
                break;
            }

            else if (marker == 1)
            {
                marker = 0;
                continue;
            }

            else if (marker == 0)
            {
                if (catch_j != i)
                {
                    current_winner = pairs[i].winner; // we reset current_winner to search other pairs.
                    continue;
                }

                locked[pairs[i].winner][pairs[i].loser] = true; // if catch j == i and marker = 0 this means
                                                                // we did not found the case leading to a cycle.
                break;
            }
        }
    }

    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            printf("%i", locked[i][j]);
        }

        printf("\n");
    }
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
        {
            int x = 0;
            for (int j = 0; j < candidate_count; j++)
            {
                if (locked[j][i] == true)
                {
                    x++;
                }
            }
            if (x == 0)
            {
                printf("%s\n", candidates[i]);
            }
        }
    return;
}
