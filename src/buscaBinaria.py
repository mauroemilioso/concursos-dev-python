import collections

def retornaListaOrdnadaBubbleSort(arr: collections):

    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def buscaBinaria(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

if __name__ == "__main__":
    lista = [50,1,55,45,12,4,20]
    retornaListaOrdnadaBubbleSort(lista)
    print(lista)
    print('Busca valor 4: ', buscaBinaria(lista,4))




    

