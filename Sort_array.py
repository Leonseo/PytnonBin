def merge(array, left_index, right_index, middle):
    # Сделаем копии обоих массивов, которые мы пытаемся объединить

    # Второй параметр не является инклюзивным, поэтому мы должны увеличить его на 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Начальные значения переменных, которые мы используем для сохранения
    # отслеживать, где мы находимся в каждом массиве
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Проходим обе копии, пока не закончатся элементы в одной
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # Если у нашего left_copy есть меньший элемент, поместите его в отсортированную
        # часть, а затем двигаться вперед в left_copy (увеличивая указатель)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Напротив сверху
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Независимо от того, откуда мы взяли наш элемент
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # У нас закончились элементы либо в left_copy, либо в right_copy.
    # поэтому мы пройдемся по оставшимся элементам и добавим их
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

def merge_sort(array, left_index, right_index):
     if left_index >= right_index:
        return

     middle = (left_index + right_index)//2
     merge_sort(array, left_index, middle)
     merge_sort(array, middle + 1, right_index)
     merge(array, left_index, right_index, middle)

array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
merge_sort(array, 0, len(array) -1)
print(array)
