#include "helpers.h"
#include <math.h>


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float average =
                (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;

            image[i][j].rgbtBlue = round(average);
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtRed = round(average);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = image[i][j].rgbtBlue;
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;

            int sepia_blue = round((red * 0.272) + (green * 0.534) + (blue * 0.131));
            int sepia_green = round((red * 0.349) + (green * 0.686) + (blue * 0.168));
            int sepia_red = round((red * 0.393) + (green * 0.769) + (blue * 0.189));

            if (sepia_blue > 255)
            {
                sepia_blue = 255;
            }
            if (sepia_green > 255)
            {
                sepia_green = 255;
            }
            if (sepia_red > 255)
            {
                sepia_red = 255;
            }

            image[i][j].rgbtBlue = sepia_blue;
            image[i][j].rgbtGreen = sepia_green;
            image[i][j].rgbtRed = sepia_red;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            uint8_t left_blue;
            uint8_t left_green;
            uint8_t left_red;

            left_blue = image[i][j].rgbtBlue;
            left_green = image[i][j].rgbtGreen;
            left_red = image[i][j].rgbtRed;

            image[i][j].rgbtBlue = image[i][width - (j + 1)].rgbtBlue;
            image[i][j].rgbtGreen = image[i][width - (j + 1)].rgbtGreen;
            image[i][j].rgbtRed = image[i][width - (j + 1)].rgbtRed;

            image[i][width - (j + 1)].rgbtBlue = left_blue;
            image[i][width - (j + 1)].rgbtGreen = left_green;
            image[i][width - (j + 1)].rgbtRed = left_red;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    typedef struct
    {
        uint8_t AvBlue;
        uint8_t AvGreen;
        uint8_t AvRed;
    } NEWRGBTRIPLE;

    NEWRGBTRIPLE imm[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Case corner top left.
            if (i == 0 && j == 0)
            {
                imm[i][j].AvBlue = round((image[i][j].rgbtBlue + image[i][j + 1].rgbtBlue +
                                          image[i + 1][j].rgbtBlue + image[i + 1][j + 1].rgbtBlue) /
                                         4.0);
                imm[i][j].AvGreen =
                    round((image[i][j].rgbtGreen + image[i][j + 1].rgbtGreen +
                           image[i + 1][j].rgbtGreen + image[i + 1][j + 1].rgbtGreen) /
                          4.0);
                imm[i][j].AvRed = round((image[i][j].rgbtRed + image[i][j + 1].rgbtRed +
                                         image[i + 1][j].rgbtRed + image[i + 1][j + 1].rgbtRed) /
                                        4.0);
            }

            // Case corner top right.
            else if (i == 0 && j == (width - 1))
            {
                imm[i][j].AvBlue = round((image[i][j].rgbtBlue + image[i][j - 1].rgbtBlue +
                                          image[i + 1][j].rgbtBlue + image[i + 1][j - 1].rgbtBlue) /
                                         4.0);
                imm[i][j].AvGreen =
                    round((image[i][j].rgbtGreen + image[i][j - 1].rgbtGreen +
                           image[i + 1][j].rgbtGreen + image[i + 1][j - 1].rgbtGreen) /
                          4.0);
                imm[i][j].AvRed = round(image[i][j].rgbtRed + image[i][j - 1].rgbtRed +
                                        image[i + 1][j].rgbtRed + image[i + 1][j - 1].rgbtRed) /
                                  4.0;
            }

            // Case corner bottom left.
            else if (i == (height - 1) && j == 0)
            {
                imm[i][j].AvBlue = round((image[i][j].rgbtBlue + image[i][j + 1].rgbtBlue +
                                          image[i - 1][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue) /
                                         4.0);
                imm[i][j].AvGreen =
                    round((image[i][j].rgbtGreen + image[i][j + 1].rgbtGreen +
                           image[i - 1][j].rgbtGreen + image[i - 1][j + 1].rgbtGreen) /
                          4.0);
                imm[i][j].AvRed = round((image[i][j].rgbtRed + image[i][j + 1].rgbtRed +
                                         image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed) /
                                        4.0);
            }

            // Case corner bottom right.
            else if (i == (height - 1) && j == (width - 1))
            {
                imm[i][j].AvBlue = round((image[i][j].rgbtBlue + image[i][j - 1].rgbtBlue +
                                          image[i - 1][j].rgbtBlue + image[i - 1][j - 1].rgbtBlue) /
                                         4.0);
                imm[i][j].AvGreen =
                    round((image[i][j].rgbtGreen + image[i][j - 1].rgbtGreen +
                           image[i - 1][j].rgbtGreen + image[i - 1][j - 1].rgbtGreen) /
                          4.0);
                imm[i][j].AvRed = round((image[i][j].rgbtRed + image[i][j - 1].rgbtRed +
                                         image[i - 1][j].rgbtRed + image[i - 1][j - 1].rgbtRed) /
                                        4.0);
            }

            // Case edge top.
            else if (i == 0 && j != 0 && j != (width - 1))
            {
                imm[i][j].AvBlue = round((image[i][j].rgbtBlue + image[i][j + 1].rgbtBlue +
                                          image[i + 1][j].rgbtBlue + image[i + 1][j + 1].rgbtBlue +
                                          image[i][j - 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue) /
                                         6.0);
                imm[i][j].AvGreen =
                    round((image[i][j].rgbtGreen + image[i][j + 1].rgbtGreen +
                           image[i + 1][j].rgbtGreen + image[i + 1][j + 1].rgbtGreen +
                           image[i][j - 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen) /
                          6.0);
                imm[i][j].AvRed = round((image[i][j].rgbtRed + image[i][j + 1].rgbtRed +
                                         image[i + 1][j].rgbtRed + image[i + 1][j + 1].rgbtRed +
                                         image[i][j - 1].rgbtRed + image[i + 1][j - 1].rgbtRed) /
                                        6.0);
            }

            // Case edge left.
            else if (j == 0 && i != 0 && i != (height - 1))
            {
                imm[i][j].AvBlue =
                    round((image[i][j].rgbtBlue + image[i - 1][j].rgbtBlue +
                           image[i + 1][j].rgbtBlue + image[i][j + 1].rgbtBlue +
                           image[i - 1][j + 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue) /
                          6.0);
                imm[i][j].AvGreen =
                    round((image[i][j].rgbtGreen + image[i - 1][j].rgbtGreen +
                           image[i + 1][j].rgbtGreen + image[i][j + 1].rgbtGreen +
                           image[i - 1][j + 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen) /
                          6.0);
                imm[i][j].AvRed =
                    round((image[i][j].rgbtRed + image[i - 1][j].rgbtRed + image[i + 1][j].rgbtRed +
                           image[i][j + 1].rgbtRed + image[i - 1][j + 1].rgbtRed +
                           image[i + 1][j + 1].rgbtRed) /
                          6.0);
            }

            // Case edge bottom.
            else if (i == (height - 1) && j != 0 && j != (width - 1))
            {
                imm[i][j].AvBlue =
                    round((image[i][j].rgbtBlue + image[i - 1][j].rgbtBlue +
                           image[i][j + 1].rgbtBlue + image[i][j - 1].rgbtBlue +
                           image[i - 1][j + 1].rgbtBlue + image[i - 1][j - 1].rgbtBlue) /
                          6.0);
                imm[i][j].AvGreen =
                    round((image[i][j].rgbtGreen + image[i - 1][j].rgbtGreen +
                           image[i][j + 1].rgbtGreen + image[i][j - 1].rgbtGreen +
                           image[i - 1][j + 1].rgbtGreen + image[i - 1][j - 1].rgbtGreen) /
                          6.0);
                imm[i][j].AvRed =
                    round((image[i][j].rgbtRed + image[i - 1][j].rgbtRed + image[i][j + 1].rgbtRed +
                           image[i][j - 1].rgbtRed + image[i - 1][j + 1].rgbtRed +
                           image[i - 1][j - 1].rgbtRed) /
                          6.0);
            }

            // Case edge right.
            else if (j == (width - 1) && i != 0 && i != (height - 1))
            {
                imm[i][j].AvBlue =
                    round((image[i][j].rgbtBlue + image[i - 1][j].rgbtBlue +
                           image[i + 1][j].rgbtBlue + image[i][j - 1].rgbtBlue +
                           image[i - 1][j - 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue) /
                          6.0);
                imm[i][j].AvGreen =
                    round((image[i][j].rgbtGreen + image[i - 1][j].rgbtGreen +
                           image[i + 1][j].rgbtGreen + image[i][j - 1].rgbtGreen +
                           image[i - 1][j - 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen) /
                          6.0);
                imm[i][j].AvRed =
                    round((image[i][j].rgbtRed + image[i - 1][j].rgbtRed + image[i + 1][j].rgbtRed +
                           image[i][j - 1].rgbtRed + image[i - 1][j - 1].rgbtRed +
                           image[i + 1][j - 1].rgbtRed) /
                          6.0);
            }

            // Case middle.
            else
            {

                imm[i][j].AvBlue = round(
                    (image[i][j].rgbtBlue + image[i - 1][j].rgbtBlue + image[i + 1][j].rgbtBlue +
                     image[i][j + 1].rgbtBlue + image[i][j - 1].rgbtBlue +
                     image[i - 1][j - 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue +
                     image[i - 1][j + 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue) /
                    9.0);
                imm[i][j].AvGreen = round(
                    (image[i][j].rgbtGreen + image[i - 1][j].rgbtGreen + image[i + 1][j].rgbtGreen +
                     image[i][j + 1].rgbtGreen + image[i][j - 1].rgbtGreen +
                     image[i - 1][j - 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen +
                     image[i - 1][j + 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen) /
                    9.0);
                imm[i][j].AvRed =
                    round((image[i][j].rgbtRed + image[i - 1][j].rgbtRed + image[i + 1][j].rgbtRed +
                           image[i][j + 1].rgbtRed + image[i][j - 1].rgbtRed +
                           image[i - 1][j - 1].rgbtRed + image[i + 1][j + 1].rgbtRed +
                           image[i - 1][j + 1].rgbtRed + image[i + 1][j - 1].rgbtRed) /
                          9.0);
            }
        }
    }

    // Swap pixel colors of actual image to calculated pixel colors (stored in NEWRGBTRIPLE
    // imm[height][width]) related to blur filter.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = imm[i][j].AvBlue;
            image[i][j].rgbtGreen = imm[i][j].AvGreen;
            image[i][j].rgbtRed = imm[i][j].AvRed;
        }
    }

    return;
}
