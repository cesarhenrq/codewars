rows = int(input("Insert number of rows: "))
columns = int(input("Insert number of colums: "))
matrix = list()

for row in range(rows):
    matrix.append(list())
    for column in range(columns):
        element = int(input(f'Insert the element in position({row + 1}, {column + 1}): '))
        matrix[row].append(element)

print(matrix)

lst1 = list()
lst2 = list()

for i in range(len(matrix)):
    lst2.append(matrix[len(matrix) - 1 - i][i])

    for j in range(len(matrix)):
        print(matrix[i][j], end="   ")
        if i == j:
            lst1.append(matrix[i][j])

    print()


print(lst1)
print(lst2)
