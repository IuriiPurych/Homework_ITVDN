"""
Задание 3
Взяв за основу код примера 06-iterable_with_an_iterator.py, расширьте функциональность класса MyList,
добавив методы для очистки списка, добавления элемента в произвольное место списка,
удаления элемента из конца и произвольного места списка.
"""
from typing import Any, List


class MyList(object):
    """Класс списка"""
    _length: int
    _head: object
    _tail: object

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(
                self,
                value: Any,
                prev_node: object = None,
                next_node: object = None) -> None:
            self.value = value
            self.prev = prev_node
            self.next = next_node

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self,
                 iterable: List = None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам
        # последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self,
                    index: int) -> object:
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)

    def clear(self):
        self._head = self._tail = None
        self._length = 0

    def insert(self,
               index: int,
               element: object) -> None:
        if  index < 0:
            raise ValueError('List index cannot be negative.')

        new_node = MyList._ListNode(element)

        if index == 0:
            new_node.next = self._head
            self._head.prev = self._head = new_node
        elif index >= self._length:
            new_node.prev = self._tail
            self._tail.next = self._tail = new_node
        else:
            node = self._head
            for _ in range(index - 1):
                node = node.next

            saved_next = node.next
            saved_prev = node.next.prev
            node.next.prev = new_node
            node.next = new_node
            new_node.prev = saved_prev
            new_node.next = saved_next
            self._length += 1

    def del_item(self, index):
        if index < 0 or index >= self._length:
            raise IndexError('The index out of range.')

        if index == 0:
            self._head = self._head.next
            self._head.prev = None
        elif index == self._length - 1:
            self._tail = self._tail.prev
            self._tail.next = None
        else:
            node = self._head
            for _ in range(index):
                node = node.next
            node.prev.next = node.next
            node.next.prev = node.prev

        self._length -= 1


def test_my_list():
    start: int = -30
    end: int = 30
    try:
        my_list_test: MyList = MyList(list([i for i in range(start, end)]))
        std_list: List = [i for i in range(start, end)]
        print(my_list_test)
        print(std_list)

        for i in range(start, end):
            assert my_list_test.__getitem__(i) == list.__getitem__(i)
    except AssertionError as e:
        print(e)


def main():
    test_my_list()
    # # Создание списка
    # my_list = MyList([0, 1, 2, 3, 4, 5])
    #
    # # Вывод длины списка
    # print(len(my_list))
    #
    # # Вывод самого списка
    # print(my_list)
    #
    # print()
    #
    # my_list.insert(11, 77)
    # # my_list.insert(element=77, index=0)
    #
    # print('List after inserted an element.')
    # print(my_list)
    #
    # my_list.del_item(len(my_list) - 1)
    # print('List after deleted the last element.')
    # print(my_list)
    #
    # my_list.del_item(0)
    # print('List after deleted the first element.')
    # print(my_list)
    #
    # # Повторный обход списка
    # for element in my_list:
    #     print(element)
    #
    # print('Clear my list.')
    # my_list.clear()
    # for element in my_list:
    #     print(element)


if __name__ == '__main__':
    main()