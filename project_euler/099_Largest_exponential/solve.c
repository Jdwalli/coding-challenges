#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

FILE *openInputFile(const char *filename, const char *mode)
{
    FILE *file = fopen(filename, mode);
    if (file == NULL)
    {
        fprintf(stderr, "Error opening file: %s\n", filename);
    }
    return file;
}


int main(int argc, char *argv[])
{

    FILE *file = openInputFile("../assets/base_exp.txt", "r");

    if (file == NULL)
    {
        return 1;
    }

    long long a, b;

    double max_value = 0.0;
    int max_line = 0;
    int line = 1;

    while (fscanf(file, "%lld,%lld", &a, &b) == 2) {
        double value = b * log(a);
        if (value > max_value){
            max_value = value;
            max_line = line;
        }

        line++;
    }

    fclose(file);
    printf("%d", max_line);


    return 0;
}