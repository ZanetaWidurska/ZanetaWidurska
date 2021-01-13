# -*- coding: utf-8 -*-
from point import Point
from point import normalize_angle


def main():
    with open('teksty.txt', 'r') as file:
        data = file.readlines()

    points = []
    for line in data:
        point = line.strip().split()
        points.append(Point(point[0], point[1], point[2]))

    length = points[0].get_length(points[1])
    azimuth = points[0].get_azimuth(points[1])
    angle = 0
    for i in range(1,len(points)-1):   
        azimuth += points[i].get_azimuth(points[i+1])
        length += points[i].get_length(points[i+1])
        angle += points[i].get_angle(points[i-1],points[i+1])
    print(f'length = {length}')
    print(f'azimuth = {azimuth}')
    print(f'angle = {angle}')


if __name__ == '__main__':
    main()
