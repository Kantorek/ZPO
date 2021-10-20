import random
import sort
from timeit import timeit

list_1 = list(range(1, 1001))  # posegregowana lista
list_2 = list(range(1000, 0, -1))  # lista od tyl
list_3 = [1] * 1000  # lista z jedną wartoscia
list_4 = random.sample(range(1, 2137420), 1000)  # lista losowa

b_t1 = timeit("sort.bubblesort(list_1)", number=1000, globals=globals())
q_t1 = timeit("sort.quicksort(list_1)", number=1000, globals=globals())

b_t2 = timeit("sort.bubblesort(list_2)", number=1000, globals=globals())
q_t2 = timeit("sort.quicksort(list_2)", number=1000, globals=globals())

b_t3 = timeit("sort.bubblesort(list_3)", number=1000, globals=globals())
q_t3 = timeit("sort.quicksort(list_3)", number=1000, globals=globals())

b_t4 = timeit("sort.bubblesort(list_4)", number=1000, globals=globals())
q_t4 = timeit("sort.quicksort(list_4)", number=1000, globals=globals())

print("Tablica", "Bubblesort", "Quicksort")
print("Posortowana:", b_t1, q_t1)
print("Od tył:", b_t2, q_t2)
print("Równa:", b_t3, q_t3)
print("Losowa:", b_t4, q_t4)
