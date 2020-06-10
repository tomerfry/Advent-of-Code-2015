#include <stdio.h>
#include <malloc.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


#define WIDTH (100)
#define HEIGHT (100)
// #define WIDTH (6)
// #define HEIGHT (6)
#define STEPS (100)
// #define STEPS (4)
#define INPUT_FILE ("input.txt")
#define SAMPLE_FILE ("sample.txt")


void print_grid(char *grid, int width, int height)
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            printf("%c", grid[width * row + col]);
        }
        printf("\n");
    }
}

int count_live_cells(char *grid, int width, int height)
{
    int count = 0;
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            if (grid[row * width + col] == '#')
            {
                count++;
            }
        }
    }
    
    return count;
}

char *update(char *prev_grid)
{
    char *next_grid = malloc(WIDTH * HEIGHT);
    int neighbor_count = 0;

    for (int row = 0; row < HEIGHT; row++)
    {
        for (int col = 0; col < WIDTH; col++)
        {
            neighbor_count = 0;

            if (row - 1 >= 0 && col - 1 >= 0 && prev_grid[(row - 1) * WIDTH + (col - 1)] == '#')
            {
                neighbor_count++;
            }
            if (col - 1 >= 0 && prev_grid[row * WIDTH + (col - 1)] == '#')
            {
                neighbor_count++;
            }
            if (row + 1 < HEIGHT && col - 1 >= 0 && prev_grid[(row + 1) * WIDTH + (col - 1)] == '#')
            {
                neighbor_count++;
            }
            
            if (row - 1 >= 0 && prev_grid[(row - 1) * WIDTH + col] == '#')
            {
                neighbor_count++;
            }
            if (row + 1 < HEIGHT && prev_grid[(row + 1) * WIDTH + col] == '#')
            {
                neighbor_count++;
            }

            if (row - 1 >= 0 && col + 1 < WIDTH && prev_grid[(row - 1) * WIDTH + (col + 1)] == '#')
            {
                neighbor_count++;
            }
            if (col + 1 < WIDTH && prev_grid[row * WIDTH + (col + 1)] == '#')
            {
                neighbor_count++;
            }
            if (row + 1 < HEIGHT && col + 1 < WIDTH && prev_grid[(row + 1) * WIDTH + (col + 1)] == '#')
            {
                neighbor_count++;
            }

            if (prev_grid[row * WIDTH + col] == '#') 
            {
                if (neighbor_count == 2 || neighbor_count == 3)
                {
                    next_grid[row * WIDTH + col] = '#';
                }
                else
                {
                    next_grid[row * WIDTH + col] = '.';
                }
            }
            else
            {
                if (neighbor_count == 3)
                {
                    next_grid[row * WIDTH + col] = '#';
                }
                else
                {
                    next_grid[row * WIDTH + col] = '.';
                }
            }
        }
    }
    
    next_grid[0] = '#';
    next_grid[WIDTH - 1] = '#';
    next_grid[(HEIGHT - 1) * WIDTH + 0] = '#';
    next_grid[(HEIGHT - 1) * WIDTH + (WIDTH - 1)] = '#';

    free(prev_grid);
    return next_grid;
}

int main(int argc, char **argv)
{
    FILE *input_file = fopen(INPUT_FILE, "r");
    char *buf = malloc(WIDTH * HEIGHT);

    for (int row = 0; row < HEIGHT; row++)
    {
        for (int col = 0; col <= WIDTH; col++)
        {
            buf[WIDTH * row + col] = getc(input_file);
        }
        getc(input_file);
    }

    for (int i = 0; i < STEPS; i++)
    {
        buf = update(buf);
        print_grid(buf, WIDTH, HEIGHT);
        getchar();
    }

    // print_grid(buf, WIDTH, HEIGHT);
    printf("%d", count_live_cells(buf, WIDTH, HEIGHT));
    fclose(input_file);
}
