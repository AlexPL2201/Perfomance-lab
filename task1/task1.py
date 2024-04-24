import sys


class CircularArray:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.arr = self.build_array()
        self.intervals = self.find_intervals()
        self.path = self.calculate_path()

    def build_array(self):
        return [i for i in range(1, self.n + 1)]

    def find_intervals(self):
        intervals = []
        start = 0
        while len(intervals) < self.n:
            end = (start + self.m - 1) % self.n
            interval = self.arr[start:end+1] if end > start else self.arr[start:] + self.arr[:end+1]
            intervals.append(interval)
            start = end if end < self.n else 0
            if start == 0 and len(intervals) < self.n:
                break
        return intervals

    def calculate_path(self):
        return [self.intervals[i][0] for i in range(0, len(self.intervals))]


def read_args():
    if len(sys.argv) > 2:
        return int(sys.argv[1]), int(sys.argv[2])
    print("Аргументы командной строки не обнаружены.")
    while True:
        try:
            n = int(input("Введите n: "))
            m = int(input("Введите m: "))
            if n <= 0 or m <= 0:
                raise ValueError("n и m должны быть положительными числами.")
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
    return n, m


if __name__ == '__main__':
    n, m = read_args()
    circular_array = CircularArray(n, m)
    print(f'Круговой массив: {circular_array.arr}')
    print(f'Путь: {circular_array.path}')
