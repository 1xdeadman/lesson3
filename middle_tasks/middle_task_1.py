
# TODO:
#  0. Реализовать классу Data интерфейс Iterable. (Классс Data должен наследовать от Iterable)
#  1. Реализовать класс итератор, позволяющий итерировать по классу Data. (Классс должен наследовать от Iterator)
#       Итерация должна осуществляться по всем элементам обоих контейнеров: first_container и second_container.
#       Сначала проход осуществляется по first_container, затем по second_container
#       Должны возвращаться значения каждого контейнера.
#       Должны возвращаться значения каждого контейнера.
#  2. Реализовать оператор сложения для двух экземпляров класса Data.
#       Сложение осуществляется только если:
#           - у обоих экземпляров контейнеры first_container имеют одинаковые размеры
#           - у обоих экземпляров контейнеры second_container имеют одинаковые размеры и одинаковые ключи
#       Результатом сложения будет новый экземпляр класса Data, у которого:
#           - элементы контейнера first_container будут являться результатом поэлементного сложения контейнеров
#               first_container складываемых экземпляров
#           - элементы контейнера second_container будут являться результатом сложения элементов
#               по одинаковым ключам контейнеров second_container у складываемых экземпляров
#       Исходные объекты не изменяются


class Data:
    def __init__(self, first_data: list[int] = None, second_data: dict[str, str] = None):
        if first_data is None:
            self.first_container = []
        else:
            self.first_container = first_data.copy()

        if second_data is None:
            self.second_container = {}
        else:
            self.second_container = second_data.copy()

    def add_data(self, new_value: int):
        if type(new_value) is not int:
            raise TypeError("new_value is not int")
        self.first_container.append(new_value)

    def set_key_data(self, new_key: str, new_value: str):
        if type(new_value) is not str:
            raise TypeError("new_value is not int")
        if type(new_key) is not str:
            raise TypeError("new_key is not int")
        self.second_container[new_key] = new_value

