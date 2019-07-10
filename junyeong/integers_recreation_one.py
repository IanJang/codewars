import math


def list_squared(m, n):
    ret = []
    for num in range(m, n + 1):
        sum_ = op_optimized_sum_square(num)
        if math.sqrt(sum_) % 1 == 0:
            ret.append([num, sum_])

    return ret


sum_square_cache = {}


def op_optimized_sum_square(n):
    if n in sum_square_cache:
        return sum_square_cache[n]
    i = 1
    square_sum = 0
    while i ** 2 < n:
        if n % i == 0:
            square_sum += (n // i) ** 2 + i ** 2
        i += 1
    if i ** 2 == n:
        square_sum += i ** 2
    sum_square_cache[n] = square_sum
    return square_sum


def get_one_example(num):
    sum = 0
    ret = []
    for i in range(1, num + 1):
        sq = i * i
        if num % i == 0:
            sum += sq
    if math.sqrt(sum) % 1 == 0:
        ret = [num, sum]
    return ret


def get_divisors(num):
    return [i for i in range(1, num + 1) if num % i == 0]


def get_squared_divisors(num):
    return [i * i for i in range(1, num + 1) if num % i == 0]


def test_all():
    assert get_divisors(42) == [1, 2, 3, 6, 7, 14, 21, 42]
    assert get_squared_divisors(42) == [1, 4, 9, 36, 49, 196, 441, 1764]

    assert get_one_example(1) == [1, 1]
    assert get_one_example(42) == [42, 2500]
    assert get_one_example(246) == [246, 84100]

    assert list_squared(1, 250) == [[1, 1], [42, 2500], [246, 84100]]
    assert list_squared(42, 250) == [[42, 2500], [246, 84100]]
    assert list_squared(250, 500) == [[287, 84100]]


def sum_square(nn):
    # math.sqrt(1).is_integer()
    return sum(([i ** 2 for i in range(1, nn + 1) if nn % i == 0]))


def optimized_sum_square(n):
    sum = n ** 2
    loop_count = 0
    for i in range(1, n // 2 + 1):
        loop_count += 1
        if n % i == 0:
            sum += i ** 2
    print("loop_count %s" % loop_count)
    return sum


if __name__ == '__main__':
    print(op_optimized_sum_square(1))

