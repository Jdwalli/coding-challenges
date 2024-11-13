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

int fully_contains_ranges(int a, int b, int c, int d) {
    return a >= c && b <= d || a <= c && b >= d;
}

int fully_contains(int a, int b, int c, int d){
    return a >= c && a <= d || b >= c && b <= d || fully_contains_ranges(a, b, c, d);
    

}

int main(int argc, char *argv[])
{

    FILE *file = openInputFile("input.txt", "r");

    if (file == NULL)
    {
        return 1;
    }

    int a, b, c, d;

    int one_range_fully_contains_other = 0;
    int any_overlap = 0;

    while (fscanf(file, "%u-%u,%u-%u", &a,&b, &c, &d) == 4) {
        one_range_fully_contains_other += fully_contains_ranges(a, b, c, d);
        any_overlap += fully_contains(a, b, c, d);
    }

    printf("Part 1 Solutions: %d\n", one_range_fully_contains_other);
    printf("Part 2 Solutions: %d\n", any_overlap);

    fclose(file);

    return 0;
}