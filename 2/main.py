#! /usr/bin/python

class Box(object):
    """
    Box class.
    """

    def __init__(self, length, width, height):
        self.l = length
        self.w = width
        self.h = height

    def get_surface_area(self):
        lw_area = self.l * self.w
        wh_area = self.w * self.h
        hl_area = self.h * self.l

        return (2 * (lw_area + wh_area + hl_area))

    def get_smallest_face(self):
        lw_area = self.l * self.w
        wh_area = self.w * self.h
        hl_area = self.h * self.l

        if lw_area < wh_area and lw_area < hl_area:
            return lw_area
        elif wh_area < hl_area:
            return wh_area
        else:
            return hl_area

    def get_smallest_peramiter(self):
        lw_per = 2 * (self.l + self.w)
        wh_per = 2 * (self.w + self.h)
        hl_per = 2 * (self.h + self.l)

        if lw_per < wh_per and lw_per < hl_per:
            return lw_per
        elif wh_per < hl_per:
            return wh_per
        else:
            return hl_per
    
    def get_bow_length(self):
        return (self.l * self.w) * self.h
def main():

    wrapping_paper = 0
    ribbon_length = 0

    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()

    print('Day 2 Advent 2015')

    for line in lines:
        length, width, height = tuple([int(num) for num in line.split('x')])
        box = Box(length, width, height)

        print('Box Surface Aread: {}, Smalles Face is {}'.format(box.get_surface_area() , box.get_smallest_face()))
        print('Ribbon Length: {}'.format(box.get_smallest_peramiter() + box.get_bow_length()))
        wrapping_paper += box.get_surface_area() + box.get_smallest_face()
        ribbon_length += box.get_smallest_peramiter() + box.get_bow_length()

    print('Total Area fo Wrapping Paper is {}'.format(wrapping_paper))
    print('Total Ribbon Length is {}'.format(ribbon_length))

if __name__ == '__main__':
	main()