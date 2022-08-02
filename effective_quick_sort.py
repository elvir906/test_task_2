"""
"Эффективная быстрая сортировка".
Решение основано на рекурсии, а так же на модификации быстрой сортировки,
называемой 'in-place', позволяющей значительно сэкономить память.

Сложность этого метода в худшем случае O(n^2), в лучшем - O(n * log(n)).
Это зависит от выбора опроного элемента.

Немного подкорректировал выполненною мною самостоятельную работу
в рамках обучения на курсе по 'Pyhton-разработчик'
при прохождении темы 'Алгоритмы и структуры данных'.
"""


def moving_elements(numbers: list, left: int, right: int) -> int:
    """
    Реализация перемещения элементов в массиве. Выбирается опорный элемент,
    который собирает справа от себя элементы, больше, чем он сам, и слева
    - меньше по значению.
    """
    pivot = (numbers[left])
    left_plus = left + 1
    right_minus = right - 1
    while True:
        if (left_plus <= right_minus and numbers[right_minus] > pivot):
            right_minus -= 1
        elif (left_plus <= right_minus and numbers[left_plus] < pivot):
            left_plus += 1
        elif (
            numbers[right_minus] > pivot
        ) or (
            numbers[left_plus] < pivot
        ):
            continue
        if left_plus <= right_minus:
            numbers[left_plus], numbers[
                right_minus
            ] = numbers[right_minus], numbers[left_plus]
        else:
            numbers[left], numbers[
                right_minus
            ] = numbers[right_minus], numbers[left]
            return right_minus


def quick_sort(numbers: list, left: int, right: int) -> None:
    """
    Реализация рекурсии
    """
    if (right - left) > 1:
        separator = moving_elements(numbers, left, right)
        quick_sort(numbers, left, separator)
        quick_sort(numbers, separator + 1, right)


if __name__ == '__main__':
    """
    Основная логика программы
    """
    print('Введите массив чисел через пробел')
    numbers = [int(number) for number in input().strip().split()]

    quick_sort(numbers, 0, len(numbers))
    print(*numbers)
