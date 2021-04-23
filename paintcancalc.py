import math


def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)

    print(f'you\'ll need {num_of_cans} cans of paint')


paint_calc(30, 9, 5)
