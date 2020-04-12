#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>

#define WIDTH (1000)
#define HEIGHT (1000)

int main(int argc, char **argv)
{

	int8_t grid[WIDTH][HEIGHT] = {{0}};

	FILE *instructions_file = fopen("input.txt", "r");
	FILE *new_file = fopen("result.txt", "w");

	for(int row = 0; row < HEIGHT; row++)
	{
		for(int col = 0; col < WIDTH; col++)
		{
			//printf("%d", grid[row][col]);
			fprintf(new_file, "%d", grid[row][col]);
		}
		fprintf(new_file, "\n");
	}

	return 0;
}

//void save_grid()
