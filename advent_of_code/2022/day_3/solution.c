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

char findCommonCharacter(char *firstCompartment, char *secondCompartment)
{
    for (int i = 0; firstCompartment[i] != '\0'; i++)
    {
        for (int j = 0; secondCompartment[j] != '\0'; j++)
        {
            if (firstCompartment[i] == secondCompartment[j])
            {
                return firstCompartment[i];
            }
        }
    }
    return '\0';
}

int calculatePriority(char *firstCompartment, char *secondCompartment)
{
    char commonCharacter = findCommonCharacter(firstCompartment, secondCompartment);

    if (commonCharacter >= 'a' && commonCharacter <= 'z')
    {
        return commonCharacter - 'a' + 1;
    }
    if (commonCharacter >= 'A' && commonCharacter <= 'Z')
    {
        return commonCharacter - 'A' + 27;
    }

    return 0;
}

void splitCompartments(const char *source, int len, char **firstCompartment, char **secondCompartment)
{

    int split = len / 2;

    *firstCompartment = (char *)malloc(len + 1);
    *secondCompartment = (char *)malloc(len - split + 1);

    strncpy(*firstCompartment, source, split);
    (*firstCompartment)[split] = '\0';

    strcpy(*secondCompartment, source + split);
}

int main(int argc, char *argv[])
{

    FILE *file = openInputFile("input.txt", "r");

    if (file == NULL)
    {
        return 1;
    }

    char input[50];
    int priority = 0;

    while (fgets(input, sizeof(input), file) != NULL)
    {

        char *firstCompartment, *secondCompartment;
        splitCompartments(input, strlen(input), &firstCompartment, &secondCompartment);
        priority += calculatePriority(firstCompartment, secondCompartment);
    }

    printf("Solution One: %d\n", priority);

    fclose(file);

    return 0;
}