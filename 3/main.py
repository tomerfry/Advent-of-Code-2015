#! /usr/bin/python

movement = {
    '^': lambda pos_x, pos_y: (pos_x, pos_y + 1),
    '>': lambda pos_x, pos_y: (pos_x + 1, pos_y),
    'v': lambda pos_x, pos_y: (pos_x, pos_y - 1),
    '<': lambda pos_x, pos_y: (pos_x - 1, pos_y),
}

def main():
    with open('input.txt', 'r') as input_file:
        instructions = input_file.read()

    #pos_list = {0: {0: 0}}
    pos_list = {}
    santa_pos = (0, 0)
    bot_pos = (0, 0)
    pos_list[santa_pos] = 1
    santa_turn = True

    print('Day 3 Advent 2015')

    for instruction in instructions:
        if santa_turn:
            santa_pos = movement[instruction](*santa_pos)
        else:
            bot_pos = movement[instruction](*bot_pos)

        santa_turn = not santa_turn

        if santa_pos in pos_list:
            pos_list[santa_pos] += 1
        else:
            pos_list[santa_pos] = 1

        if bot_pos in pos_list:
            pos_list[bot_pos] += 1
        else:
            pos_list[bot_pos] = 1

    print('Amount of positions visited: {}'.format(len(pos_list)))


#        if current_pos[0] in pos_list:
#            if pos_list[current_pos[0]] == current_pos[1]:
#               pos_list[current_pos[0]][current_pos[1]]
# def is_visited(pos, pos_list):

#def handle_pos(pos, pos_list):

if __name__ == '__main__':
    main()