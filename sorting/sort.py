# Jakub_Klimek 407457


from typing import List, Tuple


def quicksort(data: List[int], start: int = 0, stop: int = None) -> List[int]:

    if stop is None:
        stop = len(data) - 1

    l = data[:]
    i = start
    j = stop
    pivot = l[(i + j) // 2]

    while i < j:
        while l[i] < pivot:
            i += 1
        while l[j] > pivot:
            j -= 1
        if i <= j:
            (l[i], l[j]) = (l[j], l[i])
            i += 1
            j -= 1
    if start < j:
        l = quicksort(l, start, j)
    if i < stop:
        l = quicksort(l, i, stop)
    return l


def bubblesort(data: List[int]) -> Tuple[List[int], int]:
    n = len(data)
    p = 0
    l = data[:]
    while n > 1:
        swap = False
        for i in range(n-1):
            if l[i] > l[i+1]:
                (l[i+1], l[i]) = (l[i], l[i+1])
                swap = True
            p += 1
        if not swap:
            break
        n -= 1
    return l, p
