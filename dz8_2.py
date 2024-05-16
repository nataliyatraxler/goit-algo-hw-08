import heapq

def merge_k_lists(lists):
    # Ініціалізуємо мін-купу
    min_heap = []
    
    # Вставляємо перший елемент кожного списку у мін-купу
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента у списку)

    merged_list = []
    
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)
        
        # Якщо у списку ще залишилися елементи, додаємо наступний елемент до купи
        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1], list_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)

    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
