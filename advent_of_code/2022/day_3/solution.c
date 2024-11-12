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

char findCommonChar(char *firstCompartment, char *secondCompartment)
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

char findCommonCharEx(char *firstLine, char *secondLine, char *thirdLine)
{

    for (int i = 0; firstLine[i] != '\0'; i++)
    {
        char ch = firstLine[i];

        if (strchr(secondLine, ch) && strchr(thirdLine, ch))
        {
            return ch;
        }
    }

    return '\0';
}

int calculatePriority(char commonCharacter)
{

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
        char commonCharacter = findCommonChar(firstCompartment, secondCompartment);
        priority += calculatePriority(commonCharacter);
    }

    printf("Solution One: %d\n", priority);
    priority = 0;

    fseek(file, 0, SEEK_SET);

    char input1[50], input2[50], input3[50];
    int lineCount = 0;

    while (!feof(file))
    {
        if (fgets(input1, sizeof(input1), file) != NULL)
        {
            lineCount++;
        }

        if (fgets(input2, sizeof(input2), file) != NULL)
        {
            lineCount++;
        }

        if (fgets(input3, sizeof(input3), file) != NULL)
        {
            lineCount++;
        }

        if (lineCount == 3)
        {
            char commonChar = findCommonCharEx(input1, input2, input3);
            priority += calculatePriority(commonChar);

            lineCount = 0;
        }
    }

    printf("Solution Two: %d\n", priority);

    fclose(file);

    return 0;
}