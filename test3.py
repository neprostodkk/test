def min_operations_to_convert(A, B):
    m, n = len(A), len(B)
    
    # Создаем матрицу dp размером (m+1) x (n+1), где dp[i][j] будет хранить минимальное количество операций для преобразования A[:i] в B[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Инициализируем первую строку и первый столбец
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Заполняем матрицу dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]

# Пример использования
A = "123"
B = "456"
result = min_operations_to_convert(A, B)
print(f"Минимальное количество операций для преобразования строки A в строку B: {result}")
