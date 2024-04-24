import sys
import os


def read_file(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Файл '{filename}' не найден.")
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(int(line.strip('\n')))
    return data


def read_args():
    if len(sys.argv) > 1:
        return sys.argv[1]
    raise ValueError("Аргументы командной строки не обнаружены.")


def to_avg(nums):
    average = sum(nums) // len(nums)
    steps = 0
    for i in range(len(nums)):
        step = 1 if nums[i] < average else -1
        while nums[i] != average:
            nums[i] += step
            steps += 1
    return nums, steps


def count_steps(nums):
    average = sum(nums) // len(nums)
    steps = sum([abs(num - average) for num in nums])
    return steps


if __name__ == '__main__':
    file_path = read_args()
    arr = read_file(file_path)
    arr_changed, counter = to_avg(arr.copy())
    # counter = count_steps(arr) # Кол-во шагов можно вычислить без изменения исходного массива
    print(f'{arr} --> {arr_changed}. Количество шагов: {counter}')
