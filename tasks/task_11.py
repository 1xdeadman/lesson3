"""
Внимательно прочитайте код в этом файле и добавьте свой код везде, где встречается <YOUR CODE>.
Перед каждым заданием вы можете прочитать его описание, помеченное меткой TODO.
для проверки введите из папки с проектом: pytest -vm task_7
"""
from typing import Any, Union, Tuple, Generator


class Parent:
    common_value = []

    def __init__(self, new_value: int):
        if isinstance(new_value, int):
            self.test_value = new_value
        self.data = "text"


# TODO: реализуйте класс Child, являющийся дочерним от класса Parent.
#  1. Ваш класс должен создавать в своем конструкторе новый атрибут экземпляра класса child_data и инициализировать его
#  Словарем со значением {"key": "value"}.
#  2. Ваш класс должен полностью повторять логику создания родительского класса.
#  3. Ваш класс должен реализовывать классовый метод create_zero_class(cls). Данный метод должен возвращать новый
#  экземпляр такого эе класса, что и у вызвавшего! его элемента.

"<YOUR CODE>"
class Child():
    pass
