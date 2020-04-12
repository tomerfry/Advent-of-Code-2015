#include <iostream>
#include <fstream>
#include <iterator>


int main(int argc, char **argv)
{
	char c;
	int current_floor = 0, floors_visited = 0;
	bool visited_basement = 0;

	std::cout << "Day 1 of Advent2015" << std::endl;
	std::fstream fs;
	fs.open("input.txt", std::fstream::in);

//	do//
//	{
//	/	std::cout << c << " char" << std::endl;
//		fs.read(&c, 1);
//	}while(c != '\x00');
//

	while(fs >> c)
	{
		if(!(visited_basement))
		{
			floors_visited++;
		}

		//fs.read(&c, 1);
		std::cout << c << std::endl;
		switch(c)
		{
			case '(':
				current_floor++;
				break;
			case ')':
				current_floor--;
				break;
		}

		if(current_floor == -1)
		{
			visited_basement = 1;
		}
	}



	std::cout << "The floor is: " << current_floor << std::endl;
	std::cout << "For the " << floors_visited << " Time He visited the Basement." << std::endl;
	return 0;
}



