# №21 Задать список X длиной N, среди элементов которого есть положительные, отрицательные и
#     равные нулю из которого:
# a. сформировать новый список Y, взяв в него только те элементы из X, которые больше по
#    модулю заданного числа M.
# b. все положительные элементы в нём заменить на отрицательные.
# c. Вывести в консоль число M, исходный и результирующий списки.

def process_list(X, M):
    Y = [num for num in X if abs(num) > M]
    Y = [-num if num > 0 else num for num in Y]
    return Y


N = 8
X = list(range(-N//2, N//2))
M = 2

Y = process_list(X, M)

print("Число M:", M)
print("Исходный список X:", X)
print("Результирующий список Y:", Y)
