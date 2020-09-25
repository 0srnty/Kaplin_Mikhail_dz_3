from timeit import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def main():
    n = 34
    r1 = revers(n)
    r2 = revers_2(n)
    r3 = revers_3(n)


print(timeit("revers(34)", setup= "from __main__ import revers"))
print(timeit("revers_2(34)", setup= "from __main__ import revers_2"))
print(timeit("revers_3(34)", setup= "from __main__ import revers_3"))
cProfile.run('main()')