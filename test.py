def equalElements(mas):
    """
    Функция, которая находит общие элементы во всех подсписках в списке списков.

    :param mas: список списков
    :return: множество общих элементов
    """
    seen = set()
    if len(mas) == 0:
        return seen  # Если нет списков, возвращаем пустое множество

    for element in mas[0]:
        count = 1
        for lst in mas[1:]:
            count += 1 if element in lst else False
        if count == len(mas):
            seen.add(element)  # Добавляем элемент только если он встречается во всех списках

    return seen


def test_equalElements():
    """
    Функция для тестирования модуля equalElements с различными примерами.
    """
    # Тест 1: Простой случай с одинаковыми элементами
    mas1 = [[1, 2, 3], [2, 3, 4], [2, 3, 5]]
    assert equalElements(mas1) == {2, 3}, "Тест 1 не пройден"

    # Тест 2: Без общих элементов
    mas2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert equalElements(mas2) == set(), "Тест 2 не пройден"

    # Тест 3: Все списки пустые
    mas3 = [[], [], []]
    assert equalElements(mas3) == set(), "Тест 3 не пройден"

    # Тест 4: Один список пустой
    mas4 = [[1, 2, 3], [], [1, 2, 3]]
    assert equalElements(mas4) == set(), "Тест 4 не пройден"

    # Тест 5: Все элементы одинаковы
    mas5 = [[1, 1, 1], [1, 1], [1]]
    assert equalElements(mas5) == {1}, "Тест 5 не пройден"

    # Тест 6: Общие элементы строки и числа
    mas6 = [[1, "e", 6, 89, 9], [2, 5, "6", 7, 6], [23, "6", 7, 8, 6]]
    assert equalElements(mas6) == {6}, "Тест 6 не пройден"

    print("Все тесты пройдены!")


# Запуск тестов
test_equalElements()
