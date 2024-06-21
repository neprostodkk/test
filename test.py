import math

def is_perfect_square(num):
    sqrt = int(math.sqrt(num))
    return sqrt * sqrt == num

def find_largest_perfect_square(arr):
    max_perfect_square = None

    for num in arr:
        if is_perfect_square(num):
            if max_perfect_square is None or num > max_perfect_square:
                max_perfect_square = num

    return max_perfect_square

numbers = [4, 7, 9, 16, 25, 36, 49]
result = find_largest_perfect_square(numbers)

if result:
    print(f"Наибольшее число, являющееся полным квадратом: {result}")
else:
    print("В массиве нет чисел, являющихся полными квадратами.")