#include <stdio.h>
#include <malloc.h>
#include <string.h>

typedef size_t BOOL;
#define TRUE (1)
#define FALSE (0)

BOOL is_duplicate(int alphabet[]);

int main(int argc, char **argv)
{
	printf("Day 5 Advent 2015\n");
	FILE *input_file = fopen("input.txt", "r");

	//char string[10];
	//fprintf(input_file, "%s\n", string);
	//printf("%s", string);
	char *line = NULL, *ptr = NULL;
	size_t len = 0;
	ssize_t read;

	char * vowls = "aeiou";
	int vowls_num;
	int alphabet[26];
	int nice_amount = 0;
	BOOL found_double = FALSE;

	while (getline(&line, &len, input_file) != -1) {
        vowls_num = 0;
        memset(alphabet, 0, sizeof(alphabet));
        ptr = line;
        found_double = FALSE;
        // printf("%s", line);

        while(*ptr != '\n')
        {
        	if(strchr(vowls, *ptr) != NULL)
        	{
        		vowls_num++;
        	}
        	if(*ptr - 97 > 0)
        	{
        		alphabet[*ptr - 97] += 1;
        		if (!found_double && alphabet[*ptr - 97] > 1 && *(ptr - 1) == *ptr)
        		{
        			found_double = TRUE;
        		}
        	}

        	ptr++;
        }

        if( (strstr(line, "ab") == NULL) && (strstr(line, "cd") == NULL) && (strstr(line, "pq") == NULL) && (strstr(line, "xy") == NULL) &&
        	(vowls_num >= 3) && found_double)
        {
        	printf("Nice\n");
        	nice_amount++;
        }
        else
        {
        	printf("Naughty\n");
        }

    }

    printf("%d\n", nice_amount);

    if (line)
    {
    	free(line);
    }

	fclose(input_file);
	return 0;
}

BOOL is_duplicate(int *alphabet)
{
	for(int i = 0; i < 26; i++)
	{
		if(alphabet[i] > 1)
		{
			return TRUE;
		}
	}
	return FALSE;
}