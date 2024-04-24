import sys
import os


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, point: Point, r: int):
        self.center = point
        self.radius = r

    def is_point_in_circle(self, point: Point):
        distance = pow(point.x - self.center.x, 2) + pow(point.y - self.center.y, 2)
        squared_r = pow(self.radius, 2)
        if distance <= squared_r:
            return 1 if distance < squared_r else 0
        return 2


def read_args():
    if len(sys.argv) > 2:
        return sys.argv[1], sys.argv[2]
    raise ValueError("Аргументы командной строки не обнаружены.")


def read_file(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Файл '{filename}' не найден.")
    with open(filename, 'r') as f:
        data = f.read().split('\n')
    return data


def parse_circle_data(filename):
    data = read_file(filename)
    return [int(elem) for elem in data[0].split()], int(data[1])


def parse_points(filename):
    data = read_file(filename)
    return [[int(p) for p in point.split()] for point in data]


if __name__ == '__main__':
    file1, file2 = read_args()
    center, radius = parse_circle_data(file1)
    points_lst = [Point(point[0], point[1]) for point in parse_points(file2)]
    circle = Circle(Point(center[0], center[1]), radius)
    for point in points_lst:
        print(circle.is_point_in_circle(point))
