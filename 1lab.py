#Выполнил студент группы БСТ2201
#Импорт необходимых компонентов для выполнения лабораторной работы
import random
import time

#1
print("\n1\nHello, World! I am Andrey.")

#2
print("\n2")
def gen_matrix(m, n, min_limit, max_limit):
    matrix = []
    for i in range(m):
        row = []
        for c in range(n):
            row.append(random.randint(min_limit, max_limit))
        matrix.append(row)
    return matrix

print("----\nПриём входных данных\n----")
m = int(input("Количество строк: "))
n = int(input("Количество колонок: "))
min_limit = int(input("Минимальный порог диапазона: "))
max_limit = int(input("Максимальный порог диапазона: "))

matrix = gen_matrix(m, n, min_limit, max_limit)
print("----\nСгенерированная матрица:\n-----")
for row in matrix:
    print(row)

#3
print("\n3")

print("----\nИсходная матрица:\n-----")
for row in matrix:
    print(row)
#Сортировка выбором
def selection_sort_row(matrix):
    sorted_matrix = [] #Создаю новую матрицу
    for row in matrix:
        sorted_row = row[:]  #Создаю копию строки
        n = len(sorted_row) #Получаю длину строки
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if sorted_row[j] < sorted_row[min_index]:
                    min_index = j
            if min_index != i:
                sorted_row[i], sorted_row[min_index] = sorted_row[min_index], sorted_row[i]
        sorted_matrix.append(sorted_row)
    return sorted_matrix

start_time = time.time()

selection_matrix = selection_sort_row(matrix)

print("----\nСортировка выбором:\n-----")
for row in selection_matrix:
    print(row)

selection_time = round((time.time()-start_time)*1000)

#Сортировка вставкой

def insertion_sort_matrix(matrix):
    sorted_matrix = [] #Создаю новую матрицу
    for row in matrix:
        sorted_row = row[:] #Создаю копию строки
        for i in range(1, len(sorted_row)):
            key = sorted_row[i]
            j = i - 1
            while j >= 0 and key < sorted_row[j]:
                sorted_row[j + 1] = sorted_row[j]
                j -= 1
            sorted_row[j + 1] = key
        sorted_matrix.append(sorted_row)
    return sorted_matrix

start_time = time.time()

insertion_matrix = insertion_sort_matrix(matrix)

print("----\nСортировка вставкой:\n-----")
for row in insertion_matrix:
    print(row)

insertion_time = round((time.time()-start_time)*1000)

#Сортировка пузырьком

def bubble_sort_matrix(matrix):
    sorted_matrix = [row[:] for row in matrix]  #Создаю копию матрицы
    for row in sorted_matrix:
        n = len(row)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if row[j] > row[j+1]:
                    row[j], row[j+1] = row[j+1], row[j]
    return sorted_matrix

start_time = time.time()

bubble_matrix = insertion_sort_matrix(matrix)

print("----\nСортировка пузырьком:\n-----")
for row in bubble_matrix:
    print(row)

bubble_time = round((time.time()-start_time)*1000)

#Сортировка Шелла

def shell_sort_matrix(matrix):
    sorted_matrix = [row[:] for row in matrix]  #Создаю копию матрицы
    for row in sorted_matrix:
        n = len(row)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = row[i]
                j = i
                while j >= gap and row[j - gap] > temp:
                    row[j] = row[j - gap]
                    j -= gap
                row[j] = temp
            gap //= 2
    return sorted_matrix

start_time = time.time()

shell_matrix = insertion_sort_matrix(matrix)

print("----\nСортировка Шелла:\n-----")
for row in shell_matrix:
    print(row)

shell_time = round((time.time()-start_time)*1000)

#Быстрая сортировка

def quick_sort_matrix(matrix):
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
    sorted_matrix = [quicksort(row) for row in matrix]
    return sorted_matrix

start_time = time.time()

quicksort_matrix = quick_sort_matrix(matrix)

print("----\nБыстрая сортировка:\n-----")
for row in quicksort_matrix:
    print(row)

quicksort_time = round((time.time()-start_time)*1000)

#Турнирная сортировка

def tournament_sort(matrix):
    # Функция для сравнивания элементов матрицы
    def tournament(matrix, i, j):
        if i == j:
            return i
        winner_left = tournament(matrix, i, (i + j) // 2)
        winner_right = tournament(matrix, (i + j) // 2 + 1, j)
        return i if matrix[winner_left] < matrix[winner_right] else j
    
    #Функция построения отсортированной матрицы
    def build_sorted(matrix):
        sorted_arr = [] #Создаю новую строку
        while matrix:
            winner_index = tournament(matrix, 0, len(matrix) - 1) #Получаю индекс выигравшего элемента
            sorted_arr.append(matrix.pop(winner_index)) #Подставляю выигравший элемент
        return sorted_arr
    
    sorted_matrix = [build_sorted(row) for row in matrix]
    return sorted_matrix

start_time = time.time()

tournament_matrix = insertion_sort_matrix(matrix)

print("----\nТурнирная сортировка:\n-----")
for row in tournament_matrix:
    print(row)

tournament_time = round((time.time()-start_time)*1000)

start_time = time.time()

base_matrix = [sorted(row) for row in matrix]

print("----\nСтандартная сортировка:\n-----")
for row in base_matrix:
    print(row)

base_time = round((time.time()-start_time)*1000)

print("\nИтоги:\n")
print("--- сортировка выбором длилась {0} ms ---".format(selection_time))
print("--- сортировка вставкой длилась {0} ms ---".format(insertion_time))
print("--- сортировка пузырьком длилась {0} ms ---".format(bubble_time))
print("--- сортировка Шелла длилась {0} ms ---".format(shell_time))
print("--- Быстрая сортировка рекурсией длилась {0} ms ---".format(quicksort_time))
print("--- Турнирная сортировка длилась {0} ms ---".format(tournament_time))
print("--- Стандартная сортировка длилась {0} ms ---".format(base_time))