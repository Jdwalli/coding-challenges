#include <stdio.h>
#include <stdlib.h>

FILE *openInputFile(const char *filename, const char *mode)
{
    FILE *file = fopen(filename, mode);
    if (file == NULL)
    {
        fprintf(stderr, "Error opening file: %s\n", filename);
    }
    return file;
}

int compare(const void *a, const void *b)
{
    return (*(int *)b - *(int *)a);
}

int main(int argc, char *argv[])
{

    FILE *file = openInputFile("input.txt", "r");

    if (file == NULL)
    {
        return 1;
    }

    int *calories = malloc(sizeof(int));

    if (calories == NULL)
    {
        fprintf(stderr, "Allocation error.\n");
        return 1;
    }

    int maxCalories = 0;
    int elfIndex = 0;
    int calorie;
    char input[20];

    while (fgets(input, sizeof(input), file) != NULL)
    {
        if (input[0] == '\n')
        {
            if (calories[elfIndex] > maxCalories)
            {
                maxCalories = calories[elfIndex];
            }

            elfIndex++;
            calories = realloc(calories, (elfIndex + 1) * sizeof(int));
            if (calories == NULL)
            {
                fprintf(stderr, "Allocation error.\n");
                return 1;
            }
            calories[elfIndex] = 0;
        }
        else
        {
            calorie = atoi(input);
            calories[elfIndex] += calorie;
        }
    }

    if (calories[elfIndex] > maxCalories)
    {
        maxCalories = calories[elfIndex];
    }

    printf("Solution One: %d\n", maxCalories);

    qsort(calories, elfIndex + 1, sizeof(int), compare);

    printf("Solution Two: %d\n", calories[0] + calories[1] + calories[2]);

    fclose(file);
    free(calories);

    return 0;
}