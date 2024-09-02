import random


def crear_matriz(filas, columnas):
    return [[random.randint(1, 50) for _ in range(columnas)] for _ in range(filas)]


def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{num:2d}" for num in fila))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def ordenar_fila(matriz, num_fila):
    fila = matriz[num_fila]
    bubble_sort(fila)
    matriz[num_fila] = fila

matriz = crear_matriz(5, 5)


print("Matriz original:")
imprimir_matriz(matriz)


while True:
    try:
        fila_a_ordenar = int(input("\nIngrese el número de fila a ordenar (0-4): "))
        if 0 <= fila_a_ordenar <= 4:
            break
        else:
            print("Por favor, ingrese un número entre 0 y 4.")
    except ValueError:
        print("Por favor, ingrese un número válido.")


ordenar_fila(matriz, fila_a_ordenar)


print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
imprimir_matriz(matriz)