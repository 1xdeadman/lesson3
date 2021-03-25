import pytest
import random as rnd
from tasks.task_9 import YourClass


@pytest.mark.task_9
def test_constructor():
    test_elem1 = YourClass()
    test_elem2 = YourClass()
    assert 'data' in dir(test_elem1)
    assert type(test_elem1.data) is list
    assert len(test_elem1.data) == 0
    assert id(test_elem1.data) != id(test_elem2.data)


@pytest.mark.task_9
def test_concat():
    test_elem = YourClass()

    text = ""
    for i in range(10000):
        new_value = rnd.randint(1, 10000)
        text += f"{new_value} "
        test_elem.data.append(new_value)

    text = text[:-1]

    assert test_elem.concat() == text