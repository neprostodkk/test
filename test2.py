def maximize_number(A, B):
    max_number = int(A)
    A = list(A)
    B = list(B)

    for i in range(len(A)):
        for j in range(len(B)):
            temp_A = A[:]
            temp_A[i] = B[j]
            new_number = int("".join(temp_A))
            if new_number > max_number:
                max_number = new_number

    return max_number

A = "123"
B = "598"
result = maximize_number(A, B)
print(f"Максимальное число, полученное из A: {result}")
