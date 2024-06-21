def maximize_number(A, B):
    max_number = int(A)  # Изначально считаем A самым большим числом
    A = list(A)
    B = list(B)

    for i in range(len(A)):
        for j in range(len(B)):
            temp_A = A[:]  # Создаем копию A
            temp_A[i] = B[j]  # Заменяем цифру в A на цифру из B
            new_number = int("".join(temp_A))  # Преобразуем список обратно в число
            if new_number > max_number:
                max_number = new_number  # Обновляем максимальное число

    return max_number

A = "123"
B = "598"
result = maximize_number(A, B)
print(f"Максимальное число, полученное из A: {result}")
