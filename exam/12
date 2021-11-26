import random
n = int(input("Количество строк:"))
m = int(input("Количество столбцов:"))
matrix = [[random.randint(0,9) for w in range(m)] for q in range(n)]
for a in matrix:
        print(a)
main_diagonal = [matrix[w][q] for w in range(n) for q in range(m) if w==q]
print("Главная диагональ:", main_diagonal)
k = int(input("Номер строки"))
p = int(input("Номер столбца"))
first = [matrix[k-1][w] for w in range(m)]
second = [matrix[q][p-1] for q in range(n)]
print(first)
print(second)
r = int(input("Номер строки элемента"))
t = int(input("Номер столбца элемента"))
third = matrix[r-1][t-1]
print(third)
