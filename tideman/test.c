






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
                initialize = catch_j;
            }

            for (int j = initialize; j < i; j++)
            {
                if (current_winner == pairs[i].winner)
                {
                    catch_j++;
                }

                if (current_winner == pairs[j].loser)
                {
                    if (pairs[j].winner == current_loser)
                    {
                        marker = 10;
                        break;
                    }
                    else if (pairs[j].winner != current_loser)
                    {
                        current_winner = pairs[j].winner;
                        marker = 1;

                        break;
                    }
                }

                else
                {
                    continue;
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

            else if (catch_j == i && marker == 0)
            {
                locked[pairs[i].winner][pairs[i].loser] = true;
                break;
            }

            else if (catch_j != i && marker == 0)
            {
                current_winner = pairs[i].winner;
                continue;
            }

        }
    }
