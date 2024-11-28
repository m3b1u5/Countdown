# ДЗ: Счетчик обратного отсчета
import time


def get_num():
    while True:
        try:
            num = int(input("Введите целое положительное число: "))
            if num <= 0:
                raise ValueError
        except ValueError:
            print("Ошибка, некорректное число")
        else:
            return num


def main():
    target = get_num()
    n = target
    while n >= 0:
        print(n, "*" * int((n * 20 / target)))
        time.sleep(0.5)
        n -= 1


main()
