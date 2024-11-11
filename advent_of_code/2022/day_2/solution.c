#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *openInputFile(const char *filename, const char *mode)
{
    FILE *file = fopen(filename, mode);
    if (file == NULL)
    {
        fprintf(stderr, "Error opening file: %s\n", filename);
    }
    return file;
}

int calculateObjectPoints(char p2)
{
    int points = 0;
    switch (p2)
    {
    case 'A':
        points = 1;
        break;
    case 'X':
        points = 1;
        break;
    case 'B':
        points = 2;
        break;
    case 'Y':
        points = 2;
        break;
    case 'C':
        points = 3;
        break;

    case 'Z':
        points = 3;
        break;
    }
    return points;
}

int calculatePoints(char p1, char p2)
{
    int points = 0;

    points += calculateObjectPoints(p2);

    if ((p1 == 'A' && p2 == 'X') ||
        (p1 == 'B' && p2 == 'Y') ||
        (p1 == 'C' && p2 == 'Z'))
    {
        return points + 3;
    }

    if ((p1 == 'A' && p2 == 'Y') ||
        (p1 == 'B' && p2 == 'Z') ||
        (p1 == 'C' && p2 == 'X'))
    {
        return points + 6;
    }

    return points;
}

int calculateNewPoints(char p1, char p2)
{
    int points = 0;

    if (p2 == 'X')
    {
        switch (p1)
        {
        case 'A':
            return calculateObjectPoints('Z');
        case 'B':
            return calculateObjectPoints('X');
        case 'C':
            return calculateObjectPoints('Y');
        }
    }

    if (p2 == 'Y')
    {
        return calculateObjectPoints(p1) + 3;
    }

    if (p2 == 'Z')
    {
        switch (p1)
        {
        case 'A':
            return calculateObjectPoints('Y') + 6;
        case 'B':
            return calculateObjectPoints('Z') + 6;
        case 'C':
            return calculateObjectPoints('X') + 6;
        }
    }
}

int main(int argc, char *argv[])
{

    FILE *file = openInputFile("input.txt", "r");

    if (file == NULL)
    {
        return 1;
    }

    char input[20];
    int score1 = 0;
    int score2 = 0;

    while (fgets(input, sizeof(input), file) != NULL)
    {
        char *token1 = strtok(input, " ");
        char *token2 = strtok(NULL, " ");

        if (token1 != NULL && token2 != NULL)
        {
            char p1 = token1[0];
            char p2 = token2[0];
            score1 += calculatePoints(p1, p2);
            score2 += calculateNewPoints(p1, p2);
        }
    }

    printf("Solution One: %d\n", score1);
    printf("Solution Two: %d\n", score2);

    return 0;
}