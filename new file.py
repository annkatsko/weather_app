def is_int(value) -> bool:
    return type(value) == int


def odd_sum(some_list: list) -> int:
    sum = 0
    for i in some_list:
        if is_int(i):
            if i % 2 != 0:
                sum += i
    return sum


if __name__ == '__main__':
    d = [1.4, '2', '3', True]
    try:
        print(odd_sum(d))
    except TypeError:
        print("Все элементы списка должны быть целыми числами")
    else:
        print('All executed well')
