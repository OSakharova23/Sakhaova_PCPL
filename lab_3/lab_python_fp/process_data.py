import json
import sys
from random import randint
from print_result import print_result
from cm_timer import cm_timer_1


path = sys.argv[1] if len(sys.argv) > 1 else None

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted({result_1['job-name'].lower() for result_1 in arg if 'job-name' in result_1}, key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    salaries = [randint(100000, 200000) for i in arg]
    return [f"{profession}, зарплата {salary} руб." for profession, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
