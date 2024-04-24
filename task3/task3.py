import sys
import os
import json


def read_args():
    if len(sys.argv) > 3:
        return sys.argv[1], sys.argv[2], sys.argv[3]
    raise ValueError("Аргументы командной строки не обнаружены. Пример: task3.py ")


def read_json(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Файл '{filename}' не найден.")
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def write_report(report, values, report_path):
    for test in report['tests']:
        set_values(test, values)

    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)


def set_values(test, report):
    for value in report['values']:
        if int(value['id']) == int(test['id']):
            test['value'] = value['value']
            break
    if 'values' in test:
        for sub_test in test['values']:
            set_values(sub_test, report)


if __name__ == '__main__':
    file1, file2, file3 = read_args()
    tests, values = read_json(file1), read_json(file2)
    write_report(tests, values, file3)

