import heapq

# Пірамідальне сортування (heapsort) з використанням модуля heapq
def heapsort(iterable):
    h = []
    # Додаємо кожне значення з iterable до купи
    for value in iterable:
        heapq.heappush(h, value)
    # Витягуємо елементи з купи у відсортованому порядку
    return [heapq.heappop(h) for _ in range(len(h))]

# Алгоритм мінімізації витрат на з'єднання мережевих кабелів
def min_cost_to_connect_cables(cables):
    if len(cables) <= 1:
        return 0
    
    # Перетворюємо список кабелів у мін-купу
    heapq.heapify(cables)
    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найменших елемента
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        # Об'єднуємо їх
        cost = first + second
        # Додаємо витрати на об'єднання до загальних витрат
        total_cost += cost
        # Вставляємо новий кабель назад до купи
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклади використання

# Пірамідальне сортування
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = heapsort(array)
print("Відсортований масив:", sorted_array)

# Мінімальні витрати на з'єднання кабелів
cables = [4, 3, 2, 6]
min_cost = min_cost_to_connect_cables(cables)
print("Мінімальні витрати на з'єднання кабелів:", min_cost)
